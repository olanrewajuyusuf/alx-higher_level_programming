#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    i = 1
    if len(arg) > 1:
        if len(arg) == 1:
            print("{} argument:".format(len(arg)-1))
        else:
            print("{} arguments:".format(len(arg)-1))
        while i <= len(arg)-1:
            print("{}: {}".format(i, arg[i]))
            i = i + 1
    else:
        print("0 arguments.")
