import keyboard
import pyperclip
import time
import re
import threading

saved_text = ""

def monitor_clipboard():
    global saved_text
    recent_value = ""
    while True:
        try:
            tmp_value = pyperclip.paste()
            if tmp_value and tmp_value != recent_value:
                saved_text = tmp_value
                recent_value = tmp_value
        except Exception as e:
            print(f"Ошибка чтения буфера обмена: {e}")
        time.sleep(0.5)
        
def paste_saved_clipboard():
    global saved_text
    text = saved_text

    if text:
        text = re.sub(r'[^\S\n]+', ' ', text)
        text = re.sub(r'\n+', '\n', text)
        for char in text:
            if char == '\n':
                keyboard.write('\n')
            else:
                keyboard.write(char)
            time.sleep(0.1)

threading.Thread(target=monitor_clipboard, daemon=True).start()
keyboard.add_hotkey('pause', paste_saved_clipboard)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Программа завершена.")