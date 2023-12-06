import unittest
from ..app.main import parse_markdown_content, MarkdownDocument

class TestParseMarkdownContent(unittest.TestCase):

    def test_parse_valid_markdown(self):
        markdown_content = """
 
# Test Document

This is a test document.

---

```python
print("Hello, world!")
```

# Table Database

|  Title  | Tags |
|---------|------|
| Prompts |  AI  |
"""

        result = parse_markdown_content(markdown_content)

        self.assertIsInstance(result, MarkdownDocument)
        self.assertEqual(result.content.strip(), "This is a test document.")
        self.assertEqual(len(result.code_blocks), 1)
        self.assertIn("Hello, world!", result.code_blocks[0].code)
        self.assertEqual(len(result.tables), 1)
        self.assertEqual(result.tables[0].headers, ['Title', 'Tags'])
        self.assertEqual(result.tables[0].rows[0], {'Title': 'Prompts', 'Tags': 'AI'})

if __name__ == '__main__':
    unittest.main()