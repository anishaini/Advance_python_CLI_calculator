# 🖥️ Advanced Universal Calculator - CLI Version

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)
![CLI](https://img.shields.io/badge/CLI-Optimized-brightgreen.svg)
![Terminal](https://img.shields.io/badge/Terminal-Ready-black.svg)

**एक Powerful, Lightweight, All-in-One Command Line Calculator**

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Commands](#-commands-reference) • [Examples](#-examples)

</div>

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [📦 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage Guide](#-usage-guide)
- [🎯 Commands Reference](#-commands-reference)
- [📊 Examples](#-examples)
- [🔧 Customization](#-customization)
- [🐛 Troubleshooting](#-troubleshooting)
- [📄 License](#-license)

---

## 🌟 Features

### 🧮 **Basic Calculator**
- Addition, Subtraction, Multiplication, Division
- Parentheses support for complex expressions
- Percentage calculations
- Real-time expression evaluation
- Error handling for invalid inputs

### 🔬 **Scientific Calculator**
- **Trigonometric**: sin, cos, tan (degree mode)
- **Logarithmic**: log (base 10), ln (base e)
- **Power**: square, cube, power operations
- **Constants**: π (pi), e (Euler's number)
- **Factorial**: factorial(n)
- **Square Root**: sqrt(n)

### 📏 **Unit Converter**
- **Length**: cm, m, km, ft, in, yd, mile
- **Weight**: g, kg, lb, oz, ton
- **Temperature**: °C, °F, K
- **Currency**: USD, EUR, GBP, JPY, CAD, AUD, CNY, INR
- **Area**: m², km², ft², acre, hectare
- **Volume**: L, mL, gal, ft³, m³
- **Speed**: km/h, m/s, mph, ft/s

### 🔢 **Number System Converter**
- Decimal ↔ Binary
- Decimal ↔ Octal
- Decimal ↔ Hexadecimal
- Cross-system conversions (e.g., Binary → Hex)

### 💾 **History Management**
- Auto-saves all calculations with timestamps
- View complete calculation history
- Clear history
- Save history to JSON file
- Load history from JSON file
- Maximum 100 entries (configurable)

### 💰 **Currency Exchange**
- 8+ international currencies
- Configurable exchange rates
- Quick display of all rates

### 🎨 **User Experience**
- Color-coded output
- Interactive menu system
- Command shortcuts
- Help system
- Input validation
- Error handling

---

## 📦 Installation

### Prerequisites
```bash
Python 3.7 or higher

# Clone the repository
git clone https://github.com/yourusername/advanced-calculator-cli.git
cd advanced-calculator-cli

# No external dependencies required!
# Uses only Python built-in modules:
# - math
# - json
# - datetime
# - os

python calculator_cli.py

# Start the calculator
python calculator_cli.py

# You'll see:
🚀 ADVANCED UNIVERSAL CALCULATOR (CLI)
============================================================
📌 Type 'help' for commands, 'exit' to quit
============================================================

============================================================
📋 MAIN MENU
============================================================
1. 🧮 Basic Calculator
2. 🔬 Scientific Calculator
3. 📏 Unit Converter
4. 🔢 Number System Converter
5. 📜 View History
6. 💰 Currency Exchange Rates
7. 🆘 Help
8. 🚪 Exit
============================================================

👉 Enter your choice (or command):

👉 Enter your choice: 3

📏 UNIT CONVERTER
Format: <value> <from_unit> <to_unit>
Example: 100 cm ft
Units: cm, m, km, ft, in, yd, mile
       g, kg, lb, oz, ton
       °C, °F, K
Convert: 100 cm ft
✅ 100.0 cm = 3.2808 ft

👉 Enter your choice: convert 100 cm ft
✅ 100.0 cm = 3.2808 ft
