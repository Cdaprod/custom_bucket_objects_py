from minio_main import connect_to_minio, process_bucket_data
from weaviate_main import connect_to_weaviate, define_schema, ingest_data
from main import parse_markdown_content

def main():
    # Connect to MinIO
    minio_client = connect_to_minio()
    bucket_name = "your-bucket-name"

    # Retrieve data from MinIO
    minio_data = process_bucket_data(minio_client, bucket_name)

    # Process data using main.py
    processed_data = [parse_markdown_content(data) for data in minio_data]

    # Connect to Weaviate and define schema
    weaviate_client = connect_to_weaviate()
    define_schema(weaviate_client)

    # Ingest data into Weaviate
    for data in processed_data:
        ingest_data(weaviate_client, data)

if __name__ == "__main__":
    main()
