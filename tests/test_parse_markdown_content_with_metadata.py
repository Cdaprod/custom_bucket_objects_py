import unittest
from ..main import parse_markdown_content, MarkdownDocument

def test_parse_valid_markdown_with_metadata(self):
    markdown_content = """
---
Tags:
  - Memory
  - Prompt Template
  - Cloud
  - Mono Repository
  - Python
  - RAG
  - Weaviate
Link to Repository: https://github.com/Cdaprod/custom_bucket_objects
Status: Done
Created time: 2023-10-01T13:31
Created By: David Cannan
---
 
# Test Document

This is a test document.

---

```python
print("Hello, world...it's David Cannan aka Cdaprod!")
```

# Table Database

|  Title  | Tags |
|---------|------|
| Prompts |  AI  |
"""

    result = parse_markdown_content(markdown_content)

    expected_metadata = {
        'Tags': ['Memory', 'Prompt Template', 'Cloud', 'Mono Repository', 'Python', 'RAG', 'Weaviate'],
        'Link to Repository': 'https://github.com/Cdaprod/custom_bucket_objects',
        'Status': 'Done',
        'Created time': '2023-10-01T13:31',
        'Created By': 'David Cannan'
    }

    self.assertEqual(result.metadata, expected_metadata)
    self.assertIsInstance(result, MarkdownDocument)
    self.assertEqual(result.content.strip(), "This is a test document.")
    self.assertEqual(len(result.code_blocks), 1)
    self.assertIn("Hello, world!", result.code_blocks[0].code)
    self.assertEqual(len(result.tables), 1)
    self.assertEqual(result.tables[0].headers, ['Title', 'Tags'])
    self.assertEqual(result.tables[0].rows[0], {'Title': 'Prompts', 'Tags': 'AI'})
