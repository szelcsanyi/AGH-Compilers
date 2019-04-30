import sys

from ply import yacc

from compiler import MLexer
from compiler.AST import *


def MParser():

    # ==============================================
    #   PROGRAM
    # ==============================================
    def p_program_head(p):
        """ program : """
        p[0] = ProgramStatement(p.linespan(0), [])

    def p_program_tail(p):
        """ program : statement program """
        p[0] = ProgramStatement(p.linespan(0), [p[1]] + p[2].statements)

    # ==============================================
    #   STATEMENTS
    # ==============================================
    def p_statement_assignment(p):
        """ statement : variable ASSIGN expression SEMICOLON
        """
        p[0] = AssignmentStatement(p.linespan(0), p[1], p[3])

    def p_statement_assignment_with_operator(p):
        """ statement : variable ASSIGN_PLUS expression SEMICOLON
                      | variable ASSIGN_MINUS expression SEMICOLON
                      | variable ASSIGN_TIMES expression SEMICOLON
                      | variable ASSIGN_DIVIDE expression SEMICOLON
        """
        p[0] = AssignmentWithOperatorStatement(p.linespan(0), p[2], p[1], p[3])

    def p_statement_block(p):
        """ statement : BRACKET_CURLY_L program BRACKET_CURLY_R """
        p[0] = p[2]

    def p_statement_print(p):
        """ statement : PRINT comma_list SEMICOLON """
        p[0] = InstructionStatement(p.linespan(0), p[1], p[2])

    def p_statement_break(p):
        """ statement : BREAK SEMICOLON """
        p[0] = InstructionStatement(p.linespan(0), p[1], [])

    def p_statement_continue(p):
        """ statement : CONTINUE SEMICOLON """
        p[0] = InstructionStatement(p.linespan(0), p[1], [])

    def p_statement_return(p):
        """ statement : RETURN expression SEMICOLON """
        p[0] = InstructionStatement(p.linespan(0), p[1], p[2])

    def p_statement_while(p):
        """ statement : WHILE BRACKET_ROUND_L expression BRACKET_ROUND_R statement """
        p[0] = WhileStatement(p.linespan(0), p[3], p[5])

    def p_statement_for(p):
        """ statement : FOR ID ASSIGN range statement """
        p[0] = ForStatement(p.linespan(0), Identifier(p.linespan(0), p[2]), p[4], p[5])

    def p_statement_if(p):
        """ statement : IF BRACKET_ROUND_L expression BRACKET_ROUND_R statement %prec SIMPLE_IF
                      | IF BRACKET_ROUND_L expression BRACKET_ROUND_R statement ELSE statement
        """
        p[0] = IfStatement(p.linespan(0), p[3], p[5], p[7] if len(p) > 7 else None)

    # ==============================================
    #   EXPRESSIONS
    # ==============================================
    def p_expression_constant(p):
        """ expression : INT
                       | FLOAT
                       | STRING
        """
        p[0] = ConstantExpression(p.linespan(0), p[1])

    def p_expression_unary_minus(p):
        """ expression : MINUS expression %prec UNARY_MINUS """
        p[0] = UnaryMinusExpression(p.linespan(0), p[2])

    def p_expression_transpose(p):
        """ expression : expression APOSTROPHE """
        p[0] = TransposeExpression(p.linespan(0), p[1])

    def p_expression_binary_operator(p):
        """ expression : expression PLUS expression
                       | expression MINUS expression
                       | expression TIMES expression
                       | expression DIVIDE expression
                       | expression GREATER expression
                       | expression LESS expression
                       | expression GREATER_EQUAL expression
                       | expression LESS_EQUAL expression
        """
        p[0] = ScalarOperatorExpression(p.linespan(0), p[2], [p[1], p[3]])

    def p_expression_equal_operator(p):
        """ expression : expression EQUALS expression
                       | expression NOT_EQUALS expression
        """
        p[0] = EqualOperatorExpression(p.linespan(0), p[2], p[1], p[3])

    def p_expression_matrix_operator(p):
        """ expression : expression DOT_PLUS expression
                       | expression DOT_MINUS expression
                       | expression DOT_TIMES expression
                       | expression DOT_DIVIDE expression
        """
        p[0] = MatrixOperatorExpression(p.linespan(0), p[2], p[1], p[3])

    def p_expression_function(p):
        """ expression : function BRACKET_ROUND_L comma_list BRACKET_ROUND_R """
        p[0] = FunctionExpression(p.linespan(0), p[1], p[3])

    def p_expression_vector(p):
        """ expression : vector """
        p[0] = p[1]

    def p_expression_variable(p):
        """ expression : variable """
        p[0] = p[1]

    # ==============================================
    #   VARIABLES
    # ==============================================
    def p_variable_id(p):
        """ variable : ID """
        p[0] = Identifier(p.linespan(0), p[1])

    def p_variable_selector(p):
        """ variable : ID vector """
        p[0] = Selector(p.linespan(0), Identifier(p.linespan(1), p[1]), p[2])

    # ==============================================
    #   HELPERS
    # ==============================================
    def p_function(p):
        """ function : EYE
                     | ZEROS
                     | ONES
        """
        p[0] = p[1]

    def p_vector(p):
        """ vector : BRACKET_SQUARE_L comma_list BRACKET_SQUARE_R """
        p[0] = VectorExpression(p.linespan(0), p[2])

    def p_comma_list_head(p):
        """ comma_list : expression """
        p[0] = [p[1]]

    def p_comma_list(p):
        """ comma_list : comma_list COMMA expression  """
        p[0] = p[1] + [p[3]]

    def p_range(p):
        """ range : expression COLON expression """
        p[0] = RangeExpression(p.linespan(0), p[1], p[3])

    # ==============================================
    #   ERRORS
    # ==============================================
    def p_error(p):
        raise ParserError(p)

    # ==============================================
    #   PRECEDENCE
    # ==============================================
    precedence = (
        ("nonassoc", "SIMPLE_IF"),
        ("nonassoc", "ELSE"),
        ("nonassoc", "EQUALS", "NOT_EQUALS", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL"),
        ("left", "PLUS", "MINUS", "DOT_PLUS", "DOT_MINUS"),
        ("left", "TIMES", "DIVIDE", "DOT_TIMES", "DOT_DIVIDE"),
        ("right", "UNARY_MINUS"),
        ("left", "APOSTROPHE")
    )

    # ==============================================
    #   YACC SETUP
    # ==============================================
    lexer = MLexer()
    tokens = list(lexer.lextokens)
    start = "program"

    return yacc.yacc()


class ParserError(Exception):
    def __init__(self, production):
        if production:
            super().__init__(f"Unexpected token ({production.type}, '{production.value}') at line {production.lineno}")
        else:
            super().__init__("Unexpected end of input")

        self.production = production
