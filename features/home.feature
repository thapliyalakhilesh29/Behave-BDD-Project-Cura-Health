Feature: Cura Health Home page

  Scenario: Verify the home page
    Given Launch the Chrome Browser
    When Pass the website URL in Browser
    Then User must land to Website Home Page

  Scenario: Verify the functionality of Appointment link button
    Given Launch the Chrome Browser
    When Pass the website URL in Browser
    And Click on the Appointment Button
    Then User should redirect to login Page


  Scenario: Verify the functionality of Menu Button
    Given Launch the Chrome Browser
    When Pass the website URL in Browser
    And Click on the Menu icon
    Then Menu bar  should open & have Home & Login Shortcut links


