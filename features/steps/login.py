from behave import *
from selenium.webdriver.common.by import By
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    context.home_page.click_on_myaccount_option()
    context.home_page.click_on_login_option()


@when(u'I enter valid eamil address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("demoauto@gmail.com")
    context.login_page.enter_password("soumya123")

@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()

@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_edit_account_info()


@when(u'I enter invalid eamil address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("demo@gmail.com")
    context.login_page.enter_password("soumya123")


@then(u'I should get propper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_status_check().__eq__(expected_text)


@when(u'I enter valid eamil address and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("demoauto@gmail.com")
    context.login_page.enter_password("soumya")

@when(u'I enter invalid eamil address and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("demo@gmail.com")
    context.login_page.enter_password("soumya")

@when(u'I  dont enter anything into  the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")