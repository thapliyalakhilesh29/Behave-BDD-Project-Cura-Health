from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the browser and navigate to login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")



@when(u'User keep the mandatory field empty and click the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "txt-username").clear()
    context.driver.find_element(By.ID, "txt-password").clear()
    context.driver.find_element(By.ID, "btn-login").click()



@then(u'Error message should be displayed')
def step_impl(context):
    actual_error = context.driver.find_element(By.XPATH, '//p[@class="lead text-danger"]').text
    expected_error = "Login failed! Please ensure the username and password are valid."
    assert actual_error.__eq__(expected_error)
    context.driver.quit()


@when(u'Provide valid username and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, "txt-username").send_keys('John Doe')
    context.driver.find_element(By.ID, "txt-password").send_keys('123')
    context.driver.find_element(By.ID, "btn-login").click()


@then(u'A Error message should be displayed')
def step_impl(context):
    actual_error = context.driver.find_element(By.XPATH, '//p[@class="lead text-danger"]').text
    expected_error = 'Login failed! Please ensure the username and password are valid.'
    assert actual_error.__eq__(expected_error)
    context.driver.quit()



@when(u'Provide invalid username and valid password')
def step_impl(context):
    context.driver.find_element(By.ID, "txt-username").send_keys('a123')
    context.driver.find_element(By.ID, "txt-password").send_keys('ThisIsNotAPassword')
    context.driver.find_element(By.ID, "btn-login").click()


@then(u'Different Error message should be displayed')
def step_impl(context):
    actual_error = context.driver.find_element(By.XPATH, '//p[@class="lead text-danger"]').text
    expected_error = 'Login failed! Please ensure the username and password are valid.'
    assert actual_error.__eq__(expected_error)
    context.driver.quit()


@when(u'Provide valid username and valid password')
def step_impl(context):
    context.driver.find_element(By.ID, "txt-username").send_keys('John Doe')
    context.driver.find_element(By.ID, "txt-password").send_keys('ThisIsNotAPassword')
    context.driver.find_element(By.ID, "btn-login").click()

@then(u'User  should redirected to Appointment page.')
def step_impl(context):
    assert context.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
