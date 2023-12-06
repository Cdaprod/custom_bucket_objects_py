import unittest
from ..app.main import SourceCode

class TestSourceCode(unittest.TestCase):

    def setUp(self):
        self.sample_code = {
            "id": "test_id",
            "imports": ["pandas", "numpy"],
            "classes": ["TestClass", "AnotherClass"],
            "code": "class TestClass: pass",
            "syntax": "Python",
            "context": "Test context",
            "metadata": {"key": "value"}
        }

    def test_source_code_creation(self):
        source_code = SourceCode(**self.sample_code)

        self.assertEqual(source_code.id, "test_id")
        self.assertListEqual(source_code.imports, ["pandas", "numpy"])
        self.assertListEqual(source_code.classes, ["TestClass", "AnotherClass"])
        self.assertEqual(source_code.code, "class TestClass: pass")
        self.assertEqual(source_code.syntax, "Python")
        self.assertEqual(source_code.context, "Test context")
        self.assertDictEqual(source_code.metadata, {"key": "value"})

if __name__ == '__main__':
    unittest.main()
