import os
from dotenv import load_dotenv

load_dotenv()


class ProjectSettings:
    SOURCE_DIRECTORY_PATH: str = "source"
    AZURE_STORAGE_CONNECTION_STRING: str = os.environ.get(
        "AZURE_BLOB_CONNECTION_STRING"
    )
    AZURE_STORAGE_CONTAINER_NAME: str = "files"
