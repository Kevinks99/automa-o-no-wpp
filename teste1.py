import pyautogui
import pyperclip
import time 
pyautogui.PAUSE=2
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

#entrar no whatsapp
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')

time.sleep(10)
#clicar no contato
pyautogui.moveTo(x=360, y=469)
pyautogui.click(x=360, y=469)

#escrever mensagem
texto = 'Mensagem de teste, não leve em concideração'
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

#enviar a mensagem
pyautogui.press('enter')
