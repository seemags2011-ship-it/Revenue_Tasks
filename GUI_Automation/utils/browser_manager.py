from playwright.sync_api import sync_playwright

class BrowserManager:
    """Manages Playwright browser lifecycle."""

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def launch_browser(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless, slow_mo=100)
        self.page = self.browser.new_page()
        return self.page

    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
