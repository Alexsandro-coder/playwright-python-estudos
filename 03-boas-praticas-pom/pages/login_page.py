from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        # Mapeia os elementos como objetos Locator reais do Playwright
        self.campo_usuario = page.locator("[data-test='username']")
        self.campo_senha = page.locator("[data-test='password']")
        self.campo_login = page.locator("[data-test='login-button']")

    def acessar(self):
        self.page.goto("https://www.saucedemo.com")

    def fazer_login(self, usuario: str, senha: str):
        self.campo_usuario.fill(usuario)
        self.campo_senha.fill(senha)
        self.campo_login.click()
