import os
import re
import sys


def main():
    tainted_2 = sys.argv[1]
    tainted_3 = tainted_2

    if 1==0:

        # remove ||, &&, ;, &, and |
        pattern = '\|\||&&|[;&|]'
        tainted_3 = re.sub(pattern, '', tainted_2)


    #flaw
    os.system('ls ' + tainted_3)


if __name__ == '__main__':
        main()