from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.alerta_erro = page.locator("[data-test='error']")
        self.titulo = page.locator("[data-test='title']")

