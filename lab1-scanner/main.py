import sys
import scanner
from tabulate import tabulate

if __name__ == '__main__':

    # open input file
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Cannot open {0} file".format(sys.argv[1]))
        sys.exit(0)

    # load input
    text = file.read()

    # tokenize
    tokens = scanner.tokenize(text)

    # display
    print(tabulate(
        [(t.lineno, scanner.find_column(text, t), t.type, t.value) for t in tokens],
        headers=("row", "col", "type", "value"),
        tablefmt="fancy_grid"
    ))
