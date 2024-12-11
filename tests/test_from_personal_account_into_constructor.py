from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestFromPersonalAccountIntoConstructor:

    def test_from_personal_account_into_constructor(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        burger_section = WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BURGER_SECTION))
        burger_section.is_displayed()

        assert login.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_from_constructor_into_logo(self, login):
        login.find_element(*Locators.AUTH_BUTTON).click()
        login.find_element(*Locators.PERS_ACC_INTO_BUTTON).click()
        login.find_element(*Locators.LOGO_BUTTON).click()

        burger_section = WebDriverWait(login, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BURGER_SECTION))
        burger_section.is_displayed()

        assert login.current_url == 'https://stellarburgers.nomoreparties.site/'