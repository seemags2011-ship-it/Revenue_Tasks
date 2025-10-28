import requests
from behave import given, then

@given('I send a GET request to "{url}"')
def step_send_get_request(context, url):
    context.response = requests.get(url, timeout=15)

@then('the response status code should be {status_code:d}')
def step_validate_status_code(context, status_code):
    actual = context.response.status_code
    assert actual == status_code, f"Expected {status_code}, got {actual}"

@then('the field "{field}" should be "{expected_value}"')
def step_validate_field_value(context, field, expected_value):
    data = context.response.json()
    actual = data.get(field)
    assert actual == expected_value, f'Expected "{expected_value}", got "{actual}"'

@then('the field "{field}" should contain "{expected_value}"')
def step_validate_array_contains(context, field, expected_value):
    data = context.response.json()
    arr = data.get(field, [])
    assert isinstance(arr, list), f'"{field}" is not a list. Actual: {type(arr)}'
    assert expected_value in arr, f'"{expected_value}" not found in {arr}'
