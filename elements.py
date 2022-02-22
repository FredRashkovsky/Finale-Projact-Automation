from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constance import web_Constances
from locators import web_Locators
from selenium.webdriver.common.by import By


class web_elements:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(web_Constances.URL)
        self.driver.maximize_window()

    def field_input(self , locator, input):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(input)
    
    def wait_For_Alert(self):
        self.wait.until(EC.alert_is_present()).accept()


    def navigate_To(self, navigateTo):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, navigateTo))).click()

    def add_To_Cart(self):
        assert self.wait.until(EC.presence_of_element_located(web_Locators.item_name_checker))
        self.driver.find_element(*web_Locators.add_To_Cart_Button).click()
        self.wait_For_Alert()
        return  "".join([s for s in list(self.driver.find_element(*web_Locators.price).text) if s.isdigit()])
    
    def home_Button(self):
        self.wait.until(EC.element_to_be_clickable(web_Locators.home_Button)).click()
        




