Aqui está o README atualizado para refletir as mudanças feitas no código:  

---

# 📌 Sistema Bancário com Python  

🚀 **Este projeto** faz parte da trilha de formação em Python da DIO e evoluiu para um sistema bancário mais completo e modularizado. Além das funcionalidades básicas de depósito, saque e extrato, agora o sistema permite a criação de usuários e contas bancárias, reforçando conceitos de programação estruturada e boas práticas em desenvolvimento de software.  

## 📖 Sobre o Projeto  

Este sistema bancário simula operações reais, permitindo aos usuários:  

- ✅ **Depósito** 💰  
- ✅ **Saque** 💸  
- ✅ **Exibição de extrato** 📜  
- ✅ **Cadastro de novos usuários** 👤  
- ✅ **Criação de contas bancárias** 🏦  
- ✅ **Listagem de contas criadas** 📋  

Com essa evolução, o projeto agora adota uma estrutura modularizada, tornando o código mais organizado, reutilizável e escalável.  

## 🛠️ Tecnologias Utilizadas  

- ✔️ **Python 3**  
- ✔️ **Uso de funções para modularização do código**  
- ✔️ **Manipulação de listas e dicionários para armazenar usuários e contas**  

## 📌 Funcionalidades  

### **🏦 Operações Bancárias**  
- **Depósito:** O usuário informa o valor e ele é adicionado ao saldo.  
- **Saque:** O usuário pode sacar um valor respeitando as seguintes regras:  
  - Não pode ultrapassar o saldo disponível;  
  - Não pode exceder o limite de saque por transação;  
  - Há um limite máximo de saques diários.  
- **Extrato:** Exibe todas as transações realizadas e o saldo atual.  

### **👥 Gestão de Usuários e Contas**  
- **Criar Usuário:** Permite cadastrar um novo usuário no sistema utilizando CPF como identificador único.  
- **Criar Conta Bancária:** Associa uma nova conta a um usuário existente. Cada conta pertence a uma agência fixa e possui um número único.  
- **Listar Contas:** Exibe todas as contas criadas, mostrando agência, número da conta e titular.  

## 📌 Estrutura do Código  

O código agora é organizado em funções para cada operação, facilitando a manutenção e a leitura. Algumas melhorias incluem:  

- **Uso de funções separadas** (`depositar()`, `sacar()`, `exibir_extrato()`, etc.).  
- **Parâmetros posicionais e nomeados**, garantindo maior clareza na chamada das funções.  
- **Armazenamento de usuários e contas em listas**, simulando um banco de dados simples.  

---

💡 **Boas Práticas:** Esta refatoração torna o sistema mais robusto e modularizado, sendo uma ótima base para quem deseja aprender sobre gerenciamento de transações bancárias e manipulação de dados em Python.  

🔗 **Link para o repositório**: [GitHub - Sistema Bancário Python](https://github.com/lucassiqueiraa/DesafioSistemaBancario)  

---

Esse novo README reflete as mudanças feitas no código, destacando a modularização e as novas funcionalidades. 🚀