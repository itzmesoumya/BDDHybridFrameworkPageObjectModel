from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email_field_id ="input-email"
    password_field_id ="input-password"
    login_button_xpath="//input[@class='btn btn-primary']"
    account_create_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self,email_address):
        self.driver.find_element(By.ID,self.email_field_id).send_keys(email_address)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_field_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def display_status_check(self):
        return self.driver.find_element(By.XPATH,self.account_create_message_xpath).text