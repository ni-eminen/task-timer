import time
import os
from pynput import keyboard
cmd = input('Topic: ')
minutes = float(input('Timer (minutes): '))
global coffee_count
global history

coffee_count = 0
increment = .1
principles = [

]

def timer():
    global coffee_count
    elapsed = 0
    while minutes - (elapsed / 60) > 0:
        time.sleep(increment)
        elapsed += increment
        os.system('clear')
        print(f'Topic: {cmd}')
        print(f'Elapsed time: {max(minutes - 1 - int(elapsed // 60), 0)} min,'
                                f' {round(60 - (elapsed % 60), 2) if round(elapsed % 60) != 0 else 0} sec')
        print(f'coffees today: {coffee_count}')
        print()
        for x in principles:
            print(x)

def on_press(key):
    global coffee_count
    try:
        if key.char == 'c':
            coffee_count += 1
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:

        pass

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

timer()