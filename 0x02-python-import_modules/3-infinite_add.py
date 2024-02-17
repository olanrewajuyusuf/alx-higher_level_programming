#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg, res, i = sys.argv, 0, 1
    if len(arg) > i:
        while i <= len(arg)-1:
            res = res + int(arg[i])
            i = i + 1
        print("{}".format(res))
    else:
        print("{}".format(res))
