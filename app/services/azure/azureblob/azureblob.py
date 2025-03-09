import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class AzureBlobService:
    def __init__(self, connection_string: str, container_name: str):
        """Initialize the AzureBlobService with a connection string and container name."""
        self.blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )
        self.container_client = self.blob_service_client.get_container_client(
            container_name
        )

    def upload_blob(self, file_path: str, blob_name: str = None):
        """Upload a file to Azure Blob Storage."""
        if blob_name is None:
            blob_name = os.path.basename(file_path)

        blob_client = self.container_client.get_blob_client(blob_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded {file_path} to {blob_name}")

    def download_blob(self, blob_name: str, download_path: str):
        """Download a blob from Azure Blob Storage."""
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print(f"Downloaded {blob_name} to {download_path}")

    def list_blobs(self):
        """List all blobs in the container."""
        blobs = self.container_client.list_blobs()
        return [blob.name for blob in blobs]

    def delete_blob(self, blob_name: str):
        """Delete a blob from Azure Blob Storage."""
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
        print(f"Deleted blob {blob_name}")
