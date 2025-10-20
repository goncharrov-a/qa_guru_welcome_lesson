from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_element(self, selector):
        return self.wait.until(EC.presence_of_element_located(selector))

    def not_find_element(self, selector):
        return self.wait.until_not(EC.presence_of_element_located(selector))

    def click(self, selector, force=False):
        element = self.wait.until(EC.presence_of_element_located(selector))
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def fill(self, selector, value):
        element = self.find_element(selector)
        element.send_keys(value)


class User:
    def __init__(self, unique):
        self.first_name = "Ivan"
        self.last_name = "Petrov"
        self.email = f"test{unique}{unique}@mail.ru"
        self.phone_number = "+79993338811"
        self.password = "random_pass"


class RegistrationPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    POLICY_AGREEMENT = (By.ID, "input-agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[value="Continue"]')
    CONTENT = (By.ID, "content")
    TEXT_ASSERT = (By.XPATH, '//h1[text() = " Your Account Has Been Created!"]')

    def check_form_is_visible(self):
        assert self.find_element(self.FIRST_NAME)
        assert self.find_element(self.LAST_NAME)
        assert self.find_element(self.EMAIL)
        assert self.find_element(self.PHONE)
        assert self.find_element(self.PASSWORD)
        assert self.find_element(self.CONFIRM_PASSWORD)
        assert self.find_element(self.POLICY_AGREEMENT)
        assert self.find_element(self.CONTINUE_BUTTON)

    def check_form_is_not_visible(self):
        assert self.not_find_element(self.FIRST_NAME)
        assert self.not_find_element(self.LAST_NAME)
        assert self.not_find_element(self.EMAIL)
        assert self.not_find_element(self.PHONE)
        assert self.not_find_element(self.PASSWORD)
        assert self.not_find_element(self.CONFIRM_PASSWORD)
        assert self.not_find_element(self.POLICY_AGREEMENT)
        assert self.not_find_element(self.CONTINUE_BUTTON)

    def fill_registration_form(self, user: User):
        self.fill(self.FIRST_NAME, user.first_name)
        self.fill(self.LAST_NAME, user.last_name)
        self.fill(self.EMAIL, user.email)
        self.fill(self.PHONE, user.phone_number)
        self.fill(self.PASSWORD, user.password)
        self.fill(self.CONFIRM_PASSWORD, user.password)
        self.click(self.POLICY_AGREEMENT, force=True)
        self.click(self.CONTINUE_BUTTON)

    def check_that_success_form_is_visible(self):
        assert self.find_element(self.CONTENT)
        assert self.find_element(self.TEXT_ASSERT)
