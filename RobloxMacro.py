import keyboard, time

#

time.sleep(10)
running = True
while running:
    if keyboard.is_pressed("f7"):
        running = False
        break
    keyboard.press("d")
    time.sleep(1.25)
    keyboard.release("d")
    time.sleep(0.5)
    keyboard.press("e")
    time.sleep(4)
    keyboard.release("e")
    for i in range(4):
        keyboard.press("d")
        time.sleep(1.75)
        keyboard.release("d")
        time.sleep(0.5)
        keyboard.press("e")
        time.sleep(4)
        keyboard.release("e")
    keyboard.press("s")
    time.sleep(12.75)
    keyboard.release("s")
    for i in range(10):
        if keyboard.is_pressed("f7"):
            running = False
            break
        time.sleep(30)