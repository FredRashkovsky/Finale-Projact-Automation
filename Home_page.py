from constance import web_Constances
from elements import web_elements
from selenium.webdriver.support import expected_conditions as EC
from locators import web_Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class home_Page_Objacts(web_elements):

    def __init_subclass__(self):
        return super().__init_subclass__()

    def sign_Up(self):
        self.navigate_To(web_Constances.SIGN)
        self.field_input(web_Locators.sign_User_Name, "Fred")
        self.field_input(web_Locators.sign_User_Password, "123password")
        self.driver.find_element(*web_Locators.sign_Up_Button).click()
        self.wait_For_Alert()
        self.driver.find_element(*web_Locators.sign_Close_Button).click()


    def login(self):
        self.navigate_To(web_Constances.LOGIN)
        self.field_input(web_Locators.login_User_Name, "Fred")
        self.field_input(web_Locators.login_User_Password, "123password")
        self.driver.find_element(*web_Locators.login_Submit_Button).click()
        self.wait_For_Alert()
        self.driver.find_element(*web_Locators.login_Close_Buttton).click()

    def buy_item(self):
        self.wait.until(EC.element_to_be_clickable(web_Locators.item_From_Shop)).send_keys(Keys.CONTROL,Keys.RETURN)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        item_price = self.add_To_Cart()
        self.driver.close()
        self.driver.switch_to.window(tabs[0])
        return item_price

    def cart_Item(self, item_price):
        self.navigate_To(web_Constances.CART)
        assert self.wait.until(EC.presence_of_element_located(web_Locators.price_In_Cart))
        assert self.driver.find_element(By.XPATH, "//td[contains(text(),'" + item_price + "')]")
        assert self.driver.find_element(*web_Locators.total_Price).text == item_price
        

class cart_page_objact(home_Page_Objacts):
    def __init_subclass__(self) :
        return super().__init_subclass__()
    
    


test = home_Page_Objacts()
test.sign_Up()
test.login()
test.cart_Item(test.buy_item())

