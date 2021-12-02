# Imtiaz Adar
# Phone : +8801778767775
# Email : imtiaz-adar@hotmail.com
# Project : Automated Messenger
# Language used : Python

import pyautogui as adar
from time import sleep
how = int(input('Enter how many times you want to send message : '))
for i in range(how):
    adar.typewrite('Hi ! how are you? what are you doing? I wanna talk to you')
    adar.press('enter')
    sleep(2)