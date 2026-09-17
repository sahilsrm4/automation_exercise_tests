from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        self.name = page.locator(
            "input[data-qa='signup-name']"
        )

        self.email = page.locator(
            "input[data-qa='signup-email']"
        )

        self.signup_button = page.locator(
            "button[data-qa='signup-button']"
        )

        self.email_exists_message = page.get_by_text(
            "Email Address already exist!"
        )

        self.account_information_heading = page.get_by_text(
            "Enter Account Information"
        )

    def signup(self, name, email):
        self.name.fill(name)
        self.email.fill(email)
        self.signup_button.click()

    def is_email_already_registered(self):
        return self.email_exists_message.is_visible()

    def is_account_information_visible(self):
        return self.account_information_heading.is_visible()