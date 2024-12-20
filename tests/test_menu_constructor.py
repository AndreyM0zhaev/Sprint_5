from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMenuConstructor:
    def test_menu_constructor_tab_filling(self, driver):
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BURGER_SECTION))
        driver.find_element(*Locators.LINK_FILLINGS).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.HEADER_FILLING)).is_displayed()

    def test_menu_constructor_tab_sauces(self, driver):
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BURGER_SECTION))
        driver.find_element(*Locators.LINK_SAUCES).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.HEADER_SAUCES)).is_displayed()

    def test_menu_constructor_tab_buns(self, driver):
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BURGER_SECTION))
        driver.find_element(*Locators.LINK_SAUCES).click()
        driver.find_element(*Locators.LINK_BUNS).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.HEADER_BUNS)).is_displayed()


