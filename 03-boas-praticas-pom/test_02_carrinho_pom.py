from playwright.sync_api import Page, expect

import pages


def test_adicionar_item_ao_carrinho(pagina_logada: Page):
    inventory = pages.InventoryPage(pagina_logada)
    cart = pages.CartPage(pagina_logada)

    expect(inventory.titulo).to_have_text("Products")

    inventory.adicionar_mochila_ao_carrinho()
    expect(inventory.badge_carrinho).to_have_text("1")

    inventory.ir_para_carrinho()
    expect(pagina_logada).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.nome_item).to_have_text("Sauce Labs Backpack")


def test_remover_item_do_carrinho(pagina_logada: Page):
    inventory = pages.InventoryPage(pagina_logada)

    inventory.adicionar_mochila_ao_carrinho()
    inventory.remover_mochila_do_carrinho()

    expect(inventory.badge_carrinho).not_to_be_visible()
    expect(inventory.botao_add_mochila).to_be_visible()