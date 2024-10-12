import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Pass the website URL in Browser')
def step_impl(context):
    context.driver.get("https://katalon-demo-cura.herokuapp.com")


@then(u'User must land to Website Home Page')
def step_impl(context):
    assert context.driver.title.__eq__("CURA Healthcare Service")
    context.driver.quit()


@when(u'Click on the Appointment Button')
def step_impl(context):
    context.driver.find_element(By.ID, "btn-make-appointment").click()


@then(u'User should redirect to login Page')
def step_impl(context):
    #assert context.driver.current_URL.__eq__("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    assert context.driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[1]/h2').text.__eq__("Login")
    context.driver.quit()


@when(u'Click on the Menu icon')
def step_impl(context):
    context.driver.find_element(By.ID, "menu-toggle").click()
    time.sleep(5)


@then(u'Menu bar  should open & have Home & Login Shortcut links')
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//nav/ul/li")
    texts = [element.text for element in elements]
    print(texts)
    assert "Home" in texts
    assert "Login" in texts

    context.driver.quit()
