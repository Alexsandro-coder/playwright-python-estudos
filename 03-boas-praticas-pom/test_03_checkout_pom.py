from playwright.sync_api import Page, expect

import pages


def test_fluxo_checkout_completo(pagina_logada: Page):
    inventory = pages.InventoryPage(pagina_logada)
    cart = pages.CartPage(pagina_logada)
    checkout = pages.CheckoutPage(pagina_logada)

    inventory.adicionar_mochila_ao_carrinho()
    inventory.ir_para_carrinho()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.nome_item).to_have_text("Sauce Labs Backpack")

    cart.avancar_para_checkout()

    checkout.preencher_cadastro("alex", "sandro", "57460000")
    checkout.clicar_botao_continuar()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout.nome_item).to_have_text("Sauce Labs Backpack")

    checkout.clicar_botao_finalizar()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout.titulo).to_have_text("Checkout: Complete!")
    expect(checkout.mensagem_sucesso).to_have_text("Thank you for your order!")


def test_checkout_sem_preencher_dados(pagina_logada: Page):
    inventory = pages.InventoryPage(pagina_logada)
    cart = pages.CartPage(pagina_logada)
    checkout = pages.CheckoutPage(pagina_logada)

    inventory.adicionar_mochila_ao_carrinho()
    inventory.ir_para_carrinho()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.nome_item).to_have_text("Sauce Labs Backpack")

    cart.avancar_para_checkout()
    checkout.clicar_botao_continuar()

    expect(checkout.alerta_erro).to_be_visible()
    expect(checkout.alerta_erro).to_have_text("Error: First Name is required")