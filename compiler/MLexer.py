import ply.lex as lex


def MLexer():

    # operators
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"

    # dot operators
    t_DOT_PLUS = r"\.\+"
    t_DOT_MINUS = r"\.-"
    t_DOT_TIMES = r"\.\*"
    t_DOT_DIVIDE = r"\./"

    # comparators
    t_EQUALS = r"=="
    t_NOT_EQUALS = r"!="
    t_GREATER = r">"
    t_LESS = r"<"
    t_GREATER_EQUAL = r">="
    t_LESS_EQUAL = r"<="

    # assigns
    t_ASSIGN = r"="
    t_ASSIGN_PLUS = r"\+="
    t_ASSIGN_MINUS = r"-="
    t_ASSIGN_TIMES = r"\*="
    t_ASSIGN_DIVIDE = r"/="

    # symbols
    t_SEMICOLON = r";"
    t_COMMA = r","
    t_APOSTROPHE = r"'"
    t_COLON = r":"

    # brackets
    t_BRACKET_ROUND_L = r"\("
    t_BRACKET_ROUND_R = r"\)"
    t_BRACKET_SQUARE_L = r"\["
    t_BRACKET_SQUARE_R = r"\]"
    t_BRACKET_CURLY_L = r"{"
    t_BRACKET_CURLY_R = r"}"

    # reserved keywords
    reserved = {
        "if": "IF",
        "else": "ELSE",
        "for": "FOR",
        "while": "WHILE",
        "break": "BREAK",
        "continue": "CONTINUE",
        "return": "RETURN",
        "eye": "EYE",
        "zeros": "ZEROS",
        "ones": "ONES",
        "print": "PRINT"
    }

    # identifiers
    def t_ID(token):
        r"""[a-zA-Z_][a-zA-Z0-9_]*"""
        token.type = reserved.get(token.value, 'ID')  # Check for reserved words
        return token

    # strings
    def t_STRING(token):
        r"""\"(\\.|[^\"])*\""""
        token.value = token.value[1:-1].replace('\\"', '"')
        return token

    # float number
    def t_FLOAT(token):
        r"""((\d+\.\d*|\.\d+)([eE][-+]?\d+)?)|(\d+[eE][-+]?\d+)"""
        token.value = float(token.value)
        return token

    # int number
    def t_INT(token):
        r"""\d+"""
        token.value = int(token.value)
        return token

    # generate list of tokens
    tokens = list(map(lambda x: x[2:], filter(lambda x: x.startswith("t_"), dir()))) + list(reserved.values())

    # ignored input
    t_ignore = ' \t'
    t_ignore_COMMENT = r'\#.*'

    # new lines and line number handling
    def t_newline(token):
        r"""\n+"""
        token.lexer.lineno += len(token.value)

    # errors handling
    def t_error(token):
        raise LexerError(token)

    return lex.lex()


class LexerError(Exception):
    def __init__(self, token):
        super().__init__(f"Illegal character '{token.value[0]}' at line {token.lineno}")

        self.token = token
