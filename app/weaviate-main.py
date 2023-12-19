from minio import Minio
from main import (
    parse_yaml_metadata,
    parse_table,
    parse_python_script,
    parse_markdown_content,
    EnhancedGeneralAnalysisPromptTemplate,
    agent_executor
)

def connect_to_minio():
    # Connect to MinIO
    client = Minio(
        "MINIO_SERVER_URL",
        access_key="YOUR_ACCESS_KEY",
        secret_key="YOUR_SECRET_KEY",
        secure=True  # Set to False if not using https
    )
    return client

def process_bucket_data(client, bucket_name):
    # List objects in the bucket and process
    objects = client.list_objects(bucket_name)
    for obj in objects:
        # Assuming the object contains markdown content
        # You would need to adjust this logic based on your data structure
        data = client.get_object(bucket_name, obj.object_name).read()
        markdown_document = parse_markdown_content(data.decode('utf-8'))
        # Further processing...
        print(markdown_document)

def main():
    client = connect_to_minio()
    bucket_name = "your-bucket-name"
    process_bucket_data(client, bucket_name)

if __name__ == "__main__":
    main()
