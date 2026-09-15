from playwright.sync_api import Playwright,expect,Page
import time
import pytest

@pytest.fixture
def login_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://automationexercise.com/")
    page.locator("a").filter(has_text=" Signup / Login").click()
    page.locator("input[type='email'][data-qa='login-email']").fill("sahil9068@gmail.com")
    page.locator("input[type='password'][data-qa='login-password']").fill("Sahil@123")
    page.locator('button[data-qa="login-button"]').click()
    return page

def test_adding_item_to_cart(login_page):
    login_page.get_by_role("link", name="Products").click()
    login_page.locator("input[name='search']").fill("T-Shirt")
    login_page.locator("#submit_search").click()
    login_page.locator(".add-to-cart").first.click()
    expect(login_page.locator("div[class='modal-content']").filter(has_text="Added")).to_be_visible()
    login_page.get_by_role("button",name="Continue Shopping").click()
    time.sleep(2)



