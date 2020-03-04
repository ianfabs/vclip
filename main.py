import clipboard
import atomic_store
from pynput import keyboard

clip_store = atomic_store.open('clipboards.json', default=dict())

def on_activate_paste(): print('pasted')
def on_activate_copy():
    clip_store.value["main"] = clip_store.value["main"] + [clipboard.paste()]

def for_canonical(f):
    return lambda k: f(l.canonical(k))

paste_hk = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+v'), on_activate_paste)
copy_hk = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), on_activate_copy)

with keyboard.Listener(
        on_press=for_canonical(paste_hk.press),
        on_release=for_canonical(paste_hk.release)
    ) as l:
        l.join()