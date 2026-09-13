# 🧹 Service Clean App

O **Service Clean** é um aplicativo desktop moderno desenvolvido em Python para conectar clientes a profissionais prestadores de serviços residenciais (como diaristas, eletricistas, pintores, jardineiros, entre outros). A interface foi construída com foco em usabilidade, segurança e agilidade.

---

## 🚀 Como Baixar e Executar o Aplicativo (Sem precisar de Python)

Se você quer apenas testar o aplicativo no seu computador Windows, siga estes passos simples:

1. Acesse a aba **[Releases](https://github.com)** no canto direito desta página.
2. Na versão mais recente, clique no arquivo **`main.zip`** dentro da seção *Assets* para fazer o download.
3. Após o término do download, extraia (descompacte) a pasta `.zip` em qualquer local do seu computador.
4. Abra a pasta extraída, localize o arquivo **`main.exe`** e dê um duplo clique para rodar o aplicativo!

---

## 🛠️ Funcionalidades Principais

* **Área do Cliente:** Cadastro simples e busca de profissionais filtrados por categorias de serviço.
* **Área do Profissional:** Tela dedicada de cadastro contendo especificações de Profissão, Bairro de Atendimento, Preço Estimado e Chave Pix.
* **Módulo de Pagamento:** Simulação completa de faturamento, cálculo de divisões de valores (split da plataforma) e geração de código Pix Copia e Cola.
* **Módulo de Compartilhamento:** Integração de envio de dados e convites diretamente para o WhatsApp do cliente ou prestador.
* **Segurança Robustecida:** Criptografia de senhas via hash `bcrypt` e rotinas de sanitização de entradas contra ataques maliciosos (SQL Injection).

---

## 💻 Tecnologias Utilizadas

* **Linguagem Principal:** Python 3
* **Interface Gráfica:** CustomTkinter (Visual escuro/claro responsivo e moderno)
* **Banco de Dados:** SQLite (Armazenamento local ágil estruturado via `database.py`)
* **Segurança:** Bcrypt (Geração de hashes seguros)
* **Empacotamento:** PyInstaller (Compilação para executável portátil)

---

## 📁 Estrutura de Arquivos do Projeto

* `main.py` — Inicialização do app, ciclo principal e gerenciamento da interface de login.
* `cadastro_profissional.py` — Módulo isolado da janela de registro de novos prestadores.
* `database.py` — Criação de tabelas, alimentação de sementes iniciais e consultas SQL.
* `seguranca.py` — Filtros de força de senha, sanitização de textos e criptografia.
* `pagamento.py` — Regras de split financeiro e mock-up de Pix Copia e Cola.
* `modulo_compartilhamento.py` — Formatação de links dinâmicos para a API do WhatsApp.
* `dados_profissionais.py` — Dicionários estruturados contendo dados de mock de bairros, avaliações e comentários.
*
