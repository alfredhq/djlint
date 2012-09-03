import ast
import os
from djlint.parsers import Parser
from unittest import TestCase
from .base import TESTS_ROOT, EXAMPLE_PROJECT_FILES


class ParserTests(TestCase):

    def setUp(self):
        self.example_project = os.path.join(TESTS_ROOT, 'example_project')

    def test_init_with_absolute_path(self):
        parser = Parser(self.example_project)
        self.assertEqual(parser.repo_path, self.example_project)

    def test_init_with_relative_path(self):
        with self.assertRaises(ValueError):
            parser = Parser('relative/path')

    def test_walk(self):
        parser = Parser(self.example_project)
        self.assertEqual(
            sorted(list(parser.walk())),
            sorted([os.path.join(self.example_project, x)
                    for x in EXAMPLE_PROJECT_FILES])
        )

    def test_relpath(self):
        parser = Parser(self.example_project)
        path = os.path.join(self.example_project, 'app/models.py')
        self.assertEqual(parser.relpath(path), 'app/models.py')

    def test_parse_file(self):
        parser = Parser(self.example_project)
        path = os.path.join(self.example_project, 'app/models.py')
        code = parser.parse_file(path)
        self.assertIsInstance(code, tuple)
        self.assertIsInstance(code[1], ast.Module)
        self.assertEqual(code[0], 'app/models.py')

    def test_parse_file_with_syntax_error(self):
        parser = Parser(self.example_project)
        path = os.path.join(self.example_project, 'syntax_error.py')
        code = parser.parse_file(path)
        self.assertIsInstance(code, tuple)

    def test_parse_non_existent_file(self):
        parser = Parser(self.example_project)
        path = os.path.join(self.example_project, 'non_existent.py')
        with self.assertRaises(IOError):
            code = parser.parse_file(path)

    def test_parse(self):
        parser = Parser(self.example_project)
        code = parser.parse()
        self.assertIsInstance(code, dict)
        self.assertEqual(
            sorted(list(parser.parse())),
            sorted(EXAMPLE_PROJECT_FILES)
        )
