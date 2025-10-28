Feature: Check Motor Vehicle Stamp Duty

  Scenario: Verify vehicle stamp duty calculation flow
    Given I navigate to the Service NSW stamp duty page
    When I click on "Check online" button
    Then I should see the vehicle stamp duty calculator page
    When I select "Yes" for new vehicle
    And I enter "35000" as the vehicle amount
    And I click the "Calculate" button
    Then I should see a popup window with calculation results