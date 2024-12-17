from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants

class TestIntoPersonalAccount:
    def test_into_personal_account(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()

        WebDriverWait(login, 5).until(EC.url_to_be(Constants.PROFILE_URL))
        assert login.current_url == Constants.PROFILE_URL