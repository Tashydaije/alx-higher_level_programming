#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argsCopy = sys.argv.copy()
    argsCount = len(argsCopy) - 1
    total = 0
    for i in range(argsCount):
        total += int(argsCopy[i + 1])

    print("{}".format(total))
