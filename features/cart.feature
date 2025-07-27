@cart
Feature: Cart Module
  As a logged-in user of the Sauce Demo application
  I want to manage items in my shopping cart
  So that I can review and modify my selections before checkout

  Background:
    Given user is on "https://www.saucedemo.com/"
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @smoke @cart
  Scenario: View cart contents
    Given user is on the products page
    When user clicks Add to cart
    And user clicks cart icon
    Then verify page has text "Your Cart"
    And cart page displays selected items

  @cart
  Scenario: View empty cart
    When user clicks on cart icon
    Then verify page has text "Your Cart"
    And cart should be empty

  @cart
  Scenario: Add item and verify in cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on cart icon
    Then verify page has text "Your Cart"
    And cart should contain "Sauce Labs Backpack"
    And cart item should have price "$29.99"

  @cart
  Scenario: Remove item from cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on cart icon
    And user clicks on "Remove" button for "Sauce Labs Backpack"
    Then cart should be empty

  @cart
  Scenario: Continue shopping from cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on cart icon
    And user clicks on "Continue Shopping" button
    Then verify page has text "Products"
    And user should be on products page

  @cart
  Scenario: Multiple items in cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on "Add to cart" button for "Sauce Labs Bike Light"
    And user clicks on cart icon
    Then verify page has text "Your Cart"
    And cart should contain "Sauce Labs Backpack"
    And cart should contain "Sauce Labs Bike Light"
    And cart should have 2 items

  @cart
  Scenario: Verify cart item details
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on cart icon
    Then cart item "Sauce Labs Backpack" should have correct details
    And item quantity should be "1"
    And item description should be displayed
