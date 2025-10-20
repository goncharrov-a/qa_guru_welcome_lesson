import os
import random
import time
from os import register_at_fork

import pytest
from dotenv import load_dotenv
from selenium import webdriver

from registration_page import RegistrationPage
from registration_page import User

load_dotenv()

base_url = os.getenv("BASE_URL")


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture
def unique_user():
    unique_data = str(int(time.time())) + str(random.randint(100, 999))
    user: User = User(unique_data)
    yield user


@pytest.fixture
def registration_page(driver_chrome):
    yield RegistrationPage(driver_chrome)


def test_user_registration_pom(registration_page, unique_user):
    registration_page.check_form_is_visible()
    registration_page.fill_registration_form(unique_user)
    registration_page.check_form_is_not_visible()
    registration_page.check_that_success_form_is_visible()


def test_blank_form_warnings(registration_page):
    registration_page.check_form_is_visible()
    registration_page.click_continue_button()
