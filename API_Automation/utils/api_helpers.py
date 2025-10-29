def verify_status_code(response, expected_code=200):
    """Verify HTTP response status code."""
    assert response.status_code == expected_code, \
        f"Expected status {expected_code}, got {response.status_code}"


def verify_field_value(response_json, field, expected_value):
    """Verify specific field in the JSON response."""
    actual = response_json.get(field)
    assert actual == expected_value, \
        f"Expected '{field}' to be '{expected_value}', got '{actual}'"
