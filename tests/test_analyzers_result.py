from djlint.analyzers.base import Result, CodeSnippet
from unittest2 import TestCase


class ResultTests(TestCase):

    def test_init(self):
        result = Result('simple result', 'app/models.py', 2)
        self.assertEqual(result.description, 'simple result')
        self.assertEqual(result.path, 'app/models.py')
        self.assertEqual(result.line, 2)
        self.assertIsInstance(result.source, CodeSnippet)
        self.assertIsInstance(result.solution, CodeSnippet)
