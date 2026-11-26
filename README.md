# Automação de Testes E2E com Playwright e Pytest

Repositório de estudos práticos de automação de testes End-to-End (E2E) utilizando **Python**, **Playwright** e **Pytest** sobre a aplicação de e-commerce [SauceDemo](https://www.saucedemo.com/). O projeto documenta a progressão técnica desde scripts lineares até uma suíte modular estruturada com **Page Object Model (POM)**, herança via `BasePage` e isolamento de estado com *fixtures*.

---

## Evolução do Projeto

O repositório está dividido em três fases progressivas de maturidade:

1. **`01-fundamentos/` — Scripts Iniciais e Navegação:**
   * Configuração do ambiente Playwright (Sync API).
   * Estratégias de localização de elementos (`data-test`, CSS selectors, roles).
   * Primeiras validações de estado e URL com `expect` e *auto-waiting* nativo.

2. **`02-pytest-estruturado/` — Organização de Suíte com Pytest:**
   * Migração de scripts isolados para funções de teste padronizadas (`test_*.py`).
   * Parametrização de cenários (`@pytest.mark.parametrize`) para cobertura de múltiplos perfis e validações de erro.
   * Uso de *fixtures* básicas para inicialização e encerramento do navegador.

3. **`03-boas-praticas-pom/` — Arquitetura Page Object Model (POM):**
   * Separação estrita entre mapeamento de elementos (`Locator`), ações de tela e asserções de teste (`expect`).
   * Implementação de **`BasePage`** para centralizar componentes compartilhados (`titulo` e `alerta_erro`), evitando duplicação sem criar um *God Object*.
   * Exposição limpa dos Page Objects através da fachada `pages/__init__.py` (`__all__`).
   * Injeção de pré-condições autenticadas por meio da *fixture* `pagina_logada` em `conftest.py`.

---

## Estrutura de Diretórios

```text
playwright-python-estudos/
├── 01-fundamentos/                # Scripts lineares, seletores e asserções básicas
├── 02-pytest-estruturado/         # Testes estruturados com Pytest e parametrização
├── 03-boas-praticas-pom/          # Arquitetura final em Page Object Model
│   ├── pages/
│   │   ├── __init__.py            # Fachada de exportação das classes de página
│   │   ├── base_page.py           # Classe base com locators comuns entre telas
│   │   ├── login_page.py          # Mapeamento e ações da tela de autenticação
│   │   ├── inventory_page.py      # Catálogo de produtos e navegação ao carrinho
│   │   ├── cart_page.py           # Conferência de itens e avanço ao checkout
│   │   └── checkout_page.py       # Preenchimento de entrega, resumo e conclusão
│   ├── conftest.py                # Fixtures de ciclo de vida e sessão autenticada
│   ├── test_01_login_pom.py       # Cenários de autenticação (sucesso e credenciais inválidas)
│   ├── test_02_carrinho_pom.py    # Cenários de adição e validação de itens no carrinho
│   └── test_03_checkout_pom.py    # Fluxo E2E completo de compra e validação de campos obrigatórios
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Cenários Automatizados (Fase 3 — POM)

| Arquivo de Teste | Caso de Teste | Objetivo da Validação |
| :--- | :--- | :--- |
| `test_01_login_pom.py` | `test_login_com_sucesso` | Autentica com `standard_user` e valida redirecionamento e título da página de inventário. |
| `test_01_login_pom.py` | `test_login_com_credenciais_invalidas` | Valida a exibição e a mensagem de erro para usuário bloqueado ou senha incorreta. |
| `test_02_carrinho_pom.py` | `test_adicionar_item_ao_carrinho` | Adiciona a *Sauce Labs Backpack* ao carrinho e verifica o contador e o item listado. |
| `test_02_carrinho_pom.py` | `test_remover_item_do_carrinho` | Garante a remoção de itens e a atualização imediata do estado do carrinho. |
| `test_03_checkout_pom.py` | `test_fluxo_checkout_completo` | Executa a jornada E2E completa: seleção de produto -> carrinho -> dados de entrega -> resumo -> confirmação de pedido. |
| `test_03_checkout_pom.py` | `test_checkout_sem_preencher_dados` | Tenta avançar no checkout sem preencher dados obrigatórios e valida o alerta `"Error: First Name is required"`. |

---

## Pré-requisitos e Instalação

* **Python 3.10+** instalado na máquina.
* **Git** para clonar o repositório.

### Passo a passo

1. **Clone o repositório e acesse a pasta do projeto:**

```bash
git clone [https://github.com/alexsandro-coder/playwright-python-estudos.git](https://github.com/alexsandro-coder/playwright-python-estudos.git)
cd playwright-python-estudos
```

2. **Crie e ative o ambiente virtual (`.venv`):**

* **Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

* **Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências e os binários dos navegadores do Playwright:**

```bash
pip install -r requirements.txt
playwright install
```

---

## Como Executar os Testes

* **Executar toda a suíte em Page Object Model (modo headless):**

```bash
python -m pytest 03-boas-praticas-pom/
```

* **Executar acompanhando no navegador (modo visual com câmera lenta):**

```bash
python -m pytest 03-boas-praticas-pom/ --headed --slowmo 300
```

* **Executar apenas o fluxo de checkout:**

```bash
python -m pytest 03-boas-praticas-pom/test_03_checkout_pom.py -v
```

---

## Autor

Desenvolvido por **Alex Sandro Rodrigues Nobre Junior** — [GitHub](https://github.com/alexsandro-coder)