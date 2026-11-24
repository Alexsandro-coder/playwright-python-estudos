from playwright.sync_api import sync_playwright  # Importa a API síncrona para controlar o navegador


# Inicia o gerenciador do Playwright e encerra os processos automaticamente ao final
with sync_playwright() as p:
    # Abre uma instância do Chromium (headless=False exibe a janela; slow_mo=500 pausa 500ms entre ações)
    with p.chromium.launch(headless=False, slow_mo=500) as navegador:

        # Cria um contexto isolado (sessão, cookies e cache próprios)
        with navegador.new_context() as contexto:
            # Cria uma aba isolada dentro desse contexto
            pagina = contexto.new_page()

            # Navega até a página de login do SauceDemo
            pagina.goto("https://www.saucedemo.com")

            # Tenta logar com o usuário bloqueado propositalmente pelo sistema
            pagina.locator("[data-test='username']").fill("locked_out_user")
            pagina.locator("[data-test='password']").fill("secret_sauce")
            pagina.locator("[data-test='login-button']").click()

            # Guarda o localizador da caixa de erro em uma variável para reutilização
            alerta_erro = pagina.locator("[data-test='error']")

            # Exige que o alerta esteja visível (se falhar aqui, evita um falso positivo)
            assert alerta_erro.is_visible(), "A mensagem de erro não apareceu na tela!"

            # Salva uma captura de tela inteira como evidência visual do bloqueio
            pagina.screenshot(path="evidencias/evidencia_erro_login.png", full_page=True)

            # Lê o texto do alerta apenas uma vez e armazena na variável
            texto_erro = alerta_erro.inner_text()
            print(f"Mensagem capturada: {texto_erro}")

            # Valida se o texto exibido corresponde exatamente ao esperado
            assert texto_erro == "Epic sadface: Sorry, this user has been locked out.", (
                f"Alerta inesperado: {texto_erro}"
            )