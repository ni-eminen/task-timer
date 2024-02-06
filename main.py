import time
import os
from pynput import keyboard
cmd = input('Topic: ')
global coffee_count
coffee_count = 0

def timer():
    global coffee_count
    elapsed = 0
    while(True):
        time.sleep(0.1)
        elapsed += .1
        os.system('clear')
        print(f'Topic: {cmd}')
        print(f'Elapsed time: {int(elapsed // 60)} min, {round(elapsed % 60, 2)} sec')
        print(f'coffees today: {coffee_count}')

def on_press(key):
        try:
            if key.char == 'c':
                global coffee_count
                coffee_count += 1
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            # Special key
            pass

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

timer()