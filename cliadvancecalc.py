import math
import json
import os
from datetime import datetime

class AdvancedCalculatorCLI:
    def __init__(self):
        self.history = []
        self.exchange_rates = {
            'USD': 83.0,
            'EUR': 90.0,
            'GBP': 105.0,
            'JPY': 0.56,
            'CAD': 61.0,
            'AUD': 55.0,
            'CNY': 11.5,
            'INR': 1.0
        }
        self.load_history()
    
    def display_banner(self):
        """Display welcome banner"""
        print("\n" + "="*60)
        print("🚀 ADVANCED UNIVERSAL CALCULATOR (CLI)")
        print("="*60)
        print("📌 Type 'help' for commands, 'exit' to quit")
        print("="*60)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("📋 MAIN MENU")
        print("="*60)
        print("1. 🧮 Basic Calculator")
        print("2. 🔬 Scientific Calculator")
        print("3. 📏 Unit Converter")
        print("4. 🔢 Number System Converter")
        print("5. 📜 View History")
        print("6. 💰 Currency Exchange Rates")
        print("7. 🆘 Help")
        print("8. 🚪 Exit")
        print("="*60)
    
    def display_help(self):
        """Display help"""
        print("\n" + "="*60)
        print("🆘 HELP - COMMANDS GUIDE")
        print("="*60)
        print("\n📌 BASIC CALCULATOR:")
        print("   Enter expression like: 5+3, 10*2, (4+5)*3")
        print("   Operators: +, -, *, /, **, %")
        print("\n📌 SCIENTIFIC:")
        print("   sin(30), cos(45), tan(60)")
        print("   log(100), ln(10), sqrt(16)")
        print("   pi, e, factorial(5)")
        print("\n📌 UNIT CONVERTER:")
        print("   convert <value> <from_unit> <to_unit>")
        print("   Example: convert 100 cm ft")
        print("   Units: cm, m, km, ft, in, yd, mile")
        print("          g, kg, lb, oz, ton")
        print("          °C, °F, K")
        print("\n📌 NUMBER SYSTEM:")
        print("   conv <number> <from_system> <to_system>")
        print("   Example: conv 1010 binary decimal")
        print("   Systems: decimal, binary, octal, hex")
        print("\n📌 OTHER COMMANDS:")
        print("   history - Show calculation history")
        print("   clear - Clear history")
        print("   save - Save history to file")
        print("   rates - Show currency exchange rates")
        print("   exit - Exit program")
        print("="*60)
    
    # ========== BASIC CALCULATOR ==========
    def basic_calculator(self, expression):
        """Evaluate basic mathematical expression"""
        try:
            # Safe evaluation
            allowed = {'+', '-', '*', '/', '**', '%', '(', ')', ' '}
            if not all(c in allowed or c.isdigit() or c == '.' for c in expression):
                return "❌ Invalid characters in expression!"
            
            result = eval(expression)
            self.add_history(f"{expression} = {result}")
            return f"✅ Result: {result}"
        except ZeroDivisionError:
            return "❌ Error: Division by zero!"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    # ========== SCIENTIFIC CALCULATOR ==========
    def scientific_calculator(self, expression):
        """Evaluate scientific expressions"""
        try:
            # Replace function names
            expr = expression.lower().replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')
            expr = expr.replace('log', 'math.log10')
            expr = expr.replace('ln', 'math.log')
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('pi', str(math.pi))
            expr = expr.replace('e', str(math.e))
            
            # Factorial
            if 'factorial' in expr:
                import re
                match = re.search(r'factorial\((\d+)\)', expr)
                if match:
                    num = int(match.group(1))
                    result = math.factorial(num)
                    self.add_history(f"factorial({num}) = {result}")
                    return f"✅ Result: {result}"
            
            # Evaluate
            result = eval(expr)
            
            # Convert degrees to radians for trig functions
            if 'math.sin' in expr or 'math.cos' in expr or 'math.tan' in expr:
                # Already handled with math.radians?
                pass
            
            self.add_history(f"{expression} = {result}")
            return f"✅ Result: {result}"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    # ========== UNIT CONVERTER ==========
    def convert_units(self, value, from_unit, to_unit):
        """Convert between units"""
        try:
            value = float(value)
            result = value
            
            # Length conversions
            if from_unit in ['cm', 'm', 'km', 'ft', 'in', 'yd', 'mile']:
                # Convert to base unit (meters)
                if from_unit == 'cm':
                    result = value / 100
                elif from_unit == 'km':
                    result = value * 1000
                elif from_unit == 'ft':
                    result = value / 3.28084
                elif from_unit == 'in':
                    result = value / 39.3701
                elif from_unit == 'yd':
                    result = value / 1.09361
                elif from_unit == 'mile':
                    result = value * 1609.34
                
                # Convert from base to target
                if to_unit == 'cm':
                    result = result * 100
                elif to_unit == 'km':
                    result = result / 1000
                elif to_unit == 'ft':
                    result = result * 3.28084
                elif to_unit == 'in':
                    result = result * 39.3701
                elif to_unit == 'yd':
                    result = result * 1.09361
                elif to_unit == 'mile':
                    result = result / 1609.34
            
            # Weight conversions
            elif from_unit in ['g', 'kg', 'lb', 'oz', 'ton']:
                # Convert to base (kg)
                if from_unit == 'g':
                    result = value / 1000
                elif from_unit == 'lb':
                    result = value / 2.20462
                elif from_unit == 'oz':
                    result = value / 35.274
                elif from_unit == 'ton':
                    result = value * 1000
                
                if to_unit == 'g':
                    result = result * 1000
                elif to_unit == 'lb':
                    result = result * 2.20462
                elif to_unit == 'oz':
                    result = result * 35.274
                elif to_unit == 'ton':
                    result = result / 1000
            
            # Temperature conversions
            elif from_unit in ['°C', '°F', 'K']:
                if from_unit == '°C' and to_unit == '°F':
                    result = (value * 9/5) + 32
                elif from_unit == '°C' and to_unit == 'K':
                    result = value + 273.15
                elif from_unit == '°F' and to_unit == '°C':
                    result = (value - 32) * 5/9
                elif from_unit == '°F' and to_unit == 'K':
                    result = (value - 32) * 5/9 + 273.15
                elif from_unit == 'K' and to_unit == '°C':
                    result = value - 273.15
                elif from_unit == 'K' and to_unit == '°F':
                    result = (value - 273.15) * 9/5 + 32
            
            # Currency conversions
            elif from_unit in self.exchange_rates and to_unit in self.exchange_rates:
                inr_value = value * self.exchange_rates[from_unit]
                result = inr_value / self.exchange_rates[to_unit]
            
            else:
                return f"❌ Error: Invalid units! Use 'help' for list of units."
            
            message = f"✅ {value} {from_unit} = {result:.4f} {to_unit}"
            self.add_history(f"Converted: {value} {from_unit} → {result:.4f} {to_unit}")
            return message
            
        except ValueError:
            return "❌ Error: Please enter a valid number!"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    # ========== NUMBER SYSTEM CONVERTER ==========
    def convert_number_system(self, value, from_sys, to_sys):
        """Convert between number systems"""
        try:
            # Convert to decimal first
            if from_sys.lower() == 'decimal':
                decimal = int(value)
            elif from_sys.lower() == 'binary':
                decimal = int(value, 2)
            elif from_sys.lower() == 'octal':
                decimal = int(value, 8)
            elif from_sys.lower() == 'hex':
                decimal = int(value, 16)
            else:
                return f"❌ Error: Invalid system! Use: decimal, binary, octal, hex"
            
            # Convert from decimal to target
            if to_sys.lower() == 'decimal':
                result = str(decimal)
            elif to_sys.lower() == 'binary':
                result = bin(decimal)[2:]
            elif to_sys.lower() == 'octal':
                result = oct(decimal)[2:]
            elif to_sys.lower() == 'hex':
                result = hex(decimal)[2:].upper()
            else:
                return f"❌ Error: Invalid system! Use: decimal, binary, octal, hex"
            
            message = f"✅ {value} ({from_sys}) = {result} ({to_sys})"
            self.add_history(message)
            return message
            
        except ValueError:
            return f"❌ Error: Invalid number for {from_sys} system!"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    # ========== HISTORY FUNCTIONS ==========
    def add_history(self, entry):
        """Add entry to history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append(f"[{timestamp}] {entry}")
        if len(self.history) > 100:
            self.history.pop(0)
    
    def view_history(self):
        """Display history"""
        if not self.history:
            return "📭 No history yet!"
        
        print("\n" + "="*60)
        print("📜 CALCULATION HISTORY")
        print("="*60)
        for i, entry in enumerate(self.history, 1):
            print(f"{i:3}. {entry}")
        print("="*60)
        return ""
    
    def clear_history(self):
        """Clear history"""
        self.history = []
        return "🗑️ History cleared!"
    
    def save_history(self):
        """Save history to file"""
        try:
            filename = f"calculator_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            data = {
                'history': self.history,
                'timestamp': str(datetime.now())
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return f"✅ History saved to {filename}"
        except Exception as e:
            return f"❌ Error saving history: {str(e)}"
    
    def load_history(self):
        """Load history from file"""
        try:
            # Find latest history file
            files = [f for f in os.listdir('.') if f.startswith('calculator_history_') and f.endswith('.json')]
            if not files:
                return "📭 No history files found!"
            
            latest = sorted(files)[-1]
            with open(latest, 'r') as f:
                data = json.load(f)
                self.history = data.get('history', [])
            return f"✅ History loaded from {latest}"
        except Exception as e:
            return f"❌ Error loading history: {str(e)}"
    
    def show_rates(self):
        """Show exchange rates"""
        print("\n" + "="*60)
        print("💰 CURRENCY EXCHANGE RATES (1 USD = ?)")
        print("="*60)
        for currency, rate in self.exchange_rates.items():
            print(f"  1 USD = {rate:.2f} {currency}")
        print("="*60)
        return ""
    
    # ========== MAIN LOOP ==========
    def run(self):
        """Main program loop"""
        self.display_banner()
        
        while True:
            try:
                self.display_menu()
                choice = input("\n👉 Enter your choice (or command): ").strip()
                
                # ===== EXIT =====
                if choice in ['8', 'exit', 'quit']:
                    print("\n" + "="*60)
                    print("👋 Thank you for using Advanced Calculator!")
                    print(f"📊 Total calculations: {len(self.history)}")
                    print("="*60)
                    break
                
                # ===== HELP =====
                elif choice in ['7', 'help', '?']:
                    self.display_help()
                
                # ===== HISTORY =====
                elif choice in ['5', 'history']:
                    self.view_history()
                
                elif choice == 'clear':
                    print(self.clear_history())
                
                elif choice == 'save':
                    print(self.save_history())
                
                elif choice == 'load':
                    print(self.load_history())
                
                # ===== CURRENCY RATES =====
                elif choice in ['6', 'rates']:
                    self.show_rates()
                
                # ===== BASIC CALCULATOR =====
                elif choice == '1':
                    print("\n🧮 BASIC CALCULATOR")
                    print("Enter expression (e.g., 5+3, 10*2, (4+5)*3)")
                    expr = input("Expression: ")
                    print(self.basic_calculator(expr))
                
                # ===== SCIENTIFIC CALCULATOR =====
                elif choice == '2':
                    print("\n🔬 SCIENTIFIC CALCULATOR")
                    print("Functions: sin, cos, tan, log, ln, sqrt, factorial")
                    print("Constants: pi, e")
                    expr = input("Expression: ")
                    print(self.scientific_calculator(expr))
                
                # ===== UNIT CONVERTER =====
                elif choice == '3':
                    print("\n📏 UNIT CONVERTER")
                    print("Format: <value> <from_unit> <to_unit>")
                    print("Example: 100 cm ft")
                    print("Units: cm, m, km, ft, in, yd, mile")
                    print("       g, kg, lb, oz, ton")
                    print("       °C, °F, K")
                    inp = input("Convert: ").split()
                    if len(inp) == 3:
                        print(self.convert_units(inp[0], inp[1], inp[2]))
                    else:
                        print("❌ Invalid format! Use: <value> <from_unit> <to_unit>")
                
                # ===== NUMBER SYSTEM =====
                elif choice == '4':
                    print("\n🔢 NUMBER SYSTEM CONVERTER")
                    print("Format: <number> <from_system> <to_system>")
                    print("Example: 1010 binary decimal")
                    print("Systems: decimal, binary, octal, hex")
                    inp = input("Convert: ").split()
                    if len(inp) == 3:
                        print(self.convert_number_system(inp[0], inp[1], inp[2]))
                    else:
                        print("❌ Invalid format! Use: <number> <from_system> <to_system>")
                
                # ===== COMMAND PARSING =====
                elif choice.startswith('convert '):
                    parts = choice.split()
                    if len(parts) == 4:
                        print(self.convert_units(parts[1], parts[2], parts[3]))
                    else:
                        print("❌ Use: convert <value> <from_unit> <to_unit>")
                
                elif choice.startswith('conv '):
                    parts = choice.split()
                    if len(parts) == 4:
                        print(self.convert_number_system(parts[1], parts[2], parts[3]))
                    else:
                        print("❌ Use: conv <number> <from_system> <to_system>")
                
                else:
                    # Try as basic expression
                    if choice and not choice.isdigit():
                        result = self.basic_calculator(choice)
                        print(result)
                    else:
                        print("❌ Invalid choice! Type 'help' for commands.")
                
                # Prompt to continue
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting...")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

# ========== MAIN ==========
if __name__ == "__main__":
    app = AdvancedCalculatorCLI()
    app.run()