import pyautogui
import time
import threading
import keyboard
import os


def alterar(): #alterar entre as abas do navegador
    while True:
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'tab')


def encerrar(): #encerrar o processo
    while True:
        if keyboard.is_pressed('p'):
            os._exit(0)


threading.Thread(target=alterar).start() #rodar duas funções ao mesmo tempo
threading.Thread(target=encerrar).start()