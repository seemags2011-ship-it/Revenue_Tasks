from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from behave import given, when, then
import time


def safe_goto(page, url, retries=1):
    for attempt in range(retries + 1):
        try:
            page.goto(url, timeout=90000, wait_until="domcontentloaded")
            page.wait_for_selector("text=Check online", timeout=15000)
            print("✅ Page loaded successfully.")
            return True
        except Exception as e:
            if attempt < retries:
                print(f"⚠️ Navigation attempt {attempt+1} failed, retrying... ({e})")
                time.sleep(3)
            else:
                print(f"❌ Navigation failed after {retries+1} attempts: {e}")
                raise


@given("I navigate to the Service NSW stamp duty page")
def step_open_stamp_duty_page(context):
    print("🌐 Navigating to Service NSW stamp duty page...")
    safe_goto(
        context.page,
        "https://www.service.nsw.gov.au/transaction/check-motor-vehicle-stamp-duty",
        retries=1
    )


@when('I click on "Check online" button')
def step_click_check_online(context):
    print("🖱️ Clicking on 'Check online' button...")
    button = context.page.locator("a:has-text('Check online')")
    button.first.click(timeout=10000)
    context.page.wait_for_load_state("domcontentloaded", timeout=15000)
    context.page.wait_for_selector("text=Is this registration for a passenger vehicle?", timeout=20000)
    print("✅ Calculator page loaded successfully.")


@then("I should see the vehicle stamp duty calculator page")
def step_verify_calculator_page(context):
    print("🔍 Verifying calculator page visibility...")
    context.page.wait_for_selector("text=Is this registration for a passenger vehicle?", timeout=15000)
    print("✅ Calculator page verified.")


@when('I select "Yes" for new vehicle')
def step_select_yes(context):
    print("🚗 Selecting 'Yes' for new vehicle question...")
    radio = context.page.locator("label:has-text('Yes')")
    radio.first.click(timeout=5000)
    print("✅ Selected 'Yes' successfully.")


@when('I enter "50000" as the vehicle amount')
def step_enter_amount(context):
    print("💰 Entering vehicle price: 50000")
    input_box = context.page.locator("input[type='text']").first
    input_box.fill("50000")
    print("✅ Vehicle price entered successfully.")


@when('I click the "Calculate" button')
def step_click_calculate(context):
    print("🧮 Clicking the 'Calculate' button...")
    btn = context.page.locator("button:has-text('Calculate')").first
    btn.click(timeout=10000)
    print("✅ Clicked 'Calculate' successfully.")
    time.sleep(3)


@then("I should see a popup window with calculation results")
def step_verify_popup(context):
    print("🔍 Verifying calculation popup...")
    body_text = context.page.text_content("body").lower()
    assert "stamp duty" in body_text or "result" in body_text, "❌ Calculation result popup not found."
    print("✅ Popup verified successfully.")
    context.browser_manager.close_browser()
    print("🧹 Browser closed.")
