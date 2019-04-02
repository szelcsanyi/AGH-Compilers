import sys

from tabulate import tabulate

from compiler import MScanner

if __name__ == '__main__':

    # open input file
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Cannot open {0} file".format(sys.argv[1]))
        sys.exit(0)

    # tokenize input
    tokens = MScanner().tokenize(file.read())

    # display
    print(tabulate(
        [(t.lineno, t.columnno, t.type, t.value) for t in tokens],
        headers=("row", "col", "type", "value"),
        tablefmt="fancy_grid"
    ))
