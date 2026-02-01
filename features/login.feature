Feature: Login functionality

  @smoke
  Scenario: User login with valid credentials
    Given user is on login page
    When user login with valid username and password
    Then user should be redirected to dashboard