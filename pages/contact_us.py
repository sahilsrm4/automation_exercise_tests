from playwright.sync_api import Page


class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page

        # Contact form
        self.name = page.locator("[data-qa='name']")
        self.email = page.locator("[data-qa='email']")
        self.subject = page.locator("[data-qa='subject']")
        self.message = page.locator("[data-qa='message']")
        self.upload_file = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("[data-qa='submit-button']")

        # Contact Us success message
        self.success_message = page.locator(
            "#contact-page .status.alert-success"
        )

        # Home button after successful submission
        self.home_button = page.locator(
            "#form-section a.btn-success"
        )

    def navigate_to_contact_us(self):
        self.page.goto(
            "https://automationexercise.com/contact_us"
        )

    def fill_contact_form(self, name, email, subject, message):
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.message.fill(message)

    def upload_file_fn(self, file_path):
        self.upload_file.set_input_files(file_path)

    def submit_form(self):
        # Handle JavaScript confirm popup
        self.page.once(
            "dialog",
            lambda dialog: dialog.accept()
        )

        self.submit_button.click()

    def get_success_message(self):
        return self.success_message.text_content()

    def is_home_button_visible(self):
        return self.home_button.is_visible()