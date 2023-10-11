from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context, driver):
    selected_browser = ConfigReader.read_configuration("basic info","browser")
    if selected_browser.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif selected_browser.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif selected_browser.__eq__("edge"):
        context.driver = webdriver.Edge()
    else:
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))


def after_scenario(context, driver):
    context.driver.quit()