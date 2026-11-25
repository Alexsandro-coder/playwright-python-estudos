from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_com_sucesso(page: Page):
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.fazer_login("standard_user", "secret_sauce")

    # Valida a mudança de rota (o título "Products" ficará sob responsabilidade da InventoryPage)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_usuario_bloqueado(page: Page):
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.fazer_login("locked_out_user", "secret_sauce")

    expect(login_page.alerta_erro).to_be_visible()
    expect(login_page.alerta_erro).to_have_text("Epic sadface: Sorry, this user has been locked out.")