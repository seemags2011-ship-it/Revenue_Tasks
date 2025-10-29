from behave import given, when, then
from api_objects.author_service import get_author_details
from utils.api_helpers import verify_status_code, verify_field_value


@given("I fetch author details from OpenLibrary API")
def step_fetch_author_details(context):
    context.response = get_author_details("OL1A")  # Sachi Rautroy


@then('the response should contain author name as "Sachi Rautroy"')
def step_verify_author_name(context):
    verify_status_code(context.response, 200)
    data = context.response.json()
    verify_field_value(data, "personal_name", "Sachi Rautroy")


@then('the alternate name should be "Yugashrashta Sachi Routray"')
def step_verify_alternate_name(context):
    data = context.response.json()
    # alternate_names is a list
    assert "Yugashrashta Sachi Routray" in data.get("alternate_names", []), \
        f"Expected alternate name not found. Found: {data.get('alternate_names')}"
