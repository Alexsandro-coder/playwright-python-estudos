from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator("[data-test='title']")
        self.botao_add_mochila = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.botao_remover_mochila = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.badge_carrinho = page.locator("[data-test='shopping-cart-badge']")
        self.icone_carrinho = page.locator("[data-test='shopping-cart-link']")

    def adicionar_mochila_ao_carrinho(self):
        self.botao_add_mochila.click()

    def remover_mochila_do_carrinho(self):
        self.botao_remover_mochila.click()

    def ir_para_carrinho(self):
        self.icone_carrinho.click()
