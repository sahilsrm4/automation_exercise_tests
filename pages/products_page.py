from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_box = page.locator(
            "input[name='search']"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.product_cards = page.locator(
            ".product-image-wrapper"
        )

        self.add_to_cart_button = page.locator(
            ".add-to-cart"
        )

        self.added_modal = page.locator(
            "div[class='modal-content']"
        ).filter(has_text="Added")

        self.continue_shopping_button = page.get_by_role(
            "button",
            name="Continue Shopping"
        )

    def search_product(self, product):
        self.search_box.fill(product)
        self.search_button.click()

    def product_exists(self):
        return self.product_cards.count() > 0

    def add_first_product_to_cart(self):

        product_id = self.add_to_cart_button.first.get_attribute(
            "data-product-id"
        )

        self.add_to_cart_button.first.click()

        expect(self.added_modal).to_be_visible()

        self.continue_shopping_button.click()

        return product_id