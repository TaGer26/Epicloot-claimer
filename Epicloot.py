import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By

bonus = 0
element = 0

##Func
def get1():
    global bonus
    global element
    wd.refresh()
    f_element()
    time.sleep(8)
    element.click()
    bonus = bonus + 1
    print ('Бонус забран! (' + (str(bonus)) + ' шт)')
    time.sleep(3605)

t1 = threading.Thread(target=get1)

def f_element():
    global element
    time.sleep(7)
    element = wd.find_element(By.CLASS_NAME, 'game-gift__take')

##Start
print ('Epicloot-event-claimer')
print ('')
wd = webdriver.Chrome()
wd.get('http://epicloot.in')
time.sleep(0.25)
st = input('Пожалуйста авторизируйтесь в аккаунт и перейдите на страницу event, затем нажмите enter: ')
time.sleep(0.25)
start = input('Старт (y/n)?: ')
if start == 'y':
    t1.start()
elif start == 'n':
    exit()