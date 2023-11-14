import pytest
import allure

from pages.fususone.fusus_page import HomePage
from utils.driver_factory import DriverFactory

#@pytest.mark.usefixtures("setup")
class TestHomePage:

    @allure.title("Home page - smoke test on Chrome Browser")
    @allure.description("Check if home page of fususone has correct title on Chrome Browser")
    def test_homepage_title_chrome(self):
        config = {
            "browser": "chrome",
            "headless_mode": False,
            "base_url": "https://fususone.com/",
            "timeout": 10
        }
        driver = DriverFactory.get_driver(config)
        driver.implicitly_wait(config["timeout"])
        driver.maximize_window()
        homepage = HomePage(driver)
        homepage.open()
        homepage.enterEmailAndNext()
        homepage.loginClick()
        homepage.enterPass()
        homepage.loginClick()
        assert("fususONE" in homepage.get_page_title())

    @allure.title("Home page - smoke test on Firefox Browser")
    @allure.description("Check if home page of fususone has correct title on Firefox Browser")
    def test_homepage_title_firefox(self):
        config = {
            "browser": "firefox",
            "headless_mode": False,
            "base_url": "https://fususone.com/",
            "timeout": 20
        }
        driver = DriverFactory.get_driver(config)
        driver.implicitly_wait(config["timeout"])
        driver.maximize_window()
        homepage = HomePage(driver)
        homepage.open()
        homepage.enterEmailAndNext()
        homepage.loginClick()
        homepage.enterPass()
        homepage.loginClick()
        assert ("fususONE" in homepage.get_page_title())

    @allure.title("Home page - smoke test on Edge Browser")
    @allure.description("Check if home page of fususone has correct title on Edge Browser")
    def test_homepage_title_edge(self):
        config = {
            "browser": "edge",
            "headless_mode": False,
            "base_url": "https://fususone.com/",
            "timeout": 20
        }
        driver = DriverFactory.get_driver(config)
        driver.implicitly_wait(config["timeout"])
        driver.maximize_window()
        homepage = HomePage(driver)
        homepage.open()
        homepage.enterEmailAndNext()
        homepage.loginClick()
        homepage.enterPass()
        homepage.loginClick()
        assert ("fususONE" in homepage.get_page_title())
