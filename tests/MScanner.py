import unittest

from compiler import MScanner, LexerError


class TestMScanner(unittest.TestCase):
    
    def setUp(self):
        self.scanner = MScanner()
    
    def test_symbols(self):
        tokens = self.scanner.tokenize("+-*/.+.-.*./==!=><>=<==+=-=*=/=;,':()[]{}")
        
        self.assertEqual(len(tokens), 29)
        
        self.assertEqual(tokens[0].type, 'PLUS')
        self.assertEqual(tokens[1].type, 'MINUS')
        self.assertEqual(tokens[2].type, 'TIMES')
        self.assertEqual(tokens[3].type, 'DIVIDE')
        self.assertEqual(tokens[4].type, 'DOT_PLUS')
        self.assertEqual(tokens[5].type, 'DOT_MINUS')
        self.assertEqual(tokens[6].type, 'DOT_TIMES')
        self.assertEqual(tokens[7].type, 'DOT_DIVIDE')
        self.assertEqual(tokens[8].type, 'EQUALS')
        self.assertEqual(tokens[9].type, 'NOT_EQUALS')
        self.assertEqual(tokens[10].type, 'GREATER')
        self.assertEqual(tokens[11].type, 'LESS')
        self.assertEqual(tokens[12].type, 'GREATER_EQUAL')
        self.assertEqual(tokens[13].type, 'LESS_EQUAL')
        self.assertEqual(tokens[14].type, 'ASSIGN')
        self.assertEqual(tokens[15].type, 'ASSIGN_PLUS')
        self.assertEqual(tokens[16].type, 'ASSIGN_MINUS')
        self.assertEqual(tokens[17].type, 'ASSIGN_TIMES')
        self.assertEqual(tokens[18].type, 'ASSIGN_DIVIDE')
        self.assertEqual(tokens[19].type, 'SEMICOLON')
        self.assertEqual(tokens[20].type, 'COMMA')
        self.assertEqual(tokens[21].type, 'APOSTROPHE')
        self.assertEqual(tokens[22].type, 'COLON')
        self.assertEqual(tokens[23].type, 'BRACKET_ROUND_L')
        self.assertEqual(tokens[24].type, 'BRACKET_ROUND_R')
        self.assertEqual(tokens[25].type, 'BRACKET_SQUARE_L')
        self.assertEqual(tokens[26].type, 'BRACKET_SQUARE_R')
        self.assertEqual(tokens[27].type, 'BRACKET_CURLY_L')
        self.assertEqual(tokens[28].type, 'BRACKET_CURLY_R')

        self.assertEqual(tokens[0].value, '+')
        self.assertEqual(tokens[1].value, '-')
        self.assertEqual(tokens[2].value, '*')
        self.assertEqual(tokens[3].value, '/')
        self.assertEqual(tokens[4].value, '.+')
        self.assertEqual(tokens[5].value, '.-')
        self.assertEqual(tokens[6].value, '.*')
        self.assertEqual(tokens[7].value, './')
        self.assertEqual(tokens[8].value, '==')
        self.assertEqual(tokens[9].value, '!=')
        self.assertEqual(tokens[10].value, '>')
        self.assertEqual(tokens[11].value, '<')
        self.assertEqual(tokens[12].value, '>=')
        self.assertEqual(tokens[13].value, '<=')
        self.assertEqual(tokens[14].value, '=')
        self.assertEqual(tokens[15].value, '+=')
        self.assertEqual(tokens[16].value, '-=')
        self.assertEqual(tokens[17].value, '*=')
        self.assertEqual(tokens[18].value, '/=')
        self.assertEqual(tokens[19].value, ';')
        self.assertEqual(tokens[20].value, ',')
        self.assertEqual(tokens[21].value, '\'')
        self.assertEqual(tokens[22].value, ':')
        self.assertEqual(tokens[23].value, '(')
        self.assertEqual(tokens[24].value, ')')
        self.assertEqual(tokens[25].value, '[')
        self.assertEqual(tokens[26].value, ']')
        self.assertEqual(tokens[27].value, '{')
        self.assertEqual(tokens[28].value, '}')

    def test_reserved(self):
        tokens = self.scanner.tokenize("if else for while break continue return eye zeros ones print")

        self.assertEqual(len(tokens), 11)

        self.assertEqual(tokens[0].type, 'IF')
        self.assertEqual(tokens[1].type, 'ELSE')
        self.assertEqual(tokens[2].type, 'FOR')
        self.assertEqual(tokens[3].type, 'WHILE')
        self.assertEqual(tokens[4].type, 'BREAK')
        self.assertEqual(tokens[5].type, 'CONTINUE')
        self.assertEqual(tokens[6].type, 'RETURN')
        self.assertEqual(tokens[7].type, 'EYE')
        self.assertEqual(tokens[8].type, 'ZEROS')
        self.assertEqual(tokens[9].type, 'ONES')
        self.assertEqual(tokens[10].type, 'PRINT')

        self.assertEqual(tokens[0].value, 'if')
        self.assertEqual(tokens[1].value, 'else')
        self.assertEqual(tokens[2].value, 'for')
        self.assertEqual(tokens[3].value, 'while')
        self.assertEqual(tokens[4].value, 'break')
        self.assertEqual(tokens[5].value, 'continue')
        self.assertEqual(tokens[6].value, 'return')
        self.assertEqual(tokens[7].value, 'eye')
        self.assertEqual(tokens[8].value, 'zeros')
        self.assertEqual(tokens[9].value, 'ones')
        self.assertEqual(tokens[10].value, 'print')

    def test_id(self):
        tokens = self.scanner.tokenize('abc1 ABC2 aBc3 _0abc _a_b_1')

        self.assertEqual(len(tokens), 5)

        self.assertSequenceEqual([t.type for t in tokens], ['ID']*len(tokens))

        self.assertEqual(tokens[0].value, 'abc1')
        self.assertEqual(tokens[1].value, 'ABC2')
        self.assertEqual(tokens[2].value, 'aBc3')
        self.assertEqual(tokens[3].value, '_0abc')
        self.assertEqual(tokens[4].value, '_a_b_1')

    def test_string(self):
        tokens = self.scanner.tokenize('"qwerty" "foo bar" "test !@#$%^&*(){}[]=+-/*" "aaa\\"bbb"')

        self.assertEqual(len(tokens), 4)

        self.assertSequenceEqual([t.type for t in tokens], ['STRING']*len(tokens))

        self.assertEqual(tokens[0].value, 'qwerty')
        self.assertEqual(tokens[1].value, 'foo bar')
        self.assertEqual(tokens[2].value, 'test !@#$%^&*(){}[]=+-/*')
        self.assertEqual(tokens[3].value, 'aaa"bbb')

    def test_float(self):
        tokens = self.scanner.tokenize("1. .1 1.1 1.E2 .1E2 1.1E2 1E2 1E-2 1E+2 1e2")

        self.assertEqual(len(tokens), 10)

        self.assertSequenceEqual([t.type for t in tokens], ['FLOAT']*len(tokens))

        self.assertEqual(tokens[0].value, 1.0)
        self.assertEqual(tokens[1].value, 0.1)
        self.assertEqual(tokens[2].value, 1.1)
        self.assertEqual(tokens[3].value, 100.0)
        self.assertEqual(tokens[4].value, 10.0)
        self.assertEqual(tokens[5].value, 110.0)
        self.assertEqual(tokens[6].value, 100.0)
        self.assertEqual(tokens[7].value, 0.01)
        self.assertEqual(tokens[8].value, 100.0)
        self.assertEqual(tokens[9].value, 100.0)

    def test_int(self):
        tokens = self.scanner.tokenize("1 12 1234567890")

        self.assertEqual(len(tokens), 3)

        self.assertSequenceEqual([t.type for t in tokens], ['INT']*len(tokens))

        self.assertEqual(tokens[0].value, 1)
        self.assertEqual(tokens[1].value, 12)
        self.assertEqual(tokens[2].value, 1234567890)

    def test_ignored(self):
        tokens = self.scanner.tokenize(" \t  \n   \n # abc for 123\n # foo ")
        self.assertEqual(len(tokens), 0)

    def test_newline(self):
        tokens = self.scanner.tokenize("\n\n\nA\nB C")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].lineno, 4)
        self.assertEqual(tokens[1].lineno, 5)
        self.assertEqual(tokens[2].lineno, 5)

    def test_errors(self):
        self.assertRaises(LexerError, self.scanner.tokenize, "%")
        self.assertRaises(LexerError, self.scanner.tokenize, "@")
        self.assertRaises(LexerError, self.scanner.tokenize, "!")
        self.assertRaises(LexerError, self.scanner.tokenize, "$")
        self.assertRaises(LexerError, self.scanner.tokenize, "^")
