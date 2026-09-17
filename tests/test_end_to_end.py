from pathlib import Path

from playwright.sync_api import Page, expect
import pytest
import sys

sys.path.append(r"D:\WatchGuard\playwright_opencart_project")

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

from utils.csv_handler import read_csv
from secret_manager.password.decryption import decrypt_password
from config.constant import VALID_LOGIN_FILE,INVALID_LOGIN_FILE,PRODUCTS_FILE,BASE_URL


# Read CSV data
valid_login_data = read_csv(VALID_LOGIN_FILE)
invalid_login_data = read_csv(INVALID_LOGIN_FILE)
product_data = read_csv(PRODUCTS_FILE)


@pytest.mark.parametrize("data", invalid_login_data)
def test_invalid_login(page: Page, data):

    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login_with_credentials(
        data["email"],
        data["password"]
    )

    expect(
        login_page.invalid_login_message
    ).to_be_visible()


@pytest.mark.parametrize("data", valid_login_data)
def test_valid_login(page: Page, data):

    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login_with_credentials(
        data["email"],
        decrypt_password(data["password"])

    )

    expect(
        login_page.logged_in_as
    ).to_be_visible()


def test_login(shared_page: Page):

    shared_page.goto(BASE_URL)

    login_page = LoginPage(shared_page)
    data = valid_login_data[0]
    login_page.login_with_credentials(
        data["email"],
        decrypt_password(data["password"])
    )

    expect(
        login_page.logged_in_as
    ).to_be_visible()


@pytest.mark.parametrize("data", product_data)
def test_adding_item_to_cart(
    shared_page: Page,
    shared_data,
    data
):

    home_page = HomePage(shared_page)
    products_page = ProductsPage(shared_page)

    home_page.open_products()

    products_page.search_product(
        data["product"]
    )

    if products_page.product_exists():

        product_id = (
            products_page.add_first_product_to_cart()
        )

        shared_data["product_ids"].append(product_id)


def test_item_in_cart(
    shared_page: Page,
    shared_data
):

    home_page = HomePage(shared_page)
    cart_page = CartPage(shared_page)

    home_page.open_cart()

    for product_id in shared_data["product_ids"]:

        product = cart_page.get_product(product_id)

        expect(product).to_have_count(1)


def test_logout(page):

    page.goto(BASE_URL)

    login_page = LoginPage(page)

    # Login
    login_page.login_with_credentials(
        "sahil9068@gmail.com",
        "Sahil@123"
    )

    # Verify login
    assert login_page.is_logged_in()

    # Logout
    login_page.logout()

    # Verify logout
    assert login_page.is_logged_out()