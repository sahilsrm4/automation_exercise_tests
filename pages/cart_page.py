from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    def get_product(self, product_id):
        return self.page.locator(
            f"tr[id='product-{product_id}']"
        )

    def product_exists(self, product_id):
        return self.get_product(product_id).count() == 1