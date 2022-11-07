# Chistopher Miller
# AFK BOT that moves your mouse every 2 seconds


import pyautogui as pag
import random
import time

while True:
	x = random.randint(800,700)
	x = random.randint(200,600)
	pag.moveTo(x,y,0.5)
	time.sleep(2)