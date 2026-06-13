# Password Strength Checker

## Overview

Password Strength Checker is a Python-based application that evaluates the strength of a password based on multiple security criteria. The project features a simple graphical user interface (GUI) built using Tkinter, allowing users to enter a password and instantly receive feedback on its strength.

## Features

* Checks password length
* Verifies the presence of uppercase letters
* Verifies the presence of lowercase letters
* Verifies the presence of digits
* Verifies the presence of special characters
* Detects unsupported characters
* Classifies passwords as Weak, Medium, Strong, or Very Strong
* Provides detailed feedback on missing password requirements
* Show/Hide Password functionality
* User-friendly Tkinter GUI

## Technologies Used

* Python
* Tkinter

## How It Works

The application evaluates the password using the following criteria:

1. Minimum length of 8 characters
2. Presence of at least one uppercase letter
3. Presence of at least one lowercase letter
4. Presence of at least one digit
5. Presence of at least one special character
6. Additional score for passwords with 12 or more characters

Based on the score obtained, the password is categorized as:

* Weak
* Medium
* Strong
* Very Strong

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the Python file:
   python gui.py
4. Enter a password in the GUI.
5. Click "Check Strength" to view the result.


## Author

Nandini Malge
