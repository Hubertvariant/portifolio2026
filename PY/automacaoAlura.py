import pyautogui as pg
from time import sleep

pg.press('win')
pg.write('alura')
pg.press('enter')
sleep(3)
pg.click(x=412, y=840)
sleep(2)