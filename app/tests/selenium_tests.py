import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ROOT_URL = 'http://127.0.0.1:5000'

USERNAME = 'usuario_teste'
PASS = '123456'

driver = webdriver.Chrome()

def test_login():
    driver.get(ROOT_URL + '/login')

    username_field = driver.find_element(by=By.ID, value='username')
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(by=By.ID, value='password')
    password_field.send_keys(PASS)

    # submit the form
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

    assert f'Logged in as: {USERNAME}' in driver.page_source

test_login()

driver.quit()