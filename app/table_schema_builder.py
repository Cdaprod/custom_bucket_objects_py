from pydantic import BaseModel, create_model
from typing import List, Dict, Any
import pandas as pd
import os

# Assume the bucket_path is known
bucket_path = "/path/to/your/bucket"

def find_file(bucket_path: str, row_name: str) -> str:
    # Define the target file name
    target_file_name = f"{row_name}.md"
    
    # Traverse the bucket
    for root, dirs, files in os.walk(bucket_path):
        if target_file_name in files:
            # Return the full path of the file if found
            return os.path.join(root, target_file_name)
    
    # Return None if the file is not found
    return None
    
def create_schema(table_data: List[Dict[str, Any]]) -> List[BaseModel]:
    schemas = []
    for row in table_data:
        # Dynamically create a Pydantic model based on the row data
        model_name = f"Schema_{row['ID']}"
        file_path = find_file(bucket_path, row['Name'])
        model = create_model(
            model_name,
            id=(int, ...),
            name=(str, ...),
            properties=(List[str], ...),
            file_path=(str, file_path)  # Set default value to the file path
        )
        # Populate the model with data
        schema_instance = model(id=row['ID'], name=row['Name'], properties=row['Properties'].split(', '))
        schemas.append(schema_instance)
    return schemas

# Assume markdown_data is your Markdown string containing your table
markdown_data = """
| ID | Name  | Properties |
|----|-------|------------|
| 1  | Item1 | prop1, prop2 |
| 2  | Item2 | prop3, prop4 |
"""

def extract_table_data(markdown: str) -> List[Dict[str, Any]]:
    # Assuming there's one table in the markdown data
    tables = pd.read_html(markdown, header=0)
    table_data = tables[0].to_dict(orient='records')
    return table_data

# Extract table data
table_data = extract_table_data(markdown_data)

# Create and populate schema
schemas = create_schema(table_data)