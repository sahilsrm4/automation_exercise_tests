from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.products_link = page.get_by_role(
            "link",
            name="Products"
        )

        self.cart_link = page.get_by_role(
            "link",
            name="Cart"
        )

    def open_products(self):
        self.products_link.click()

    def open_cart(self):
        self.cart_link.click()