Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter all fields
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with duplicate email address
    Given I navigate to Register Page
    When I enter existing  account email into email field
    And I click on Continue button
    Then I get duplicate warning message

  @register
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every fields should be displayed


