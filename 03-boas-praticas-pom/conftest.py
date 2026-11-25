import pytest
from playwright.sync_api import Page, expect

from pages import LoginPage


@pytest.fixture
def pagina_logada(page: Page) -> Page:
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.fazer_login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    return page