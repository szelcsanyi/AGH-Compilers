import sys

from compiler import MParser, MLexer, TypeChecker

if __name__ == '__main__':

    # open input file
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Cannot open {0} file".format(sys.argv[1]))
        sys.exit(0)

    # load input
    text = file.read()

    # parse
    parser = MParser()
    root = parser.parse(text, lexer=MLexer(), tracking=True)

    # check types
    checker = TypeChecker()
    checker.check(root)
    checker.print_errors()
