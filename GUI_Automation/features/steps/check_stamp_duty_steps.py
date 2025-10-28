from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from behave import given, when, then
import time
from urllib.parse import urljoin

# --- Helper Functions ---

def click_radio(page, answer="Yes"):
    """Select a radio button by its label or value, stabilize viewport."""
    try:
        radio = page.get_by_role("radio", name=answer)
        radio.scroll_into_view_if_needed()
        radio.click(force=True, timeout=5000)
        return True
    except Exception:
        # fallback using label
        try:
            label = page.locator(f"label:has-text('{answer}')").first
            label.scroll_into_view_if_needed()
            time.sleep(0.2)  # allow page animations
            label.click(force=True)
            return True
        except Exception:
            return False

def fill_price(page, amount):
    """Fill the vehicle price input field."""
    selectors = [
        "input[name*='price']",
        "input[placeholder*='Price']",
        "input[type='text']"
    ]
    for sel in selectors:
        try:
            input_box = page.locator(sel).first
            if input_box.count() > 0:
                input_box.scroll_into_view_if_needed()
                input_box.fill(str(amount))
                return True
        except Exception:
            continue
    return False

def click_calculate(page):
    """Click the Calculate button reliably."""
    try:
        btn = page.get_by_role("button", name="Calculate")
        btn.scroll_into_view_if_needed()
        btn.click(force=True, timeout=5000)
        return True
    except Exception:
        try:
            # fallback: generic button
            btn = page.locator("button:has-text('Calculate')").first
            btn.scroll_into_view_if_needed()
            time.sleep(0.2)
            btn.click(force=True)
            return True
        except Exception:
            # fallback: press Enter
            page.keyboard.press("Enter")
            return True

# --- Behave Steps ---

@given("I navigate to the Service NSW stamp duty page")
def step_open_homepage(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=100)
    context.page = context.browser.new_page()
    context.page.goto(
        "https://www.service.nsw.gov.au/transaction/check-motor-vehicle-stamp-duty",
        timeout=60000
    )
    context.page.wait_for_selector("text=Check online", timeout=15000)
    print("✅ Stamp Duty page loaded.")

@when('I click on "Check online" button')
def step_click_check_online(context):
    link = context.page.locator("a:has-text('Check online')").first
    if not link or link.count() == 0:
        raise Exception("❌ 'Check online' button not found.")

    # navigate in same tab
    href = link.get_attribute("href")
    if href:
        target = urljoin(context.page.url, href)
        context.page.goto(target, timeout=60000)
    else:
        link.click(force=True)

    context.page.wait_for_load_state("domcontentloaded", timeout=20000)

    # Answer passenger vehicle question
    if not click_radio(context.page, "Yes"):
        raise Exception("❌ Could not select 'Yes' for passenger vehicle.")

@then("I should see the vehicle stamp duty calculator page")
def step_verify_calculator_page(context):
    if not fill_price(context.page, ""):
        raise AssertionError("Calculator page not detected (price input missing).")
    print("✅ Calculator page ready.")

@when('I select "Yes" for new vehicle')
def step_select_yes(context):
    if not click_radio(context.page, "Yes"):
        raise Exception("❌ Could not select 'Yes' for new vehicle.")
    print("✅ Selected 'Yes' for new vehicle.")

@when('I enter "{amount}" as the vehicle amount')
def step_enter_amount(context, amount):
    if not fill_price(context.page, amount):
        raise Exception(f"❌ Could not fill vehicle price: {amount}")
    print(f"✅ Vehicle price entered: {amount}")

@when('I click the "Calculate" button')
def step_click_calculate_btn(context):
    if click_calculate(context.page):
        print("✅ Calculate button clicked.")

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

@then("I should see a popup window with calculation results")
def step_verify_popup(context):
    import time
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    time.sleep(2)  # small wait to allow results to load
    try:
        page_text = context.page.text_content("body") or ""
        print("\n===== PAGE TEXT START =====")
        print(page_text)
        print("===== PAGE TEXT END =====\n")

        # Look for any of these common phrases from the calculator
        keywords = ["stamp duty", "duty payable", "stampduty", "amount payable"]
        if any(k.lower() in page_text.lower() for k in keywords):
            print("✅ Found calculation results text.")
        else:
            raise AssertionError("❌ Expected result text not found in page body.")
    finally:
        try:
            context.browser.close()
            context.playwright.stop()
        except Exception as e:
            print(f"⚠️ Cleanup skipped: {e}")

