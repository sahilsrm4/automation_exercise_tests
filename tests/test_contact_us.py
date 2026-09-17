from pathlib import Path
import sys

from playwright.sync_api import Page, expect
import pytest

sys.path.append(r"D:\WatchGuard\playwright_opencart_project")

from pages.contact_us import ContactUsPage
from utils.csv_handler import read_csv


BASE_DIR = Path(__file__).resolve().parent.parent

CONTACT_DATA_FILE = (
    BASE_DIR / "test_data" / "contact_us.csv"
)

contact_data = read_csv(CONTACT_DATA_FILE)


@pytest.mark.parametrize("data", contact_data)
def test_contact_us(page: Page, data):

    contact_page = ContactUsPage(page)

    # Open Contact Us page
    contact_page.navigate_to_contact_us()

    # Fill contact form
    contact_page.fill_contact_form(
        name=data["name"],
        email=data["email"],
        subject=data["subject"],
        message=data["message"]
    )

    # Upload file
    contact_page.upload_file_fn(
        data["file_path"]
    )

    # Submit form and accept confirmation popup
    contact_page.submit_form()

    # Verify success message
    expect(
        contact_page.success_message
    ).to_be_visible()

    expect(
        contact_page.success_message
    ).to_have_text(
        "Success! Your details have been submitted successfully."
    )

    # Verify Home button
    expect(
        contact_page.home_button
    ).to_be_visible()