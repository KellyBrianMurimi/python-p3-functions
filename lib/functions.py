#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Kelly")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2
result = add(3, 5)
print(result)

def halve(number):
    return number / 2
result = halve(10)
