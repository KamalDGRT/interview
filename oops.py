'''
shortcut for commenting: Ctrl + /
    1. built in Keyboard
    2. Attached monitor
    3. Charging point
    4. Operating System
'''

"""
Note:
When both default and parameterized constructor is present in a class,
at the time of object creation, parameterized constructor is expected.
"""

integer_a = 1
name = "Kamal"
cgpa = 9.8

# How to create a function
def function_Name(a, b):
    print(a, b)
    return a + b


class Laptop:
    # Data members / property
    brand_name: str
    keyboard: bool
    monitor: float
    charging_point: bool
    operating_system: str

    # option 1 - using constructors

    def __init__(self):
        print("default constructor")
    
    # parameterised constructor
    def __init__(self, BrandName: str, Keyboard: bool, Monitor: float, ChargingPoint: bool, OperatingSystem: str):
        self.brand_name = BrandName
        self.keyboard = Keyboard
        self.monitor = Monitor
        self.charging_point = ChargingPoint
        self.operating_system = OperatingSystem

    # option 2 - using member functions

# asus_laptop = Laptop()
# asus_laptop.brand_name = "Asus"
# asus_laptop.keyboard = True
# asus_laptop.monitor = 15
# asus_laptop.charging_point = True
# asus_laptop.operating_system = "Windows"

# () - paranthesis
# {} - curly brackets / braces
# [] - square brackets
# <> - angular brackets
# ` - Tilde symbol
# * - asterik
# & - ampersand
# % - modulo
# ^ - bitwise operator

lenovo_laptop = Laptop("Lenovo", True, 13, True, "Linux")
print("Brand            : ", lenovo_laptop.brand_name)
print("Keyboard         : ", lenovo_laptop.keyboard)
print("Monitor          : ", lenovo_laptop.monitor)
print("Charging Point   : ", lenovo_laptop.charging_point)
print("Operating System : ", lenovo_laptop.operating_system)
