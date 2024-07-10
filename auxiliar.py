import pyautogui
import time

time.sleep(5) # vai esperar 5 segundos para dar tempo de eu colocar o mouse no lugar correto.
print(pyautogui.position()) # mostra a localização que seu mouse está.

pyautogui.scroll(200)