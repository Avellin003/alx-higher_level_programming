#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    operators = ["+", "-", "/", "*"]
    for i in operators:
        if (argv != operator[i]):
            print("Unknown operator. Available operators: +, -, * and /")
