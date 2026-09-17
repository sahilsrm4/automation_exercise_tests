from pathlib import Path
import sys

import pytest
from playwright.sync_api import Page, expect

sys.path.append(r"D:\WatchGuard\playwright_opencart_project")

from pages.signup_page import SignupPage
from pages.account_information import AccountInformationPage
from utils.csv_handler import read_csv


BASE_DIR = Path(__file__).resolve().parent.parent

REGISTER_DATA_FILE = (
    BASE_DIR / "test_data" / "register_user.csv"
)

register_data = read_csv(REGISTER_DATA_FILE)

def test_signup_with_existing_email(page):

    page.goto("https://automationexercise.com/signup")
    signup_page = SignupPage(page)

    signup_page.signup(
        "Sahil",
        "sahil9068@gmail.com"
    )

    expect(
        signup_page.email_exists_message
    ).to_be_visible()

@pytest.mark.parametrize("data", register_data)
def test_register_user(page: Page, data):

    page.goto("https://automationexercise.com/signup")

    signup_page = SignupPage(page)

    signup_page.signup(
        name=data["name"],
        email=data["email"]
    )

    account_page = AccountInformationPage(page)

    account_page.fill_account_information(
        password=data["password"],
        day=data["day"],
        month=data["month"],
        year=data["year"],
        title=data["title"]
    )

    account_page.fill_address_information(
        first_name=data["first_name"],
        last_name=data["last_name"],
        company=data["company"],
        address=data["address"],
        address2=data["address2"],
        country=data["country"],
        state=data["state"],
        city=data["city"],
        zipcode=data["zipcode"],
        mobile_number=data["mobile_number"]
    )

    account_created_page = account_page.create_account()

    expect(
        account_created_page.account_created_message
    ).to_be_visible()

    account_created_page.continue_to_home()