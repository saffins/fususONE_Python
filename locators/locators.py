from selenium.webdriver.common.by import By


class fususLogin:
    email = (By.XPATH,"//*[@placeholder='Enter email']")
    passwd = (By.XPATH,"//*[@type='password']")
    signBtn = (By.XPATH,"(//*[@class='mat-button-focus-overlay']/parent::button)[2]")