class StampDutyCalculatorPage:
    """Represents the Motor Vehicle Stamp Duty Calculator page."""

    def __init__(self, page):
        self.page = page
        self.radio_yes = "input[type='radio'][value='yes']"
        self.price_input = "input[name*='price'], input[placeholder*='Price']"
        self.calculate_button = "button:has-text('Calculate')"

    def select_new_vehicle(self):
        self.page.locator(self.radio_yes).scroll_into_view_if_needed()
        self.page.locator(self.radio_yes).click(force=True)
        print("✅ Selected 'Yes' for new vehicle.")

    def enter_vehicle_price(self, amount):
        field = self.page.locator(self.price_input).first
        field.scroll_into_view_if_needed()
        field.fill(str(amount))
        print(f"✅ Entered vehicle price: {amount}")

    def click_calculate_button(self):
        btn = self.page.locator(self.calculate_button)
        btn.scroll_into_view_if_needed()
        btn.click(force=True)
        print("✅ Clicked Calculate button.")
