from telegram.ext import Application, CommandHandler, filters
import psutil
import pyautogui
import platform
import subprocess
import os
from datetime import datetime
import asyncio
import keyboard  # Для ввода текста, включая кириллицу

# Telegram bot token from BotFather
BOT_TOKEN = '7718878563:AAErJPMGi9bv6d9K4S2lrQVkK9bIFfuk9sQ'
# Optional: Chat ID for sending start/stop messages (uncomment if needed)
# CHAT_ID = YOUR_CHAT_ID_HERE  # Replace with your chat ID (integer)

# Configure pyautogui
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort
pyautogui.PAUSE = 0.1  # Small delay between actions for safety

# Start command
async def start(update, context):
    await update.message.reply_text("Hiii, cutie! Welcome to the super-duper kawaii Remote Admin Bot, nyaaa! :3\n"
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
                                   "/keycombo <key1>+<key2> - Press a key combo, like ctrl+c, nyaaa! ^_^")

# System info command
async def sysinfo(update, context):
    sys_info = (
        f"OS: {platform.system()} {platform.release()}, nyaaa :3\n"
        f"CPU: {platform.processor()}, w-w ^_^\n"
        f"CPU Usage: {psutil.cpu_percent()}%, p-pwetty busy! ~✿\n"
        f"Memory: {psutil.virtual_memory().percent}% used "
        f"({psutil.virtual_memory().used / (1024**3):.2f} GB / "
        f"{psutil.virtual_memory().total / (1024**3):.2f} GB), nyaaa (*^ω^)"
    )
    await update.message.reply_text(f"Here’s your system info, cutie! {sys_info} :3")

# Screenshot command
async def screenshot(update, context):
    try:
        screenshot = pyautogui.screenshot()
        screenshot_path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(screenshot_path)
        with open(screenshot_path, 'rb') as photo:
            await update.message.reply_photo(photo=photo)
        os.remove(screenshot_path)
        await update.message.reply_text("Screenshot taken and sent, nyaaa! P-pwetty pic! ~✿")
    except Exception as e:
        await update.message.reply_text(f"Sowwy, something went wrong with the screenshot, w-w: {str(e)} >w<")

# Run shell command
async def run(update, context):
    try:
        command = ' '.join(context.args)
        if not command:
            await update.message.reply_text("Pweeease give me a command to run, nyaaa! Like /run dir :3")
            return
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout or result.stderr or "No output, nyaaa!"
        await update.message.reply_text(f"Here’s what I got, cutie:\n{output[:1000]} ^_^")
    except Exception as e:
        await update.message.reply_text(f"Oopsie, something broke when running the command, w-w: {str(e)} (*≧ω≦)")

# Mouse click command
async def click(update, context):
    try:
        pyautogui.click()
        await update.message.reply_text("Clicky-click done, nyaaa! *boop* :3")
    except Exception as e:
        await update.message.reply_text(f"Sowwy, couldn’t do the clicky, w-w: {str(e)} >w<")

# Mouse right-click command
async def rightclick(update, context):
    try:
        pyautogui.rightClick()
        await update.message.reply_text("Right-clicky done, nyaaa! *tap* ~☆")
    except Exception as e:
        await update.message.reply_text(f"Oopsie, right-clicky failed, w-w: {str(e)} ^.^*")

# Mouse double-click command
async def doubleclick(update, context):
    try:
        pyautogui.doubleClick()
        await update.message.reply_text("Double-clicky done super fast, nyaaa! *double boop* ^_^")
    except Exception as e:
        await update.message.reply_text(f"Sowwy, double-clicky didn’t work, w-w: {str(e)} :3")

# Mouse move command
async def mousemove(update, context):
    try:
        if len(context.args) != 2:
            await update.message.reply_text("Pweeease give me x and y coordinates, nyaaa! Like /mousemove 100 200 (*^ω^)")
            return
        x, y = map(int, context.args)
        screen_width, screen_height = pyautogui.size()
        if x < 0 or y < 0 or x > screen_width or y > screen_height:
            await update.message.reply_text(f"Coordinates are too big or small, nyaaa! Screen size: {screen_width}x{screen_height} >w<")
            return
        pyautogui.moveTo(x, y)
        await update.message.reply_text(f"Mousey moved to ({x}, {y}), nyaaa! *scurry scurry* ~✿")
    except ValueError:
        await update.message.reply_text("Pweeease use numbers for coordinates, nyaaa! Like /mousemove 100 200 :3")
    except Exception as e:
        await update.message.reply_text(f"Oopsie, couldn’t move mousey, w-w: {str(e)} ^.^*")

# Type text command
async def type_text(update, context):
    try:
        text = ' '.join(context.args)
        if not text:
            await update.message.reply_text("Pweeease give me some text to type, nyaaa! Like /type Привет, мир! (*≧ω≦)")
            return
        text = text.encode().decode('utf-8')  # Ensure UTF-8 for Cyrillic
        keyboard.write(text)  # Use keyboard module for Unicode support
        await update.message.reply_text(f"Typed your text, cutie: {text} *tap tap tap* :3")
    except Exception as e:
        await update.message.reply_text(f"Sowwy, couldn’t type the text, w-w: {str(e)} >w<")

# Press single key command
async def key(update, context):
    try:
        if not context.args:
            await update.message.reply_text("Pweeease tell me a key to press, nyaaa! Like /key enter ^_^")
            return
        key = context.args[0].lower()
        if key not in pyautogui.KEY_NAMES:
            await update.message.reply_text(f"That’s not a valid key, nyaaa! Try these: {', '.join(pyautogui.KEY_NAMES[:10])}... (*^ω^)")
            return
        pyautogui.press(key)
        await update.message.reply_text(f"Pressed the key, nyaaa: {key} *boop boop* ~✿")
    except Exception as e:
        await update.message.reply_text(f"Oopsie, couldn’t press the key, w-w: {str(e)} :3")

# Key combination command
async def keycombo(update, context):
    try:
        if not context.args or '+' not in context.args[0]:
            await update.message.reply_text("Pweeease give me a key combo, nyaaa! Like /keycombo ctrl+c >w<")
            return
        keys = context.args[0].lower().split('+')
        if not all(key in pyautogui.KEY_NAMES for key in keys):
            await update.message.reply_text(f"Those keys aren’t valid, nyaaa! Try these: {', '.join(pyautogui.KEY_NAMES[:10])}... ^.^*")
            return
        pyautogui.hotkey(*keys)
        await update.message.reply_text(f"Pressed the combo, nyaaa: {context.args[0]} *smashy smash* :3")
    except Exception as e:
        await update.message.reply_text(f"Sowwy, couldn’t press the combo, w-w: {str(e)} (*≧ω≦)")

# Main function to set up and run the bot
async def main():
    # Initialize the application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sysinfo", sysinfo))
    application.add_handler(CommandHandler("screenshot", screenshot))
    application.add_handler(CommandHandler("run", run))
    application.add_handler(CommandHandler("click", click))
    application.add_handler(CommandHandler("rightclick", rightclick))
    application.add_handler(CommandHandler("doubleclick", doubleclick))
    application.add_handler(CommandHandler("mousemove", mousemove))
    application.add_handler(CommandHandler("type", type_text))
    application.add_handler(CommandHandler("key", key))
    application.add_handler(CommandHandler("keycombo", keycombo))

    # Start the bot with polling
    print("Starting the kawaii bot, nyaaa! ^_^")  # Логирование в консоль
    # Optional: Send start message to Telegram (uncomment and set CHAT_ID if needed)
    # await application.bot.send_message(chat_id=CHAT_ID, text="Starting the kawaii bot, nyaaa! ^_^")
    await application.initialize()
    await application.start()
    await application.updater.start_polling(drop_pending_updates=True)

    # Keep the bot running until stopped
    try:
        while True:
            await asyncio.sleep(3600)  # Sleep to keep the loop alive
    except KeyboardInterrupt:
        print("Shutting down the bot, nyaaa! :3")  # Логирование в консоль
        # Optional: Send stop message to Telegram (uncomment and set CHAT_ID if needed)
        # await application.bot.send_message(chat_id=CHAT_ID, text="Shutting down the bot, nyaaa! :3")
        await application.updater.stop()
        await application.stop()
        await application.shutdown()

if __name__ == '__main__':
    # Use the existing event loop or create a new one
    try:
        loop = asyncio.get_running_loop()
        asyncio.ensure_future(main())
    except RuntimeError:  # No running loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())