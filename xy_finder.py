import pyautogui
import time

print("")
print("╔" + "═" * 50 + "╗")
print("║       XY COORDINATE FINDER                       ║")
print("║       Move mouse to see live coordinates         ║")
print("╠" + "═" * 50 + "╣")
print("║  Press Ctrl+C to stop                            ║")
print("╚" + "═" * 50 + "╝")
print("")

try:
    while True:
        x, y = pyautogui.position()
        print(f"  X: {x:5d}  |  Y: {y:5d}    ", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("")
    print("")
    print("  ✅ Stopped!")
    print("")