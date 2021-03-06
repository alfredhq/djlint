import os

from djlint.analyzers.syntax_error import SyntaxErrorAnalyzer
from djlint.parsers import Parser

from unittest import TestCase
from .base import TESTS_ROOT


class SyntaxErrorAnalyzerTests(TestCase):

    def setUp(self):
        self.example_project = os.path.join(TESTS_ROOT, 'example_project')
        self.code = Parser(self.example_project).parse()

    def test_analyze(self):
        analyzer = SyntaxErrorAnalyzer(self.code, self.example_project)
        results = list(analyzer.analyze())
        self.assertEqual(len(results), 1)
        result = results[0]
        self.assertEqual(result.description, 'Syntax error: invalid syntax.')
        self.assertEqual(result.path, 'syntax_error.py')
        self.assertEqual(result.line, 2)
        self.assertEqual(result.source, [
            (1, False, 'def main():'),
            (2, True,  '    syntax error'),
            (3, False, ''),
            (4, False, ''),
        ])
        self.assertEqual(result.solution, [])
