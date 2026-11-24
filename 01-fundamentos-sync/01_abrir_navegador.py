from playwright.sync_api import sync_playwright  # Importa a API síncrona para controlar o navegador


# Inicia o gerenciador do Playwright e encerra os processos automaticamente ao final
with sync_playwright() as p:
    # Abre uma instância do Chromium (headless=False exibe a janela; mude para True para rodar em segundo plano)
    with p.chromium.launch(headless=False) as navegador:
        # Cria uma aba isolada dentro do navegador
        pagina = navegador.new_page()

        # Navega até a URL informada e aguarda o carregamento inicial da página
        pagina.goto("https://www.saucedemo.com/")

        # Captura o texto definido na tag <title> do HTML da página
        titulo = pagina.title()
        print(f"Título carregado: {titulo}")

        # Valida se o título corresponde ao esperado; interrompe com AssertionError se divergir
        assert titulo == "Swag Labs", f"Título inesperado: {titulo}"