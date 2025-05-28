# 🏦 Python Banking System – OOP Version

🚀 **This project** is a continuation of the DIO Python bootcamp, now refactored to use Object-Oriented Programming (OOP). The system now features a more scalable and maintainable architecture using classes, inheritance, abstraction, and polymorphism.

---

## 📖 Project Overview

This banking system simulates real-world operations and now supports:

- ✅ **Deposits** 💰  
- ✅ **Withdrawals** 💸  
- ✅ **Transaction history (statement)** 📜  
- ✅ **Client registration** 👤  
- ✅ **Bank account creation** 🏦  
- ✅ **Listing all accounts** 📋  

With the transition to an OOP architecture, the code is now cleaner, more modular, and ready for further expansions such as savings accounts, credit functionality, and more.

---

## 🧠 Key Concepts Used

- 📦 **Encapsulation** through class attributes and methods  
- 🧬 **Inheritance** (e.g., `PessoaFisica` extends `Cliente`)  
- 🧩 **Polymorphism** and method overriding in `ContaCorrente`  
- 🧱 **Abstraction** using abstract base classes (`Transacao`)  
- 📚 **Composition** between `Conta`, `Cliente`, and `Historico`

---

## 🛠️ Technologies Used

- 🐍 **Python 3.x**
- 🏗️ OOP (Object-Oriented Programming)
- 🧪 Use of abstract base classes (`abc`)
- 🕒 **Datetime** for transaction logging
- 📄 CLI Interface with `textwrap`

---

## 📌 Main Functionalities

### 💳 Banking Operations

- **Deposit**  
  - Only accepts positive amounts.
  - Automatically updates balance and logs the transaction.

- **Withdraw**  
  - Applies daily withdrawal limits and maximum withdrawal amount.
  - Records successful transactions.

- **Statement**  
  - Shows a list of all transactions and current balance.

### 👥 Client and Account Management

- **Register Client**  
  - Requires full name, CPF, date of birth, and address.
  - CPF must be unique.

- **Open Account**  
  - Creates a `ContaCorrente` associated with an existing client.
  - Accounts belong to a fixed agency (`0001`) and have unique numbers.

- **List Accounts**  
  - Displays all accounts with agency number, account number, and client name.

---

## 🗂️ Code Structure

The application is structured around the following main classes:

- `Cliente` and `PessoaFisica`
- `Conta` and `ContaCorrente`
- `Transacao` (abstract), `Saque`, and `Deposito`
- `Historico` to track transactions

The `main()` function acts as the CLI controller, handling user interaction and coordinating system operations.

---

💡 **Best Practices Highlighted:**

- OOP principles applied cleanly and correctly
- Clear separation of concerns between business logic and interface
- Scalability for future feature implementations

---

🔗 **Repository**: [GitHub - Python OOP Banking System](https://github.com/lucassiqueiraa/DesafioSistemaBancario)
