Feature: Verify the login page


  Scenario: Login without credentials
    Given Launch the browser and navigate to login page
    When User keep the mandatory field empty and click the login button
    Then Error message should be displayed


  Scenario: Login with valid username but invalid password
    Given Launch the browser and navigate to login page
    When Provide valid username and invalid password
    Then Error message should be displayed


  Scenario: Login with invalid username but valid password
    Given Launch the browser and navigate to login page
    When Provide invalid username and valid password
    Then Error message should be displayed


  Scenario: Login with valid username and valid password
    Given Launch the browser and navigate to login page
    When Provide valid username and valid password
    Then User  should redirected to Appointment page.