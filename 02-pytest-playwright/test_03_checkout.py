from playwright.sync_api import Page, expect


def test_fluxo_checkout_completo(pagina_logada: Page):
    # 1. Arrange: adiciona a mochila ao carrinho e acessa o carrinho
    pagina_logada.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    carrinho_de_compras = pagina_logada.locator("[data-test='shopping-cart-link']")
    expect(carrinho_de_compras).to_have_text("1")
    carrinho_de_compras.click()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/cart.html")
    expect(pagina_logada.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")

    # 2. Act: avança para os dados de entrega e preenche o formulário
    pagina_logada.locator("[data-test='checkout']").click()
    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(pagina_logada.locator("[data-test='title']")).to_have_text("Checkout: Your Information")

    pagina_logada.locator("[data-test='firstName']").fill("Alex")
    pagina_logada.locator("[data-test='lastName']").fill("Nobre")
    pagina_logada.locator("[data-test='postalCode']").fill("57460000")

    # 3. Act & Assert: confere o resumo do pedido e finaliza a compra
    pagina_logada.locator("[data-test='continue']").click()
    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(pagina_logada.locator("[data-test='title']")).to_have_text("Checkout: Overview")
    expect(pagina_logada.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")

    pagina_logada.locator("[data-test='finish']").click()
    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(pagina_logada.locator("[data-test='title']")).to_have_text("Checkout: Complete!")
    expect(pagina_logada.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")


def test_checkout_sem_preencher_dados(pagina_logada: Page):
    # 1. Arrange: prepara o caminho mínimo até a tela de informações do checkout
    pagina_logada.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    pagina_logada.locator("[data-test='shopping-cart-link']").click()
    pagina_logada.locator("[data-test='checkout']").click()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # 2. Act: tenta avançar sem preencher nenhum campo obrigatório
    pagina_logada.locator("[data-test='continue']").click()

    # 3. Assert: valida o bloqueio e a mensagem de campo obrigatório
    alerta_erro = pagina_logada.locator("[data-test='error']")
    expect(alerta_erro).to_be_visible()
    expect(alerta_erro).to_have_text("Error: First Name is required")