from datetime import datetime
from behave import *
from selenium.webdriver.common.by import By
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to Register Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_myaccount_option()
    context.home_page.click_on_register_option()


@when(u'I enter mandatory fields')
def step_impl(context):
    context.register_page =RegisterPage(context.driver)
    context.register_page.first_name_text_field("soumya")
    context.register_page.last_name_text_field("ranjan")
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace(" ", "_").replace(":", "_")
    new_email = "soumyaranjan" + timestamp + "@gmail.com"
    context.register_page.email_text_field(new_email)
    context.register_page.phone_number_field("1234567890")
    context.register_page.password_text_field("soumya")
    context.register_page.confirm_password_text_field("soumya")
    context.driver.find_element(By.NAME,"agree").click()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page=RegisterPage(context.driver)
    context.register_page.click_on_continue_button()

@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    context.account_page=AccountPage(context.driver)
    assert context.account_page.display_create_account_message().__eq__(expected_text)


@when(u'I enter all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.first_name_text_field("soumya")
    context.register_page.last_name_text_field("ranjan")
    current_datetime = datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace(" ", "_").replace(":", "_")
    new_email = "soumyaranjan" + timestamp + "@gmail.com"
    context.register_page.email_text_field(new_email)
    context.register_page.phone_number_field("1234567890")
    context.register_page.password_text_field("soumya")
    context.register_page.confirm_password_text_field("soumya")
    context.register_page.yes_radio_button()
    context.driver.find_element(By.NAME,"agree").click()


@when(u'I enter existing  account email into email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.first_name_text_field("soumya")
    context.register_page.last_name_text_field("ranjan")
    context.register_page.email_text_field("demoauto@gmail.com")
    context.register_page.phone_number_field("1234567890")
    context.register_page.password_text_field("soumya")
    context.register_page.confirm_password_text_field("soumya")
    context.driver.find_element(By.NAME,"agree").click()


@then(u'I get duplicate warning message')
def step_impl(context):
    expected_text = "Warning: E-Mail Address is already registered!"
    context.register_page=RegisterPage(context.driver)
    assert context.register_page.display_duplicate_warning_message().__eq__(expected_text)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.first_name_text_field("")
    context.register_page.last_name_text_field("")
    context.register_page.email_text_field("")
    context.register_page.phone_number_field("")
    context.register_page.password_text_field("")
    context.register_page.confirm_password_text_field("")
    context.driver.find_element(By.NAME,"agree").click()


@then(u'Proper warning messages for every fields should be displayed')
def step_impl(context):
    context.register_page= RegisterPage(context.driver)
    first_name_expected = "First Name must be between 1 and 32 characters!"
    assert context.register_page.display_first_name_warning_message().__eq__(first_name_expected)
    last_name_expected = "Last Name must be between 1 and 32 characters!"
    assert context.register_page.display_last_name_warning_message().__eq__(last_name_expected)
    email_expected = "E-Mail Address does not appear to be valid!"
    assert context.register_page.display_email_warning_message().__eq__(email_expected)
    telephone_expected = "Telephone must be between 3 and 32 characters!"
    assert context.driver.find_element(By.XPATH,"//div[@class='col-sm-10']//div[text()='Telephone must be between 3 and 32 characters!']").text.__eq__(telephone_expected)
    password_expected = "Password must be between 4 and 20 characters!"
    assert context.register_page.display_password_warning_message().__eq__(password_expected)