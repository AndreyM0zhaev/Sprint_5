from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

class TestLogoutAccount:
    def test_logout_account(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()

        logout_button = WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.PERS_ACC_LOGOUT_BUTTON))
        logout_button.click()

        WebDriverWait(login, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'