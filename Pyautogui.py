import pyautogui
import time
import pyperclip
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from celery import Celery
from celery.schedules import crontab


driver = webdriver.Edge(r'C:\Selenium\msedgedriver.exe')

driver.get('https://google.com')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Dólar')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = float(driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))

driver.get('https://google.com')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Euro')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = float(driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))

driver.get('https://moraislucas.github.io/MeMotive/')
mensagem = driver.find_element_by_tag_name('p').text

driver.quit()

pyautogui.PAUSE = 1
print(pyautogui.position())
pyautogui.click(652, 1066)
pyautogui.click(296, 107)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("Rafael Reis")
pyautogui.click(280, 261)
escrita = f"""
Boa tarde!
A cotação do dólar hoje é de R$ {dolar:.2f}
A cotação do euro hoje é de R$ {euro:.2f}

_{mensagem}_
"""
pyperclip.copy(escrita)
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "v")
# pyautogui.press("enter")
