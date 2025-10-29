class HomePage:
    """Represents the Service NSW Stamp Duty landing page."""

    def __init__(self, page):
        self.page = page
        self.check_online_link = "a:has-text('Check online')"

    def open_stamp_duty_calculator(self):
        """Click the Check Online button."""
        self.page.wait_for_selector(self.check_online_link, timeout=10000)
        link = self.page.locator(self.check_online_link).first
        link.scroll_into_view_if_needed()
        link.click(force=True)
        print("✅ Clicked 'Check online' on Home page.")
