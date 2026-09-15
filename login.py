from playwright.sync_api import Playwright,expect
import time


def test_login(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.locator("a").filter(has_text=" Signup / Login").click()
    page.locator("input[type='email'][data-qa='login-email']").fill("sahil9068@gmail.com")
    page.locator("input[type='password'][data-qa='login-password']").fill("Sahil@123")
    page.locator('button[data-qa="login-button"]').click()
    page.get_by_role("link", name="Products").click()
    page.locator("input[name='search']").fill("T-Shirt")
    page.locator("#submit_search").click()
    page.locator(".add-to-cart").first.click()
    expect(page.locator("div[class='modal-content']").filter(has_text="Added")).to_be_visible()
    page.get_by_role("button",name="Continue Shopping").click()
    time.sleep(2)

