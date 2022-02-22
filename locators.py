from selenium.webdriver.common.by import By


class web_Locators:

    sign_User_Name = (By.XPATH, "//input[@id='sign-username']")
    sign_User_Password = (By.XPATH, "//input[@id='sign-password']")
    sign_Up_Button = (By.XPATH, "//button[contains(text(),'Sign up')]")
    sign_Close_Button = (By.XPATH, "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]")
    login_User_Name = (By.XPATH, "//input[@id='loginusername']")
    login_User_Password = (By.XPATH, "//input[@id='loginpassword']")
    login_Submit_Button = (By.XPATH, "//button[contains(text(),'Log in')]")
    login_Close_Buttton = (By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]")
    item_From_Shop = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    add_To_Cart_Button = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    item_name_checker = (By.XPATH, "//h2[contains(text(),'Samsung galaxy s6')]")
    price = (By.XPATH, "//body/div[5]/div[1]/div[2]/h3[1]")
    price_In_Cart = (By.XPATH, "//td[contains(text(),'Samsung galaxy s6')]")
    total_Price = (By.XPATH, "//h3[@id='totalp']")
    place_Order_Button = (By.XPATH, "//button[contains(text(),'Place Order')]")
    total_In_form = (By.XPATH, "//label[@id='totalm']")
    form_Fileds = (By.XPATH, "//input[@class='form-control']")
    form_purces = (By.XPATH, "//button[contains(text(),'Purchase')]")
