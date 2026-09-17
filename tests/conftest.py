import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="module")
def shared_page(playwright: Playwright):

    browser = playwright.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    yield page

    context.close()
    browser.close()


@pytest.fixture(scope="module")
def shared_data():
    return {
        "product_ids": []
    }