from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestIntoPersonalAccount:
    def test_into_personal_account(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()

        WebDriverWait(login, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'