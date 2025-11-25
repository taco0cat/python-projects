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
| **01** | [**Caesar Cipher**](./01%20-%20Caesar_Cipher.py) | Encryption/Decryption tool that shifts letters by a fixed amount. | Cryptography, Strings, ASCII |
| **02** | [**RPG Character Builder**](./02%20-%20RPG%20Character.py) | Generates a character with stats (Strength, Intel, Charisma). | Classes, Object-Oriented Programming |
| **03** | [**Pin Extractor**](./03%20-%20Pin%20Extractor.py) | Decodes a hidden PIN using a word-length algorithm. | **Steganography**, List Indexing |
| **04** | [**Number Pattern Gen**](./04%20-%20Number%20Pattern%20Generator.py) | Generates mathematical number sequences. | Loops, Mathematical Logic |
| **05** | [**Medical Data Validator**](./05%20-%20Medical%20Data%20Validator.py) | Cleans and validates medical record formats. | Data Validation, Error Handling |
| **06** | [**ISBN Validator (Debug)**](./06%20-%20Debug%20-%20ISBN%20Validator) | A debugging challenge to fix an ISBN checker. | Debugging, Checksums |

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
    python "03 - Pin Extractor.py"
    ```

---

## 🧠 Key Concepts

### 🔐 Caesar Cipher
A classic substitution cipher. It is not cryptographically secure against modern brute-force attacks (since there are only 25 possible shifts), but it is excellent for understanding the basics of encryption algorithms.

### 🕵️ Pin Extractor (Steganography)
This script demonstrates a basic form of **Steganography**—hiding secret data inside ordinary text. It uses a specific algorithm (checking word lengths at specific line indexes) to reveal a hidden numerical code within a poem.

---

## 🛡️ License

This project is open source.
**Curriculum Source:** [FreeCodeCamp Python Certification (V9)](https://www.freecodecamp.org/learn/python-v9)

---
*Created by [taco0cat](https://github.com/taco0cat)*