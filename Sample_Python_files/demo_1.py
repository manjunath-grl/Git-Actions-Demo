"""Module providing a function printing python version."""
import sys


def print_python_version():
    print(sys.version)

print("Hello, User")

class Calculator:
    def squ(a):
        return a*a

provided_Num = input("Please enter any integer: ")

print(Calculator.squ(int(provided_Num)))
print_python_version()
