import unittest
from ..app.main import SourceCodePromptTemplate, MarkdownDocumentPromptTemplate, PythonScriptPromptTemplate

class TestPromptTemplates(unittest.TestCase):

    def test_source_code_prompt_template(self):
        template = SourceCodePromptTemplate()
        result = template.format("sample script")
        self.assertIn("Analyze the following Python script", result)
        self.assertIn("sample script", result)

    def test_markdown_document_prompt_template(self):
        template = MarkdownDocumentPromptTemplate()
        result = template.format("sample markdown content")
        self.assertIn("Analyze the following Markdown content", result)
        self.assertIn("sample markdown content", result)

    def test_python_script_prompt_template(self):
        template = PythonScriptPromptTemplate()
        result = template.format("sample python script")
        self.assertIn("Analyze the following Python script", result)
        self.assertIn("sample python script", result)

if __name__ == '__main__':
    unittest.main()
