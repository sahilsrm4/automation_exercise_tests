import sys
sys.path.append("D:\WatchGuard\playwright_opencart_project")
from playwright.sync_api import Page
from pages.account_created_page import AccountCreatedPage

class AccountInformationPage:

    def __init__(self, page: Page):
        self.page = page

        # Account Information
        self.title_mr = page.locator(
            "input[name='title'][value='Mr']"
        )

        self.title_mrs = page.locator(
            "input[name='title'][value='Mrs']"
        )

        self.name = page.locator(
            "input[data-qa='name']"
        )

        self.email = page.locator(
            "input[data-qa='email']"
        )

        self.password = page.locator(
            "input[data-qa='password']"
        )

        # Date of Birth
        self.days = page.locator(
            "select[data-qa='days']"
        )

        self.months = page.locator(
            "select[data-qa='months']"
        )

        self.years = page.locator(
            "select[data-qa='years']"
        )

        # Checkboxes
        self.newsletter = page.locator(
            "input[data-qa='newsletter']"
        )

        self.special_offers = page.locator(
            "input[data-qa='optin']"
        )

        # Address
        self.first_name = page.locator(
            "input[data-qa='first_name']"
        )

        self.last_name = page.locator(
            "input[data-qa='last_name']"
        )

        self.company = page.locator(
            "input[data-qa='company']"
        )

        self.address = page.locator(
            "input[data-qa='address']"
        )

        self.address2 = page.locator(
            "input[data-qa='address2']"
        )

        self.country = page.locator(
            "select[data-qa='country']"
        )

        self.state = page.locator(
            "input[data-qa='state']"
        )

        self.city = page.locator(
            "input[data-qa='city']"
        )

        self.zipcode = page.locator(
            "input[data-qa='zipcode']"
        )

        self.mobile_number = page.locator(
            "input[data-qa='mobile_number']"
        )

        self.create_account_button = page.locator(
            "button[data-qa='create-account']"
        )

    def fill_account_information(
        self,
        password,
        day,
        month,
        year,
        title="Mr"
    ):
        if title == "Mr":
            self.title_mr.check()
        else:
            self.title_mrs.check()

        self.password.fill(password)

        self.days.select_option(day)
        self.months.select_option(month)
        self.years.select_option(year)

    def select_newsletter(self):
        self.newsletter.check()

    def select_special_offers(self):
        self.special_offers.check()

    def fill_address_information(
        self,
        first_name,
        last_name,
        company,
        address,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address.fill(address)
        self.address2.fill(address2)

        self.country.select_option(country)

        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)

    def create_account(self):
        self.create_account_button.click()
        return AccountCreatedPage(self.page)