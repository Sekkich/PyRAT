import tkinter as tk
from tkinter import messagebox
import os
import re

class ModifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Variable Modifier and Compiler")
        self.root.geometry("400x200")

        # Поле для имени переменной с значением по умолчанию
        tk.Label(root, text="Variable Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.var_name_entry = tk.Entry(root, width=30)
        self.var_name_entry.insert(0, "_W2Z8T3K9V5P1_TOKEN")  # Значение по умолчанию
        self.var_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Поле для значения переменной с значением по умолчанию
        tk.Label(root, text="New Value:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.var_value_entry = tk.Entry(root, width=30)
        self.var_value_entry.insert(0, "bpvtyzkcz")  # Значение по умолчанию
        self.var_value_entry.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка для изменения переменной
        self.modify_button = tk.Button(root, text="Modify Variable", command=self.modify_variable)
        self.modify_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Кнопка для компиляции в .exe
        self.compile_button = tk.Button(root, text="Compile to EXE", command=self.compile_script)
        self.compile_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Целевой скрипт
        self.target_script = "target.py"
        self.target_script2 = "compiler.py"

    def modify_variable(self):
        variable_name = self.var_name_entry.get().strip()
        new_value = self.var_value_entry.get().strip()

        if not variable_name or not new_value:
            messagebox.showerror("Error", "Please fill both fields")
            return

        try:
            # Читаем содержимое файла
            with open(self.target_script, 'r', encoding='utf-8') as file:
                content = file.read()

            # Ищем и заменяем значение переменной
            pattern = rf'({variable_name}\s*=\s*)(.*?)(?=\n|$)'
            new_content = re.sub(pattern, f'\g<1>{repr(new_value)}', content)

            # Записываем обновленное содержимое
            with open(self.target_script, 'w', encoding='utf-8') as file:
                file.write(new_content)

            messagebox.showinfo("Success", f"Variable {variable_name} changed to {new_value}")

        except FileNotFoundError:
            messagebox.showerror("Error", f"File {self.target_script} not found")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def compile_script(self):
        try:
            # Компилируем target.py в .exe
            os.system(f'python {self.target_script2}')
            result=0
            if result == 0:
                messagebox.showinfo("Success", f"Script {self.target_script} compiled to .exe")
            else:
                messagebox.showerror("Error", "Compilation failed. Ensure PyInstaller is installed.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during compilation: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModifierApp(root)
    root.mainloop()
