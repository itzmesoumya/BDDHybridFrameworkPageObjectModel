from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_linktext = "Login"
    register_option_linktext = "Register"
    enter_product_name="search"
    search_button_xpath = "//div[@id='search']//button[@class='btn btn-default btn-lg']"

    def enter_product_name_in_searchbox(self,product_name):
        self.driver.find_element(By.NAME,self.enter_product_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def click_on_myaccount_option(self):
        self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_linktext).click()

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_linktext).click()