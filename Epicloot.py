import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

bonus = 0
element = 0

##Opt
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--mute-audio')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-infobars')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--no-sandbox')
options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-breakpad')

##Func
def get1():
    global bonus
    global options
    global element
    wd.refresh()
    f_element()
    time.sleep(3.5)
    element.click()
    bonus = bonus + 1
    print ('Бонус забран! (' + (str(bonus)) + ' шт)')
    time.sleep(3605)
    starting()

t1 = threading.Thread(target=get1)

def f_element():
    global options
    global element
    time.sleep(3)
    element = wd.find_element(By.CLASS_NAME, 'game-gift__take')

def starting():
    time.sleep(1)
    t1.start()

##Start
print ('Epicloot-event-claimer')
print ('')
wd = webdriver.Chrome(options=options)
wd.get('http://epicloot.in')
time.sleep(0.25)
st = input('Пожалуйста авторизируйтесь в аккаунт и перейдите на страницу event, затем нажмите enter: ')
time.sleep(0.25)
start = input('Старт (y/n)?: ')
if start == 'y':
    starting()
elif start == 'n':
    exit()