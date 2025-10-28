Feature: Validate Open Library Author API

  Scenario: Verify author details from Open Library API
    Given I send a GET request to "https://openlibrary.org/authors/OL1A.json"
    Then the response status code should be 200
    And the field "personal_name" should be "Sachi Rautroy"
    And the field "alternate_names" should contain "Yugashrashta Sachi Routray"
