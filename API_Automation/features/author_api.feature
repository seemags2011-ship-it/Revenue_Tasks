Feature: Validate Author API from OpenLibrary
  Verify that the author details API returns correct information.

  Scenario: Fetch author details and validate response
    Given I fetch author details from OpenLibrary API
    Then the response should contain author name as "Sachi Rautroy"
    And the alternate name should be "Yugashrashta Sachi Routray"
