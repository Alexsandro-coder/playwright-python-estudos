from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.nome_item = page.locator("[data-test='inventory-item-name']")
        self.botao_checkout = page.locator("[data-test='checkout']")

    def avancar_para_checkout(self):
        self.botao_checkout.click()
