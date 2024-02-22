import time
import os
import requests
import time
from pynput import keyboard

global coffee_count
global history
global timer_on

timer_on = False
cmd = input('Topic: ')
minutes = float(input('Timer (minutes): '))
api_url = "http://localhost:8000"
coffee_count = 0
increment = .1
principles = [

]

def timer():
    global timer_on
    global coffee_count
    time.time()
    response = requests.post(f'{api_url}/timestamps', json={"topic": cmd, "start": True, "timestamp": time.time()})
    print('response from server:', response.json())
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
        print(f'coffees today: {coffee_count}')
        print()
        for x in principles:
            print(x)

    response = requests.post(f'{api_url}/timestamps', json={"topic": cmd, "start": False, "timestamp": time.time()})
    print('response from server:', response.json())


def on_press(key):
    global coffee_count
    global timer_on
    global history
    history.append(key.char)
    print(history[-4:])
    try:
        if ''.join(history[-4:]) == '1cof':
            coffee_count += 1
        if key.char == 'å':
            print()
            timer_on = False

    except AttributeError:

        pass

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

timer()