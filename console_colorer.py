import os
import sys


def printRed(mess):
    os.system("")
    sys.stdout.write("\033[31m")
    sys.stdout.write(mess)
    sys.stdout.write("\033[0m")
