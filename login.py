from playwright.sync_api import Playwright,expect,Page
import time
import pytest



@pytest.fixture(scope="module")
def shared_data():
    return {}

@pytest.fixture(scope="module")
def shared_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()

    yield page

    context.close()
    browser.close()

@pytest.mark.parametrize("email,password",[
    ("sahil9068@gmail.com","Sahil@123")
])
def test_valid_login(shared_page:Page,email,password):
    shared_page.goto("https://automationexercise.com/")
    shared_page.locator("a").filter(has_text=" Signup / Login").click()
    shared_page.locator("input[type='email'][data-qa='login-email']").fill(email)
    shared_page.locator("input[type='password'][data-qa='login-password']").fill(password)
    shared_page.locator('button[data-qa="login-button"]').click()

@pytest.mark.parametrize("email,password",[
    ("sahil@gmail.com","1234"),
    ("mohan@gmail.com","pass1234"),
    ("komal@gmail.com","pet1234")
])
def test_invalid_login(page:Page,email,password):
    page.goto("https://automationexercise.com/")
    page.locator("a").filter(has_text=" Signup / Login").click()
    page.locator("input[type='email'][data-qa='login-email']").fill(email)
    page.locator("input[type='password'][data-qa='login-password']").fill(password)
    page.locator('button[data-qa="login-button"]').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

@pytest.mark.parametrize("Product",[
    ("T-shirt"),
    ("Shirts"),
    ("Jackets"),
    ("Jeans")
])
def test_adding_item_to_cart(shared_page:Page,shared_data,Product):
    shared_page.get_by_role("link", name="Products").click()
    shared_page.locator("input[name='search']").fill(Product)
    shared_page.locator("#submit_search").click()
    if(shared_page.locator(".product-image-wrapper").count() >0):
      shared_page.locator(".add-to-cart").first.click()
      product_id = shared_page.locator(".add-to-cart").first.get_attribute("data-product-id")
      shared_data["product_id"] = product_id
      expect(shared_page.locator("div[class='modal-content']").filter(has_text="Added")).to_be_visible()
      shared_page.get_by_role("button",name="Continue Shopping").click()
    time.sleep(2)

def test_item_in_cart(shared_page:Page,shared_data):
     shared_page.get_by_role("link",name="Cart").click()
     if shared_data:
       expect(shared_page.locator(f"tr[id='product-{shared_data['product_id']}']")).to_have_count(1)
     time.sleep(2)

def test_logout(shared_page:Page):
    shared_page.get_by_role("link",name="Logout").click()
    time.sleep(2)
