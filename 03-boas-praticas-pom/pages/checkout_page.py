from playwright.sync_api import Page

from .base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.campo_nome = page.locator("[data-test='firstName']")
        self.campo_sobrenome = page.locator("[data-test='lastName']")
        self.campo_cep = page.locator("[data-test='postalCode']")
        self.botao_continuar = page.locator("[data-test='continue']")
        self.botao_finalizar = page.locator("[data-test='finish']")
        self.mensagem_sucesso = page.locator("[data-test='complete-header']")
        self.nome_item = page.locator("[data-test='inventory-item-name']")

    def preencher_cadastro(self, nome: str, sobrenome: str, cep: str):
        self.campo_nome.fill(nome)
        self.campo_sobrenome.fill(sobrenome)
        self.campo_cep.fill(cep)

    def clicar_botao_continuar(self):
        self.botao_continuar.click()

    def clicar_botao_finalizar(self):
        self.botao_finalizar.click()