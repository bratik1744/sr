from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
from random import randint
from time import sleep
import undetected_chromedriver.v2 as uc
import numpy as np
import undetected_chromedriver.v2 as uc
def f(url, start, stop, step):

    login_input = "stukundaniil@gmail.com"
    password_input = "B#WZ5*j0-rbom5"

    driver = uc.Chrome()
    driver.get(url)
    sleep(2)
    login = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[1]/input')
    password = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[2]/input')
    submit = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/button')

    login.send_keys(login_input)
    password.send_keys(password_input)
    submit.click()

    driver.get(url)

    answer_input = driver.find_elements(By.CLASS_NAME,"multiply_answers__input")
    answer_submit = driver.find_elements(By.CLASS_NAME, 'task_buttons__message_form_submit')


    for x in np.arange(start, stop, step):
        x = round(x,1)
        try:
            answer_input[0].clear()
            answer_input[0].send_keys(x)
            sleep(2)
            answer_submit[0].click()
            sleep(1)
        except Exception as e:
            print('Done!',e)





