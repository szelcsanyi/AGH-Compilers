import unittest
from typing import Any, List, Tuple

import numpy as np

from compiler.interpreter import Interpreter
from compiler.parser import MParser
from compiler.scanner import MLexer
from compiler.types import TypeChecker


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        # create new instances to clean state
        self.lexer = MLexer()
        self.parser = MParser()
        self.checker = TypeChecker()
        self.interpreter = Interpreter()

    def execute(self, program: str):
        root = self.parser.parse(program, lexer=self.lexer, tracking=True)
        self.checker.check(root)
        return self.interpreter.execute_with_return(root)

    def assertExecute(self, *tests: Tuple[str, Any]):
        # execute tests
        tests = [(self.execute(test), result) for test, result in tests]

        for test in tests:
            np.testing.assert_equal(test[0], test[1])

    def test_constants(self):
        self.assertExecute(
            ('return 2;',       2),
            ('return 2.;',      2.),
            ('return "2";',     '2'),
            ('return true;',    True),
            ('return false;',   False),
        )

    def test_matrices(self):
        self.assertExecute(
            ('return [1];',         np.asarray([1])),
            ('return [1,2,3];',     np.asarray([1, 2, 3])),
            ('return [[1], [1]];',  np.asarray([[1], [1]])),
            ('return [[1,2,3]];',   np.asarray([[1, 2, 3]])),
            ('return [[[[1]]]];',   np.asarray([[[[1]]]])),
        )

    def test_operators(self):
        sA = '[[1, 2], [3, 4]]'
        sB = '[[5, 6], [7, 8]]'
        A = np.asarray([[1, 2], [3, 4]])
        B = np.asarray([[5, 6], [7, 8]])

        self.assertExecute(
            ('return 2 + 3;',       2 + 3),
            ('return 2. + 3;',      2. + 3),
            ('return "2" + 3;',     '23'),

            ('return 2 - 3;',       2 - 3),
            ('return 2. - 3;',      2. - 3),

            ('return 2 * 3;',       2 * 3),
            ('return 2. * 3;',      2. * 3),

            ('return 2 / 3;',       2 / 3),
            ('return 2. / 3;',      2. / 3),

            ('return -2;',          -2),
            ('return -2.;',         -2.),

            ('return 2 == 2;',      2 == 2),
            ('return 2. == 2.;',    2. == 2.),
            ('return "2" == "2";',  "2" == "2"),
            ('return 2 == 3;',      2 == 3),
            ('return 2. == 3.;',    2. == 3.),
            ('return "2" == "3";',  "2" == "3"),
            ('return 2 != 3;',      2 != 3),
            ('return 2. != 3.;',    2. != 3.),
            ('return "2" != "3";',  "2" != "3"),

            ('return 3 > 2;',       3 > 2),
            ('return 2 < 3;',       2 < 3),
            ('return 3 < 2;',       3 < 2),
            ('return 2 > 3;',       2 > 3),

            ('return 3 >= 2;',      3 >= 3),
            ('return 2 <= 3;',      2 <= 3),
            ('return 3 >= 3;',      3 >= 3),
            ('return 3 <= 3;',      3 <= 3),
            ('return 3 <= 2;',      3 <= 2),
            ('return 2 >= 3;',      2 >= 3),

            (f'return {sA} .+ {sB};',   np.add(A, B)),
            (f'return {sA} .- {sB};',   np.subtract(A, B)),
            (f'return {sA} .* {sB};',   np.multiply(A, B)),
            (f'return {sA} ./ {sB};',   np.divide(A, B)),

            (f'return {sA}\';',         np.transpose(A)),
            (f'return {sB}\';',         np.transpose(B)),
        )

    def test_matrix_functions(self):
        self.assertExecute(
            ('return eye(3, 3);',       np.eye(3, 3)),
            ('return eye(1, 3);',       np.eye(1, 3)),
            ('return eye(3, 1);',       np.eye(3, 1)),

            ('return zeros(3);',        np.zeros((3, ))),
            ('return zeros(3, 2);',     np.zeros((3, 2))),
            ('return zeros(3, 2, 1);',  np.zeros((3, 2, 1))),

            ('return ones(3);',         np.ones((3, ))),
            ('return ones(3, 2);',      np.ones((3, 2))),
            ('return ones(3, 2, 1);',   np.ones((3, 2, 1))),
        )

    def test_assignment(self):
        self.assertExecute(
            ('a = 3; return a;',            3),
            ('b = 3.; return b;',           3.),
            ('c = "c"; return c;',          'c'),

            ('c = 3; c += 2; return c;',    3 + 2),
            ('c = 3; c -= 2; return c;',    3 - 2),
            ('c = 3; c *= 2; return c;',    3 * 2),
            ('c = 3; c /= 2; return c;',    3 / 2),
        )

    def test_selectors(self):
        sA = '[[1, 2], [3, 4]]'
        A = np.asarray([[1, 2], [3, 4]])

        self.assertExecute(
            (f'A = {sA}; return A[0];',       A[0]),
            (f'A = {sA}; return A[1];',       A[1]),
            (f'A = {sA}; return A[0, 1];',    A[0, 1]),
            (f'A = {sA}; return A[1, 1];',    A[1, 1]),
        )

    def test_if(self):
        self.assertExecute(
            ('if (true) return 1; return 2;',      1),
            ('if (false) return 1; return 2;',     2),

            ('if (true) return 1; else return 2; return 3;',      1),
            ('if (false) return 1; else return 2; return 3;',     2),
        )

    def test_while(self):
        self.assertExecute(
            ('a = 3; while(a > 0) a -= 1; return a;',      0),
            ('a = 0; while(a <= 3) a += 1; return a;',     4),
        )

    def test_for(self):
        self.assertExecute(
            ('a = 0; for i = 0:6 a += i; return a;',    sum(range(0, 6))),
            ('a = 0; for i = 1:6 a += i; return a;',    sum(range(1, 6))),
            ('a = 0; for i = 6:1 a += i; return a;',    sum(range(6, 1))),
        )

    def test_break(self):
        self.assertExecute(
            ('a = 0; while(true) { a += 1; if(a>5) break; } return a;',      6),
        )

    def test_continue(self):
        self.assertExecute(
            ('a = 0; for i = 0:6 { if(i<3) continue; a += i; } return a;',   sum(range(3,6))),
        )

    def test_return(self):
        self.assertExecute(
            ('a = 0; while(true) { a += 1; if(a>5) return a; }',      6),
        )
