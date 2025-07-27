@inventory
Feature: Inventory Module
  As a logged-in user of the Sauce Demo application
  I want to view and interact with the product inventory
  So that I can browse and purchase products

  Background:
    Given user is on "https://www.saucedemo.com/"
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @smoke @inventory
  Scenario: Verify product listing
    Then verify page has text "Products"
    And verify page has text "Add to cart"
    And verify products page has text "Products" and "Add to cart"

  @inventory
  Scenario: Sort products by Name (A–Z)
    Given user is on the products page
    When user clicks Sort Icon
    And user clicks Sort the Products by Name (A–Z)
    Then all the products must be sorted from A to Z

  @inventory
  Scenario: Sort products by Name (Z–A)
    Given user is on the products page
    When user clicks Sort Icon
    And user selects sort option "za"
    Then all the products must be sorted from Z to A

  @inventory
  Scenario: Sort products by Price (Low to High)
    Given user is on the products page
    When user clicks Sort Icon
    And user selects sort option "lohi"
    Then all the products must be sorted by price low to high

  @inventory
  Scenario: Sort products by Price (High to Low)
    Given user is on the products page
    When user clicks Sort Icon
    And user selects sort option "hilo"
    Then all the products must be sorted by price high to low

  @inventory
  Scenario: Add single product to cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    Then the cart badge should show "1"
    And the button should change to "Remove"

  @inventory
  Scenario: Add multiple products to cart
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on "Add to cart" button for "Sauce Labs Bike Light"
    Then the cart badge should show "2"

  @inventory
  Scenario: Remove product from cart on products page
    When user clicks on "Add to cart" button for "Sauce Labs Backpack"
    And user clicks on "Remove" button for "Sauce Labs Backpack"
    Then the cart badge should not be visible
    And the button should change to "Add to cart"
