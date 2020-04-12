import pyautogui
from PIL import ImageGrab


while True:

    tela = ImageGrab.grab() # Pega um print da tela

    # É provável que os valores range de X e Y devam ser alterados manualmente 
    for x in range(300, 430):
        for y in range(460, 461):

            area = tela.getpixel((x, y)) # Pega a cor do pixel (x,y)

            if area[0] == 172:
                pyautogui.press('up') # Pula
                break

        if area[0] == 172: break
