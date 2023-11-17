import unittest
from ..main import parse_python_script

class TestParsePythonScript(unittest.TestCase):

    def test_parse_valid_python_script(self):
        script = """
class MyClass:
    pass

import pandas as pd
"""

        result = parse_python_script(script)
        self.assertIn('MyClass', result.classes)
        self.assertIn('pandas', result.imports)
        self.assertEqual(result.syntax, 'Python')
        self.assertEqual(result.context, '')
        self.assertIsNotNone(result.id)

    def test_parse_invalid_python_script(self):
        script = "class MyClass pass"

        result = parse_python_script(script)
        self.assertEqual(result.id, 'error')
        self.assertIn('Syntax error', result.context)

if __name__ == '__main__':
    unittest.main()
