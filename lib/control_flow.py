#!/usr/bin/env python3


def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 > temperature > 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    str = ""
    if num % 3 == 0:
        str += "Fizz"
    if num % 5 == 0:
        str += "Buzz"
    if str == "":
        return num
    else:
        return str


def calculator(operation, num1, num2):
    calc_map = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2}
    result = calc_map.get(operation)
    if result == None:
        print("Invalid operation!")
        return result
    else:
        return result
