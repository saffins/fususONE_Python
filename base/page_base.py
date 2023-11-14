import allure

from locators.locators import fususLogin


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    @allure.step("Enter email and click Next")
    def enterEmailAndNext(self):
        self.driver.find_element(*fususLogin.email).send_keys("rbayonne@fusus.com")

    @allure.step("Enter password")
    def enterPass(self):
        self.driver.find_element(*fususLogin.passwd).send_keys("test123")

    @allure.step("click login")
    def loginClick(self):
        self.driver.find_element(*fususLogin.signBtn).click()
