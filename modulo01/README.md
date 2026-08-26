# 🍞 Sistema de Vendas - Padaria (CLI)

> Um sistema interativo desenvolvido em Python com interface de Linha de Comando (CLI) para gerenciamento de estoque, cadastro e vendas de produtos de uma padaria.

---

## 📋 Visão Geral do Projeto

Este projeto foi desenvolvido com o objetivo de criar uma solução prática e eficiente para o gerenciamento de uma padaria, permitindo que o negócio controle seus produtos e realize vendas de forma automatizada pelo terminal.

### 👥 Visão dos Stakeholders e Personas (User Stories)

* **PD (Product Owner / Dono do Negócio):**
> *"Eu quero criar um sistema de vendas para a padaria, para que os clientes possam comprar nossos produtos online e para que eu consiga controlar as vendas e os produtos disponíveis."*


* **QA (Qualidade / Cliente):**
> *"Eu quero poder ter facilidade para comprar os produtos da padaria online, para que eu possa economizar tempo e evitar filas."*


* **Tech (Programador / Aprendizado):**
> *"Eu quero criar um sistema de vendas para que eu possa desenvolver minhas habilidades de programação e criar um projeto útil para a padaria."*


* **Dev (Desenvolvedor Backend):**
> *"Eu quero um sistema de vendas para a padaria para que eu possa implementar as funcionalidades necessárias, como cadastro de produtos, gerenciamento de estoque e processamento de pedidos, utilizando as melhores práticas de desenvolvimento de software."*


* **UX (Designer de Experiência do Usuário):**
> *"Eu quero um sistema de vendas para a padaria para que eu possa criar uma interface intuitiva e agradável para os clientes, facilitando a navegação e a realização de compras online."*


* **IA (Análise de Dados):**
> *"Eu quero um sistema de vendas para a padaria para que eu possa coletar e analisar os dados de vendas, identificar padrões de compra e fornecer insights para melhorar as estratégias de marketing e vendas da padaria."*



---

## ⚙️ Arquitetura e Especificações Técnicas

* **Tipo de Aplicação:** Sistema **CLI (Command Line Interface)** — roda inteiramente via terminal, sem necessidade de interface gráfica complexa.
* **Linguagem:** Python 3
* **Estrutura de Dados:** Armazenamento estático baseado em vagas de memória dedicadas para gerenciar até 5 produtos iniciais e dinâmicos (`p1_nome`, `p2_nome`, etc.).

---

## 🚀 Funcionalidades Principais

O sistema conta com um menu interativo completo acessível via terminal (`0` a `9`):

1. **Cadastrar Produto:** Permite registrar novos itens informando nome, descrição, validade, estoque e preço.
2. **Listar Produtos:** Exibe todos os produtos cadastrados no sistema com detalhes de preço, estoque e validade.
3. **Excluir Produto:** Remove um produto do estoque liberando sua respectiva vaga no sistema.
4. **Pesquisar Produto:** Realiza buscas rápidas por nome para verificar a disponibilidade e detalhes no estoque.
5. **Realizar Venda:** Processa a venda de produtos, abatendo automaticamente o estoque e calculando o valor total.
6. **Suporte ao Cliente (SAC):** Exibe os canais de atendimento e centrais de ajuda da padaria.
7. **Cancelar Venda (Estorno):** Permite estornar a última venda realizada, devolvendo os itens ao estoque.
8. **Relatório Técnico / Caixa:** Mostra o total de itens gerais em estoque e a última movimentação financeira.
9. **Informações do Desenvolvedor:** Exibe os dados sobre a versão e arquitetura do sistema.
10. **Sair:** Encerra a execução do programa.

---

## 🛠️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou copie o código fonte principal do sistema (ex: `padaria.py`).
3. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS) na pasta onde o arquivo está salvo.
4. Execute o comando:
```bash
python padaria.py

```



---

## 📦 Produtos Pré-Cadastrados no Sistema

O sistema já inicializa com alguns itens padrão para teste imediato:

* **Pão Francês** (R$ 1,50)
* **Croissant** de queijo (R$ 8,00)
* **Sonho** recheado com creme (R$ 6,00)
* **Café** Expresso 300ml (R$ 10,00)
* **Suco de Laranja** natural 300ml (R$ 10,00)