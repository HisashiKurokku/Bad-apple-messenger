#Contributed by joneching

import json
from time import sleep

import pyautogui
import pyperclip

with open('output.json', 'r', encoding="utf-8") as data_file:
    json_data = data_file.read()

frames = json.loads(json_data)

sleep(5)  

for frame in frames:
    pyperclip.copy(frame)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(1/10)
