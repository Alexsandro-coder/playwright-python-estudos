from playwright.sync_api import sync_playwright  # Importa a API síncrona para controlar o navegador


# Inicia o gerenciador do Playwright e encerra os processos automaticamente ao final
with sync_playwright() as p:
    # Abre uma instância do Chromium (headless=False exibe a janela; slow_mo=500 pausa 500ms entre ações)
    with p.chromium.launch(headless=False, slow_mo=500) as navegador:

        # Cria um contexto isolado (sessão, cookies e cache próprios, como uma janela anônima)
        with navegador.new_context() as contexto:
            # Cria uma aba isolada dentro desse contexto
            pagina = contexto.new_page()

            # Navega até a URL informada e aguarda o carregamento inicial da página
            pagina.goto("https://www.saucedemo.com")

            # Exemplos de outras estratégias de busca (dica: rode `playwright codegen URL` no terminal):
            # 1ª forma (CSS Selector por atributo): pagina.locator("[data-test='username']")
            # 2ª forma (Semântico pelo placeholder): pagina.get_by_placeholder("Username")

            # Localiza os campos pelo atributo data-test, preenche as credenciais e clica em Login
            pagina.locator("[data-test='username']").fill("standard_user")
            pagina.locator("[data-test='password']").fill("secret_sauce")
            pagina.locator("[data-test='login-button']").click()

            # Salva a URL atual da página após o redirecionamento
            url = pagina.url

            # Valida se a URL corresponde ao esperado; interrompe com AssertionError se divergir
            assert url == "https://www.saucedemo.com/inventory.html", f"URL inesperada: {url}"

            # Captura o texto visível do título da vitrine de produtos
            titulo = pagina.locator("[data-test='title']").inner_text()
            print(f"Login concluído! Título da página: {titulo}")

            # Valida se o título corresponde ao esperado
            assert titulo == "Products", f"Título inesperado: {titulo}"