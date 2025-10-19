import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

load_dotenv()

base_url = os.getenv("BASE_URL")


def test_user_registration():
    driver = webdriver.Chrome()
    driver.get(base_url)

    unique = str(int(time.time())) + str(random.randint(100, 999))
    first_name = "Ivan"
    last_name = "Petrov"
    email = f'test{unique}{unique}@mail.ru'
    phone_number = "+79993338811"
    password = "random_pass"

    driver.find_element(By.ID, "input-firstname").send_keys(first_name)
    driver.find_element(By.ID, "input-lastname").send_keys(last_name)
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-telephone").send_keys(phone_number)
    driver.find_element(By.ID, "input-password").send_keys(password)
    driver.find_element(By.ID, "input-confirm").send_keys(password)
    driver.find_element(By.ID, "input-agree")

    checkbox = driver.find_element(By.ID, "input-agree")
    driver.execute_script("arguments[0].click();", checkbox)

    driver.find_element(By.CSS_SELECTOR, '[value="Continue"]').click()

    time.sleep(1)
    assert driver.find_element(By.ID, "content")
    assert driver.find_element(
        By.XPATH, '//*[text() = " Your Account Has Been Created!"]'
    )

    driver.quit()