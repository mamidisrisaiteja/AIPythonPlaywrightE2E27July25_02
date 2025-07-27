@auth
Feature: Authentication Module
  As a user of the Sauce Demo application
  I want to be able to login with valid credentials
  So that I can access the products page

  Background:
    Given user is on "https://www.saucedemo.com/"

  @smoke @auth
  Scenario: Login with valid credentials
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"
    And then redirect to Products page

  @auth
  Scenario: Login with invalid credentials
    When user enters user name as "standard_use" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Login"
    And login Button should be still displayed

  @auth
  Scenario: Login with empty username
    When user enters user name as "" and password as "secret_sauce"
    And click Login Button
    Then login Button should be still displayed
    And error message should be displayed

  @auth
  Scenario: Login with empty password
    When user enters user name as "standard_user" and password as ""
    And click Login Button
    Then login Button should be still displayed
    And error message should be displayed

  @auth
  Scenario: Login with locked out user
    When user enters user name as "locked_out_user" and password as "secret_sauce"
    And click Login Button
    Then login Button should be still displayed
    And error message should contain "locked out"
