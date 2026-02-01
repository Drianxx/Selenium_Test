Feature: Login functionality

  @smoke
  Scenario: User login with valid credentials
    Given user is on login page
    When user login as "standard_user"
    Then user should be redirected to dashboard