from playwright.sync_api import Playwright, expect
import pytest


def test_get_all_products(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.get(
        "https://automationexercise.com/api/productsList"
    )

    # Status code
    expect(response).to_be_ok()
    assert response.status == 200

    # Response body
    response_json = response.json()

    print(response_json)

    request.dispose()



def test_get_all_brands(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.get(
        "https://automationexercise.com/api/brandsList"
    )

    assert response.status == 200

    body = response.json()

    # Verify response structure
    assert "brands" in body

    brands = body["brands"]

    # Verify brands is a list
    assert isinstance(brands, list)

    # Verify at least one brand exists
    assert len(brands) > 0

    request.dispose()

def test_put_all_brands(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.put(
        "https://automationexercise.com/api/brandsList"
    )

    # HTTP status
    assert response.status == 200

    # API response
    body = response.json()

    assert body["responseCode"] == 405
    assert body["message"] == "This request method is not supported."

    request.dispose()

def test_search_product(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.post(
        "https://automationexercise.com/api/searchProduct",
        data={
            "search_product": "tshirt"
        }
    )

    assert response.status == 200

    body = response.json()

    print(body)

    request.dispose()

def test_search_product_without_parameter(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.post(
        "https://automationexercise.com/api/searchProduct"
    )

    print("HTTP status:", response.status)
    print("Response body:", response.text())

    assert response.status == 200

    body = response.json()

    assert body["responseCode"] == 400
    assert body["message"] == (
        "Bad request, search_product parameter is missing in POST request."
    )

    request.dispose()