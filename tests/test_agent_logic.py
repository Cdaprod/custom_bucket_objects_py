import unittest
from unittest.mock import patch
from ..main import agent_logic

class TestAgentLogic(unittest.TestCase):

    def test_agent_logic_python_file(self):
        input_data = {
            "filename": "test_script.py",
            "content": "print('Hello World')"
        }
        result = agent_logic(input_data)
        self.assertIn("Analyze the following Python script", result)

    def test_agent_logic_markdown_file(self):
        input_data = {
            "filename": "test_document.md",
            "content": "# Markdown Header\nSome content here"
        }
        result = agent_logic(input_data)
        self.assertIn("Analyze the following Markdown content", result)

if __name__ == '__main__':
    unittest.main()
