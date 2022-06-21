from selenium import webdriver
import time


import random
driver = webdriver.Chrome('./chromedriver')

cursor = driver

driver.get('https://www.youtube.com/')
time.sleep(random.randint(3,6)/1.714775)

# Abre uma nova aba
cursor.execute_script("window.open('');") 

time.sleep(random.randint(2,7)/1.714775)
cursor.switch_to.window(cursor.window_handles[0])

time.sleep(random.randint(2,7)/1.714775)
# Fecha a aba
cursor.close()
time.sleep(1)
cursor.switch_to.window(cursor.window_handles[0])
time.sleep(1)
cursor.get('https://www.youtube.com/')
