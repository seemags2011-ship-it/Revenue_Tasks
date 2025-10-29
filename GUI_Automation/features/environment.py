from utils.browser_manager import BrowserManager
from page_objects.home_page import HomePage
from page_objects.stamp_duty_calculator_page import StampDutyCalculatorPage

def before_all(context):
    print("🚀 Launching browser from environment setup...")
    context.browser_manager = BrowserManager()
    context.page = context.browser_manager.launch_browser(headless=False)
    context.home_page = HomePage(context.page)
    context.calculator_page = StampDutyCalculatorPage(context.page)
    print("✅ Browser launched successfully and page objects initialized.")

def after_all(context):
    print("🧹 Closing browser after all scenarios...")
    try:
        context.browser_manager.close_browser()
        print("✅ Browser closed successfully.")
    except Exception as e:
        print(f"⚠️ Cleanup error: {e}")

