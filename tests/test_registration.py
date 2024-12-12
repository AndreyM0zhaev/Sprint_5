from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators
from constants import Constants

faker = Faker()

class TestRegistrationStellarburgers:

    def test_registration_success(self, driver):
        email = faker.email()
        name = faker.name()
        password = faker.password()

        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.AUTH_BUTTON).click()

        recovery_link = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Locators.RECOVERY_LINK))

        assert recovery_link.is_displayed(), "Зарегистрироваться"
        assert driver.current_url == Constants.LOGIN_URL


    def test_registration_field_name_not_empty(self, driver):
        email = faker.email()

        password = faker.password()

        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert driver.current_url == Constants.REGISTER_URL


    def test_registration_invalid_email(self, driver):
        email = 'email@email'
        name = faker.name()
        password = faker.password()

        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert driver.current_url == Constants.REGISTER_URL


    def test_registration_with_short_password(self, driver):
        email = faker.email()
        name = faker.name()
        password = '12345'

        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.ALERT_INVALID_PASS)
        assert driver.current_url == Constants.REGISTER_URL




