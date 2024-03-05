import time
import os
import requests
import time
from pynput import keyboard
from principles import principles, goals


global timer_on
timer_on = False
cmd = input('Topic: ')
minutes = float(input('Timer (minutes): '))
api_url = "http://localhost:8000"
coffee_count = 0
increment = .1

def dict_print(d: dict, label: str):
    print()
    print(label)
    print()
    cols = d.keys()
    for col in cols:
        print(f'\t{col}:')
        for x in d[col]:
            print(f'\t\t{x}')


def timer():
    global timer_on

    time.time()
    try:
        response = requests.post(f'{api_url}/timestamps', json={"topic": cmd, "start": True, "timestamp": time.time()})
        print('response from server:', response.json())
    except:
        pass
    timer_on = True
    elapsed = 0
    while minutes - (elapsed / 60) > 0 and timer_on:
        time.sleep(increment)
        if not timer_on:
            break
        elapsed += increment
        os.system('clear')
        print(f'Topic: {cmd}')
        print(f'Elapsed time: {max(minutes - 1 - int(elapsed // 60), 0)} min,'
              f' {round(60 - (elapsed % 60), 2) if round(elapsed % 60) != 0 else 0} sec')
        print()

        print("principles")
        for x in principles:
            print(f'\t{x}')
        dict_print(goals, "goals")
    try:
        response = requests.post(f'{api_url}/timestamps', json={"topic": cmd, "start": False, "timestamp": time.time()})
        print('response from server:', response.json())
    except:
        pass

def on_press(key):
    global timer_on
    try:
        if key.char == 'å':
            timer_on = False

    except AttributeError:

        pass

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

timer()
