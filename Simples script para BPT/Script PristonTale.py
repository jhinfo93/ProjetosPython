import pyautogui
from PIL import ImageGrab
import keyboard
import time

hp = (246, 138, 83)
mana = (6, 133, 250)
res = (14, 144, 11)
fechar = (43, 43, 43)
global t
t= 0.1
global cont
cont = 0

def capture_screen():
    image = ImageGrab.grab()
    return image

def detectar_hp():
    imagem = capture_screen()
    color = imagem.getpixel((608,681))
    print(color)
    if(hp != color):
        print('Usar HP')
        return True
    return False

def detectar_res():
    imagem = capture_screen()
    color = imagem.getpixel((591,709))
    #print(color)
    if(res != color):
        print('Usar Res')
        return True
    return False

def finalizar():
    imagem = capture_screen()
    color = imagem.getpixel((710,174))
    #print(color)
    if(fechar == color):
        print('Finalizar')
        exit()

def midranda():
    keyboard.press('f5')
    time.sleep(t)
    try:
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
    except:
        print("n foi")
    time.sleep(t)
    keyboard.release('f5')
    keyboard.press('f1')
    time.sleep(0.1)
    keyboard.release('f1')

def migal():
    keyboard.press('f3')
    time.sleep(t)
    try:
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
    except:
        print("n foi")
    time.sleep(t)
    keyboard.release('f3')
    keyboard.press('f1')
    time.sleep(0.1)
    keyboard.release('f1')

def chuva():
    keyboard.press('f4')
    time.sleep(t)
    try:
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
    except:
        print("n foi")
    time.sleep(t)
    keyboard.release('f4')
    keyboard.press('f1')
    time.sleep(0.1)
    keyboard.release('f1')



def on_click():

    keyboard.press("shift")
    time.sleep(t)
    try:
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
        pyautogui.rightClick((639, 435))
    except:
        print("n foi")
    keyboard.release("shift")


def usarHp():
    keyboard.press('1')
    time.sleep(0.05)
    keyboard.release('1')
    time.sleep(0.05)
    pyautogui.moveTo(317, 540)
    keyboard.press('shift')
    time.sleep(0.05)
    keyboard.press('1')
    time.sleep(0.05)
    keyboard.release('1')
    time.sleep(0.05)
    keyboard.release('shift')
    time.sleep(0.05)


def usarRes():
    keyboard.press('3')
    time.sleep(0.05)
    keyboard.release('3')
    time.sleep(0.05)
    time.sleep(0.05)
    pyautogui.moveTo(317, 570)
    keyboard.press('shift')
    time.sleep(0.05)
    keyboard.press('3')
    time.sleep(0.05)
    keyboard.release('3')
    time.sleep(0.05)
    keyboard.release('shift')
    time.sleep(0.05)

keyboard.press("left")



while(True):
    finalizar()
    on_click()
    migal()
    if(detectar_hp()):
        try:
            usarHp()
        except:
            print("error")
    if (detectar_res()):
        try:
            usarRes()
        except:
            print("error")

    on_click()
    midranda()
    finalizar()
    if(detectar_hp()):
        try:
            usarHp()
        except:
            print("error")
    if (detectar_res()):
        try:
            usarRes()
        except:
            print("error")
    on_click()
    chuva()
    finalizar()
    if(detectar_hp()):
        try:
            usarHp()
        except:
            print("error")
    if (detectar_res()):
        try:
            usarRes()
        except:
            print("error")

    cont = cont + 1
    print(cont)
