import os
import sys
import winreg
import subprocess
import shutil
import time
import ctypes
from importlib import resources
from datetime import datetime

def log_message(message):
    """Записывает сообщение в лог-файл в директории monitor.exe"""
    log_dir = os.path.expanduser("~/AppData/Roaming/MyCorporateMonitor")
    log_file = os.path.join(log_dir, "monitor.log")
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Ошибка при записи в лог: {str(e)}")

def is_admin():
    """Проверяет, запущен ли процесс с правами администратора"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_resource_path(resource_name):
    """Получает путь к ресурсу, встроенному PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, resource_name)
    else:
        return resource_name

def check_and_restore_target():
    """Проверяет наличие target.exe, его автозагрузку и состояние, восстанавливает при необходимости"""
    if not is_admin():
        message = "monitor.exe не запущен с правами администратора. Это может помешать изменению реестра."
        print(message)
        log_message(message)
        return False

    target_dir = os.path.expanduser("~/AppData/Roaming/MyCorporateApp")
    target_exe_path = os.path.join(target_dir, "target.exe")

    # Проверяем наличие target.exe
    if not os.path.exists(target_exe_path):
        message = "target.exe не найден, восстанавливаю..."
        print(message)
        log_message(message)
        os.makedirs(target_dir, exist_ok=True)
        try:
            source_exe = get_resource_path("target.exe")
            if not os.path.exists(source_exe):
                message = "Встроенный target.exe не найден"
                print(message)
                log_message(message)
                return False
            shutil.copy2(source_exe, target_exe_path)
            message = f"target.exe восстановлен в {target_exe_path}"
            print(message)
            log_message(message)
        except Exception as e:
            message = f"Ошибка при восстановлении target.exe: {str(e)}"
            print(message)
            log_message(message)
            return False

    # Проверяем запись автозагрузки
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_READ
        )
        value, _ = winreg.QueryValueEx(key, "MyCorporateApp")
        winreg.CloseKey(key)
        if value != f'"{target_exe_path}"':
            message = "Запись автозагрузки для target.exe некорректна, восстанавливаю..."
            print(message)
            log_message(message)
            add_to_startup(target_exe_path)
    except FileNotFoundError:
        message = "Запись автозагрузки для target.exe отсутствует, восстанавливаю..."
        print(message)
        log_message(message)
        add_to_startup(target_exe_path)
    except Exception as e:
        message = f"Ошибка при проверке автозагрузки: {str(e)}"
        print(message)
        log_message(message)
        return False

    # Проверяем состояние автозагрузки
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        )
        value, _ = winreg.QueryValueEx(key, "MyCorporateApp")
        # Значение 2 в первом байте означает, что автозагрузка отключена
        if value[0] != 2:
            message = "Автозагрузка target.exe отключена, включаю..."
            print(message)
            log_message(message)
            # Устанавливаем 12-байтное значение для включённой автозагрузки
            enabled_value = b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            winreg.SetValueEx(key, "MyCorporateApp", 0, winreg.REG_BINARY, enabled_value)
            message = "Автозагрузка target.exe включена"
            print(message)
            log_message(message)
        winreg.CloseKey(key)
    except FileNotFoundError:
        message = "Состояние автозагрузки для MyCorporateApp не найдено, создаю включённое состояние..."
        print(message)
        log_message(message)
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run",
                0,
                winreg.KEY_WRITE
            )
            enabled_value = b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            winreg.SetValueEx(key, "MyCorporateApp", 0, winreg.REG_BINARY, enabled_value)
            winreg.CloseKey(key)
            message = "Состояние автозагрузки для target.exe включено"
            print(message)
            log_message(message)
        except Exception as e:
            message = f"Ошибка при создании состояния автозагрузки: {str(e)}"
            print(message)
            log_message(message)
            return False
    except Exception as e:
        message = f"Ошибка при проверке состояния автозагрузки: {str(e)}"
        print(message)
        log_message(message)
        return False

    return True

def add_to_startup(exe_path):
    """Добавляет target.exe в автозагрузку"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, "MyCorporateApp", 0, winreg.REG_SZ, f'"{exe_path}"')
        winreg.CloseKey(key)
        message = "target.exe добавлен в автозагрузку"
        print(message)
        log_message(message)
    except Exception as e:
        message = f"Ошибка при добавлении в автозагрузку: {str(e)}"
        print(message)
        log_message(message)

if __name__ == "__main__":
    # Скрываем консольное окно при запуске .exe
    if hasattr(sys, 'frozen'):
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # Периодическая проверка (каждые 60 секунд)
    while True:
        check_and_restore_target()
        time.sleep(1)  # Интервал проверки (в секундах)
