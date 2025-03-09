import os

from app.helper.get_files import get_latest_files
from app.constants.settings import ProjectSettings

from app.services.azure.azureblob.azureblob import AzureBlobService

def execute_logic():
    # set source folder directory
    directory = ProjectSettings.SOURCE_DIRECTORY_PATH

    # get latest files from source directory
    latest_files = get_latest_files(directory)

    # add complete path
    latest_files_complete_path = [os.path.join(directory, file_name) for file_name in latest_files]

    # init azure blob
    az_blob = AzureBlobService(
        connection_string=ProjectSettings.AZURE_STORAGE_CONNECTION_STRING,
        container_name=ProjectSettings.AZURE_STORAGE_CONTAINER_NAME,
    )

    # iterate over files and upload to azure blob
    for index, file_path in enumerate(latest_files_complete_path):
        az_blob.upload_blob(file_path=file_path, blob_name=file_path)
