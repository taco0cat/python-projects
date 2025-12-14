# 🐍 Python Projects & Scripts

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FreeCodeCamp](https://img.shields.io/badge/FreeCodeCamp-%23123.svg?style=for-the-badge&logo=freecodecamp&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/taco0cat/python-projects?style=for-the-badge&color=blue)

A collection of Python scripts and CLI tools developed as part of the **FreeCodeCamp Scientific Computing with Python** curriculum. This repository documents my progress in algorithms, data validation, and basic cryptography.

## 📋 Table of Contents

* [📂 Project List](#-project-list)
* [⚙️ How to Run](#-how-to-run)
* [🧠 Key Concepts](#-key-concepts)
* [🛡️ License](#-license)

---

## 📂 Project List

| ID | Project Name | Description | Key Concepts |
| :--- | :--- | :--- | :--- |
| **01** | [**Caesar Cipher**](./01%20-%20Caesar_Cipher.py) | Encryption tool that shifts letters by a fixed amount. | Cryptography, Strings |
| **02** | [**RPG Character Builder**](./02%20-%20RPG%20Character.py) | Generates a character with stats (Strength, Intel, etc). | Classes, OOP |
| **03** | [**Pin Extractor**](./03%20-%20Pin%20Extractor.py) | Decodes a hidden PIN using a word-length algorithm. | Steganography, List Indexing |
| **04** | [**Number Pattern Gen**](./04%20-%20Number%20Pattern%20Generator.py) | Generates mathematical number sequences. | Loops, Math Logic |
| **05** | [**Medical Data Validator**](./05%20-%20Medical%20Data%20Validator.py) | Cleans and validates medical record formats. | Data Validation, Error Handling |
| **06** | [**ISBN Validator (Debug)**](./06%20-%20Debug%20-%20ISBN%20Validator.py) | A debugging challenge to fix an ISBN checker. | Debugging, Checksums |
| **07** | [**Vigenère Cipher**](./07%20-%20Vigenere%20Cipher.py) | Advanced encryption using a keyword-based shift. | Polyalphabetic Ciphers, Modulo |
| **08** | [**Luhn Algorithm**](./08%20-%20Luhn%20Algorithm%20-%20Card%20Verification.py) | Validates credit card numbers using the Luhn formula. | Checksums, Data Verification |
| **09** | [**Expense Tracker**](./09%20-%20Expense%20Tracker.py) | Tracks expenses using functional programming concepts. | Lambda Functions, Filtering |
| **10** | [**Snake Case Converter**](./10%20-%20Snake_Case_Converter.py) | Utility to convert PascalCase/CamelCase to snake_case. | String Manipulation, Regex |
| **11** | [**Square Root Calc**](./11%20-%20Square%20Root%20Calculator.py) | Calculates square roots without libraries. | Bisection Method, Algorithms |
| **Cert**| [**Arithmetic Formatter**](./Certification%20Project%201.py) | **(Certification)** Formats arithmetic problems vertically. | String Formatting, Logic |

---

## ⚙️ How to Run

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
    python "08 - Luhn Algorithm - Card Verification.py"
    ```

---

## 🧠 Key Concepts

### 🔐 Cryptography (Caesar & Vigenère)
Starting with the **Caesar Cipher** (simple substitution), I progressed to the **Vigenère Cipher**, which uses a keyword to create a polyalphabetic shift. This makes the encryption much stronger against frequency analysis attacks.

### 💳 Luhn Algorithm
Implemented the industry-standard **Luhn Algorithm** (Mod 10), used globally to validate identification numbers like credit cards and IMEI numbers. It demonstrates how real-world systems prevent accidental data entry errors.

### 📉 Bisection Method
The **Square Root Calculator** moves beyond simple math functions by implementing the **Bisection Method**, a root-finding method that repeatedly bisects an interval and then selects a sub-interval in which a root must lie.

### ⚡ Functional Programming
The **Expense Tracker** utilizes Python's functional programming features, specifically `lambda` functions, to handle data filtering and processing concisely.

---

## 🛡️ License

This project is open source.
**Curriculum Source:** [FreeCodeCamp Python Certification (V9)](https://www.freecodecamp.org/learn/python-v9)

---
*Created by [taco0cat](https://github.com/taco0cat)*