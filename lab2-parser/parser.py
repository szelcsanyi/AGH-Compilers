import scanner
import ply.yacc as yacc


# ==============================================
#   PRECEDENCE
# ==============================================
precedence = (
    ("nonassoc", "IF"),
    ("nonassoc", "EQUALS", "NOT_EQUALS", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL"),
    ("left", "PLUS", "MINUS", "DOT_PLUS", "DOT_MINUS"),
    ("left", "TIMES", "DIVIDE", "DOT_TIMES", "DOT_DIVIDE"),
    ("right", "UNARY_MINUS"),
    ("nonassoc", "APOSTROPHE")
)


# ==============================================
#   HELPERS
# ==============================================
def p_comma_list(p):
    """ comma_list : expression
                   | comma_list COMMA expression
    """


# ==============================================
#   TERMINALS
# ==============================================
def p_terminal_constant(p):
    """ terminal : INT
                 | FLOAT
                 | STRING
    """


def p_terminal_id(p):
    """ terminal : ID """


def p_function(p):
    """ function : EYE
                 | ZEROS
                 | ONES
    """


# ==============================================
#   EXPRESSIONS
# ==============================================
def p_expression_terminal(p):
    """ expression : terminal """


def p_expression_left_unary_operator(p):
    """ expression : MINUS expression %prec UNARY_MINUS """


def p_expression_right_unary_operator(p):
    """ expression : expression APOSTROPHE """


def p_expression_binary_operator(p):
    """ expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression DOT_PLUS expression
                   | expression DOT_MINUS expression
                   | expression DOT_TIMES expression
                   | expression DOT_DIVIDE expression
    """


def p_expression_comparator(p):
    """ expression : expression EQUALS expression
                   | expression NOT_EQUALS expression
                   | expression GREATER expression
                   | expression LESS expression
                   | expression GREATER_EQUAL expression
                   | expression LESS_EQUAL expression
    """


def p_expression_function(p):
    """ expression : function BRACKET_ROUND_L comma_list BRACKET_ROUND_R
    """


def p_expression_matrix(p):
    """ expression : BRACKET_SQUARE_L matrix_body BRACKET_SQUARE_R """


def p_expression_matrix_body(p):
    """ matrix_body : comma_list
                    | matrix_body SEMICOLON comma_list
    """


def p_expression_assignment(p):
    """ expression : ID ASSIGN expression
                   | ID ASSIGN_PLUS expression
                   | ID ASSIGN_MINUS expression
                   | ID ASSIGN_TIMES expression
                   | ID ASSIGN_DIVIDE expression
    """


# ==============================================
#   STATEMENTS
# ==============================================
def p_statement_expression(p):
    """ statement : expression SEMICOLON """


def p_statement_block(p):
    """ statement : BRACKET_CURLY_L program BRACKET_CURLY_R
                  | BRACKET_CURLY_L BRACKET_CURLY_R
    """


def p_statement_print(p):
    """ statement : PRINT comma_list SEMICOLON """


def p_statement_break(p):
    """ statement : BREAK SEMICOLON """


def p_statement_continue(p):
    """ statement : CONTINUE SEMICOLON """


def p_statement_return(p):
    """ statement : RETURN expression SEMICOLON """


def p_statement_while(p):
    """ statement : WHILE BRACKET_ROUND_L expression BRACKET_ROUND_R statement """


def p_statement_for(p):
    """ statement : FOR ID ASSIGN expression COLON expression statement """


def p_statement_if(p):
    """ statement : if_else_if
                  | if_else_if ELSE statement
    """


def p_if_else_if(p):
    """ if_else_if : if
                   | if_else_if ELSE if
    """


def p_if(p):
    """ if : IF BRACKET_ROUND_L expression BRACKET_ROUND_R statement %prec IF """


# ==============================================
#   ERRORS
# ==============================================
def p_error(p):
    if p:
        print(f'Syntax error at line {p.lineno}? - LexToken({p.type}, \'{p.value}\')')
    else:
        print("Unexpected end of input")


# ==============================================
#   PROGRAM
# ==============================================
def p_program(p):
    """ program : statement
                | program statement
    """


# construct parser
tokens = scanner.tokens
start = "program"
parser = yacc.yacc()


# ==== HELPER FUNCTIONS ==== #

def parse(text):
    parser.parse(text, lexer=scanner.lexer)

