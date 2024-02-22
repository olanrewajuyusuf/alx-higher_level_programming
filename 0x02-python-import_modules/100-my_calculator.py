#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg = sys.argv
    if len(arg) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif arg[2] == "+":
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], add(int(arg[1]),int(arg[3]))))
        sys.exit(0)
    elif arg[2] == "-":
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], sub(int(arg[1]),int(arg[3]))))
        sys.exit(0)
    elif arg[2] == "*":
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], mul(int(arg[1]),int(arg[3]))))
        sys.exit(0)
    elif arg[2] == "/":
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], div(int(arg[1]),int(arg[3]))))
        sys.exit(0)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
