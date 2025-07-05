import os
import subprocess
import sys
import shutil

def find_file(file_name, search_path):
    """Находит файл в указанной директории"""
    for root, _, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def compile_target():
    """Компилирует target.py в target.exe"""
    target_path = find_file("target.py", os.getcwd())
    if not target_path:
        print("Ошибка: target.py не найден в текущей директории")
        sys.exit(1)

    try:
        result = subprocess.run(
            ["pyinstaller", "--onefile", "--noconsole", target_path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"target.py успешно скомпилирован в target.exe")
        dist_dir = os.path.join(os.path.dirname(target_path), "dist")
        return os.path.join(dist_dir, "target.exe")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при компиляции target.py: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)

def compile_monitor(target_exe_path):
    """Компилирует monitor.py в monitor.exe, включая target.exe как ресурс"""
    monitor_path = find_file("monitor.py", os.getcwd())
    if not monitor_path:
        print("Ошибка: monitor.py не найден в текущей директории")
        sys.exit(1)

    temp_dir = os.path.join(os.path.dirname(monitor_path), "temp")
    os.makedirs(temp_dir, exist_ok=True)
    temp_target_exe = os.path.join(temp_dir, "target.exe")
    shutil.copy2(target_exe_path, temp_target_exe)

    try:
        result = subprocess.run(
            [
                "pyinstaller",
                "--onefile",
                "--noconsole",
                f"--add-data={temp_target_exe};.",
                monitor_path
            ],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"monitor.py успешно скомпилирован в monitor.exe")
        dist_dir = os.path.join(os.path.dirname(monitor_path), "dist")
        return os.path.join(dist_dir, "monitor.exe")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при компиляции monitor.py: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def confirm_exe(exe_path, exe_name):
    """Запрашивает подтверждение для использования .exe или его замены"""
    print(f"\nСкомпилированный {exe_name} находится по пути: {exe_path}")
    print(f"Проверьте {exe_name}. Готовы продолжить? (y/n)")
    response = input().strip().lower()

    if response == 'y':
        return exe_path
    elif response == 'n':
        print(f"Хотите заменить {exe_name} другим файлом? (y/n)")
        replace_response = input().strip().lower()
        if replace_response == 'y':
            print(f"Введите полный путь к новому {exe_name}:")
            new_exe_path = input().strip()
            if os.path.exists(new_exe_path) and new_exe_path.endswith('.exe'):
                return new_exe_path
            else:
                print(f"Ошибка: указанный файл не существует или не является .exe")
                sys.exit(1)
        else:
            print(f"Хотите перекомпилировать {exe_name.replace('.exe', '.py')} после редактирования? (y/n)")
            recompile_response = input().strip().lower()
            if recompile_response == 'y':
                print(f"Отредактируйте {exe_name.replace('.exe', '.py')} и сохраните изменения, затем продолжим.")
                input("Нажмите Enter после редактирования...")
                if exe_name == "target.exe":
                    return compile_target()
                elif exe_name == "monitor.exe":
                    # Для перекомпиляции monitor.exe нужен target.exe
                    target_path = find_file("target.exe", os.path.join(os.getcwd(), "dist"))
                    if not target_path:
                        print("Ошибка: target.exe не найден в папке dist")
                        print("Перекомпилируйте target.py сначала")
                        sys.exit(1)
                    return compile_monitor(target_path)
            else:
                print("Компиляция отменена пользователем")
                sys.exit(0)
    else:
        print("Некорректный ввод. Введите 'y' или 'n'.")
        return confirm_exe(exe_path, exe_name)

def compile_deployer(target_exe_path, monitor_exe_path):
    """Компилирует deployer.py в deployer.exe, включая target.exe и monitor.exe как ресурсы"""
    deployer_path = find_file("deployer.py", os.getcwd())
    if not deployer_path:
        print("Ошибка: deployer.py не найден в текущей директории")
        sys.exit(1)

    temp_dir = os.path.join(os.path.dirname(deployer_path), "temp")
    os.makedirs(temp_dir, exist_ok=True)
    temp_target_exe = os.path.join(temp_dir, "target.exe")
    temp_monitor_exe = os.path.join(temp_dir, "monitor.exe")
    shutil.copy2(target_exe_path, temp_target_exe)
    shutil.copy2(monitor_exe_path, temp_monitor_exe)

    try:
        result = subprocess.run(
            [
                "pyinstaller",
                "--onefile",
                "--noconsole",
                f"--add-data={temp_target_exe};.",
                f"--add-data={temp_monitor_exe};.",
                deployer_path
            ],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"deployer.py успешно скомпилирован в deployer.exe")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при компиляции deployer.py: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    # Проверяем, установлен ли PyInstaller
    try:
        subprocess.run(["pyinstaller", "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("Ошибка: PyInstaller не установлен. Установите его с помощью 'pip install pyinstaller'")
        sys.exit(1)

    # Компилируем target.py в target.exe
    target_exe_path = compile_target()

    # Запрашиваем подтверждение для target.exe
    confirmed_target_exe_path = confirm_exe(target_exe_path, "target.exe")

    # Компилируем monitor.py в monitor.exe, включая target.exe
    monitor_exe_path = compile_monitor(confirmed_target_exe_path)

    # Запрашиваем подтверждение для monitor.exe
    confirmed_monitor_exe_path = confirm_exe(monitor_exe_path, "monitor.exe")

    # Компилируем deployer.py в deployer.exe, включая target.exe и monitor.exe
    compile_deployer(confirmed_target_exe_path, confirmed_monitor_exe_path)

    print("Компиляция завершена. Файлы target.exe, monitor.exe и deployer.exe находятся в папке dist")