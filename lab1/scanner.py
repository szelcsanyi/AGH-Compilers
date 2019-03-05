import ply.lex as lex

# operators
t_PLUS              = r"\+"
t_MINUS             = r"-"
t_TIMES             = r"\*"
t_DIVIDE            = r"/"

# dot operators
t_DOT_PLUS          = r"\.\+"
t_DOT_MINUS         = r"\.-"
t_DOT_TIMES         = r"\.\*"
t_DOT_DIVIDE        = r"\./"

# comparators
t_EQUALS            = r"=="
t_NOT_EQUALS        = r"!="
t_GREATER           = r">"
t_LESS              = r"<"
t_GREATER_EQUAL     = r">="
t_LESS_EQUAL        = r"<="

# assigns
t_ASSIGN            = r"="
t_ASSIGN_PLUS       = r"\+="
t_ASSIGN_MINUS      = r"-="
t_ASSIGN_TIMES      = r"\*="
t_ASSIGN_DIVIDE     = r"/="

# symbols
t_SEMICOLON         = r";"
t_COMMA             = r","
t_APOSTROPHE        = r"'"
t_COLON             = r":"

# brackets
t_BRACKET_ROUND_L   = r"\("
t_BRACKET_ROUND_R   = r"\)"
t_BRACKET_SQUARE_L  = r"\["
t_BRACKET_SQUARE_R  = r"\]"
t_BRACKET_CURLY_L   = r"{"
t_BRACKET_CURLY_R   = r"}"

# reserved keywords
reserved = {
    "if":       "IF",
    "else":     "ELSE",
    "for":      "FOR",
    "while":    "WHILE",
    "break":    "BREAK",
    "continue": "CONTINUE",
    "return":   "RETURN",
    "eye":      "EYE",
    "zeros":    "ZEROS",
    "ones":     "ONES",
    "print":    "PRINT"
}

# comments
def t_COMMENT(t):
    r'\#.*'
    pass

# identifier
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# string
def t_STRING(t):
    r'"([^"\n]|(\\"))*"'
    t.value = t.value[1:-1]
    return t

# numbers
def t_FLOAT(t):
    r"(\d+\.\d*|\.\d+|\d+[eE][+-]?\d+)"
    t.value = float(t.value)
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

# generate list of tokens
tokens = list(map(lambda x: x[2:], filter(lambda x: x.startswith("t_"), dir()))) + list(reserved.values())

# ignored
t_ignore  = ' \t'

# new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# errors
def t_error(t) :
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# construct lexer
lexer = lex.lex()



### HELPER FUNCTIONS ###

# function for getting columnno
def find_column(input, token):
    return token.lexpos - input.rfind('\n', 0, token.lexpos)

# function for tokenizing
def tokenize(input):
    tokens = []
    lexer.input(input)
    while True:
        t = lexer.token()
        if not t:
            break
        tokens.append(t)
    return tokens