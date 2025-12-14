# 🐍 Python Projects & Scripts

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FreeCodeCamp](https://img.shields.io/badge/FreeCodeCamp-%23123.svg?style=for-the-badge&logo=freecodecamp&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/taco0cat/python-projects?style=for-the-badge&color=blue)

A collection of Python scripts and CLI tools developed as part of the **FreeCodeCamp Scientific Computing with Python** curriculum. This repository documents my progress in algorithms, data validation, and basic cryptography.

## 📋 Table of Contents

* [📂 Project List](#project-list)
* [⚙️ How to Run](#how-to-run)
* [🧠 Key Concepts](#key-concepts)
* [🛡️ License](#license)

---

## <a name="project-list"></a>📂 Project List

| ID | Project Name | Description | Key Concepts |
| :--- | :--- | :--- | :--- |
| **01** | [**Caesar Cipher**](./01%20-%20Caesar_Cipher.py) | Encryption tool that shifts letters by a fixed amount. | Cryptography, Strings |
| **02** | [**Pin Extractor**](./02%20-%20Pin%20Extractor.py) | Decodes a hidden PIN using a word-length algorithm. | Steganography, List Indexing |
| **03** | [**Vigenère Cipher**](./03%20-%20Vigenere%20Cipher.py) | Advanced encryption using a keyword-based shift. | Polyalphabetic Ciphers, Modulo |
| **04** | [**Luhn Algorithm**](./04%20-%20Luhn%20Algorithm%20-%20Card%20Verification.py) | Validates credit card numbers using the Luhn formula. | Checksums, Data Verification |
| **05** | [**Expense Tracker**](./05%20-%20Expense%20Tracker.py) | Tracks expenses using functional programming concepts. | Lambda Functions, Filtering |
| **06** | [**Snake Case Converter**](./06%20-%20Snake_Case_Converter.py) | Utility to convert PascalCase/CamelCase to snake_case. | String Manipulation, Regex |
| **07** | [**Square Root Calc**](./07%20-%20Square%20Root%20Calculator.py) | Calculates square roots without libraries. | Bisection Method, Algorithms |
| **08** | [**Password Generator**](./08%20-%20Password%20Generator%20using%20RegEx.py) | Generates strong passwords using Regex constraints. | Regex, Secrets Module |
| **Cert**| [**Arithmetic Formatter**](./Certification%20Project%201.py) | **(First Certification Project)** Formats arithmetic problems vertically. | String Formatting, Logic |

---

## <a name="how-to-run"></a>⚙️ How to Run

Ensure you have **Python 3.x** installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/taco0cat/python-projects.git](https://github.com/taco0cat/python-projects.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd python-projects
    ```
3.  **Run a script:**
    *Note: Use quotes if the filename has spaces.*
    ```bash
    python "08 - Password Generator using RegEx.py"
    ```

---

## <a name="key-concepts"></a>🧠 Key Concepts

### 🔐 Cryptography (Caesar & Vigenère)
Starting with the **Caesar Cipher** (simple substitution), I progressed to the **Vigenère Cipher**, which uses a keyword to create a polyalphabetic shift. This makes the encryption much stronger against frequency analysis attacks.

### 🛡️ Regular Expressions
The **Password Generator** uses the `secrets` module for cryptographically strong random selection, combined with **Regular Expressions (Regex)** to strictly enforce user-defined constraints (e.g., "must contain at least 2 special characters").

### 💳 Luhn Algorithm
Implemented the industry-standard **Luhn Algorithm** (Mod 10), used globally to validate identification numbers like credit cards and IMEI numbers. It demonstrates how real-world systems prevent accidental data entry errors.

### 📉 Bisection Method
The **Square Root Calculator** moves beyond simple math functions by implementing the **Bisection Method**, a root-finding method that repeatedly bisects an interval and then selects a sub-interval in which a root must lie.

### ⚡ Functional Programming
The **Expense Tracker** utilizes Python's functional programming features, specifically `lambda` functions, to handle data filtering and processing concisely.

---

## <a name="license"></a>🛡️ License

This project is open source.
**Curriculum Source:** [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

---
*Created by [taco0cat](https://github.com/taco0cat)*