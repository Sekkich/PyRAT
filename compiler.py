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
        # Возвращаем путь к скомпилированному target.exe
        dist_dir = os.path.join(os.path.dirname(target_path), "dist")
        return os.path.join(dist_dir, "target.exe")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при компиляции target.py: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        sys.exit(1)

def compile_deployer(target_exe_path):
    """Компилирует deployer.py в deployer.exe, включая target.exe как ресурс"""
    deployer_path = find_file("deployer.py", os.getcwd())
    if not deployer_path:
        print("Ошибка: deployer.py не найден в текущей директории")
        sys.exit(1)

    # Копируем target.exe во временную папку для включения в PyInstaller
    temp_dir = os.path.join(os.path.dirname(deployer_path), "temp")
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
        # Очищаем временную папку
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

    # Компилируем deployer.py в deployer.exe, включая target.exe
    compile_deployer(target_exe_path)

    print("Компиляция завершена. Файлы deployer.exe и target.exe находятся в папке dist")