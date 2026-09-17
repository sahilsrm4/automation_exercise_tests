
from playwright.sync_api import Page


class AccountCreatedPage:

    def __init__(self, page: Page):
        self.page = page

        self.account_created_message = page.locator(
            "[data-qa='account-created']"
        )

        self.continue_button = page.locator(
            "[data-qa='continue-button']"
        )

    def is_account_created(self):
        return self.account_created_message.is_visible()

    def continue_to_home(self):
        self.continue_button.click()

