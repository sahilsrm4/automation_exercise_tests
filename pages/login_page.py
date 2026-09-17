from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Signup / Login link
        self.signup_login_link = page.locator("a").filter(
            has_text=" Signup / Login"
        )

        # Login form
        self.email = page.locator(
            "input[type='email'][data-qa='login-email']"
        )

        self.password = page.locator(
            "input[type='password'][data-qa='login-password']"
        )

        self.login_button = page.locator(
            "button[data-qa='login-button']"
        )

        # Logged-in user
        self.logged_in_as = page.locator("li").filter(
            has_text="Logged in as"
        )

        # Invalid login message
        self.invalid_login_message = page.get_by_text(
            "Your email or password is incorrect!"
        )

        # Logout
        self.logout_link = page.locator(
            "a[href='/logout']"
        )

    def open_login_page(self):
        self.signup_login_link.click()

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def login_with_credentials(self, email, password):
        self.open_login_page()
        self.login(email, password)

    def is_invalid_login_message_visible(self):
        return self.invalid_login_message.is_visible()

    def is_logged_in(self):
        return self.logged_in_as.is_visible()

    def logout(self):
        self.logout_link.click()

    def is_logged_out(self):
        return self.signup_login_link.is_visible()