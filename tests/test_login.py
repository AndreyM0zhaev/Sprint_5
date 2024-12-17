from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Constants
from locators import Locators

class TestLoginStellarburgers:
    def test_login_on_main_page(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        WebDriverWait(login, 5).until(EC.url_to_be(Constants.PROFILE_URL))
        assert login.current_url == Constants.PROFILE_URL


    def test_login_registration_link(self, login):
        login.find_element(*Locators.REG_LINK).click()
        login.find_element(*Locators.AUTH_LINK).click()

        login.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        login.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        login.find_element(*Locators.AUTH_BUTTON).click()

        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        logout = WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.PERS_ACC_LOGOUT_BUTTON))
        assert logout.is_displayed()
        assert login.current_url == Constants.PROFILE_URL


    def test_login_recovery_link(self, login):

        login.find_element(*Locators.RECOVERY_LINK).click()
        login.find_element(*Locators.AUTH_LINK).click()

        login.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        login.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        login.find_element(*Locators.AUTH_BUTTON).click()

        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        logout = WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.PERS_ACC_LOGOUT_BUTTON))
        assert logout.is_displayed()
        assert login.current_url == Constants.PROFILE_URL



    def test_login_personal_account(self, login):
        login.find_element(*Locators.LOGO_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()

        login.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        login.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        login.find_element(*Locators.AUTH_BUTTON).click()

        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        logout = WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.PERS_ACC_LOGOUT_BUTTON))
        assert logout.is_displayed()
        assert login.current_url == Constants.PROFILE_URL

