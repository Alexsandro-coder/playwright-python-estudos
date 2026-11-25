from playwright.sync_api import Page, expect


def test_adicionar_item_ao_carrinho(pagina_logada: Page):
    # 1. Act: adiciona a mochila ao carrinho na vitrine
    pagina_logada.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # 2. Assert: valida o contador no ícone e entra no carrinho para conferir o produto
    carrinho_de_compras = pagina_logada.locator("[data-test='shopping-cart-link']")
    expect(carrinho_de_compras).to_have_text("1")

    carrinho_de_compras.click()

    expect(pagina_logada).to_have_url("https://www.saucedemo.com/cart.html")
    expect(pagina_logada.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")


def test_remover_item_do_carrinho(pagina_logada: Page):
    # 1. Arrange & Act: adiciona o item e logo em seguida clica em remover na própria vitrine
    pagina_logada.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    pagina_logada.locator("[data-test='remove-sauce-labs-backpack']").click()

    # 2. Verifica o cabeçalho (bolinha do contador sumiu)
    expect(pagina_logada.locator("[data-test='shopping-cart-badge']")).not_to_be_visible()

    # 3. Verifica o card do produto (botão voltou ao estado original de compra)
    expect(pagina_logada.locator("[data-test='add-to-cart-sauce-labs-backpack']")).to_be_visible()
