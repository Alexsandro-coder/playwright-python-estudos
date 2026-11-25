from playwright.sync_api import Page, expect  # Page dá tipagem/autocomplete; expect faz asserções inteligentes


def test_login_com_sucesso(page: Page):
    # O parâmetro `page: Page` é uma fixture do pytest-playwright:
    # ele abre o navegador, cria uma aba limpa e fecha tudo sozinho ao fim do teste.

    # 1. Arrange (Preparação): acessa a página inicial do sistema
    page.goto("https://www.saucedemo.com")

    # 2. Act (Ação): preenche credenciais válidas e submete o formulário
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # 3. Assert (Validação): o expect() aguarda até 5s automaticamente pela condição
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='title']")).to_have_text("Products")


def test_login_usuario_bloqueado(page: Page):
    # Cada função de teste recebe uma `page` nova e isolada (sem cookies do teste anterior)

    # 1. Arrange (Preparação): acessa a página de login
    page.goto("https://www.saucedemo.com")

    # 2. Act (Ação): tenta autenticar com o usuário bloqueado
    page.locator("[data-test='username']").fill("locked_out_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # 3. Assert (Validação): garante que o alerta apareceu e exibe a mensagem exata
    alerta_erro = page.locator("[data-test='error']")
    expect(alerta_erro).to_be_visible()
    expect(alerta_erro).to_have_text("Epic sadface: Sorry, this user has been locked out.")
