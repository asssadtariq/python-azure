import os

from app.helper.get_files import get_latest_files
from app.constants.settings import ProjectSettings

from app.database.db import init_db
from app.services.azure.azureblob.azureblob import AzureBlobService


def insert_to_db(files_uploaded, cursor):
    cursor.executemany(
        "INSERT INTO file_logs (file_name) VALUES (%s)", # ?
        [(file,) for file in files_uploaded],
    )

def get_file_log_by_filename(filename, cursor):
    cursor.execute("SELECT * FROM file_logs WHERE file_name = %s", (filename,)) # ?
    data = cursor.fetchall()
    return data

def load_to_db(files_uploaded):
    # get db object
    conn, cursor = init_db()

    insert_to_db(files_uploaded=files_uploaded, cursor=cursor)

    # commit
    conn.commit()

    conn.close()


def execute_logic():
    # set source folder directory
    directory = ProjectSettings.SOURCE_DIRECTORY_PATH

    # get latest files from source directory
    latest_files = get_latest_files(directory)

    # add complete path
    latest_files_complete_path = [
        os.path.join(directory, file_name) for file_name in latest_files
    ]

    # init azure blob
    az_blob = AzureBlobService(
        connection_string=ProjectSettings.AZURE_STORAGE_CONNECTION_STRING,
        container_name=ProjectSettings.AZURE_STORAGE_CONTAINER_NAME,
    )

    files_uploaded = []
    files_upload_status = []

    # iterate over files and upload to azure blob
    for index, file_path in enumerate(latest_files_complete_path):
        files_uploaded.append(file_path)
        try:
            az_blob.upload_blob(file_path=file_path, blob_name=file_path)
            files_upload_status.append(True)
        except Exception as e:
            files_upload_status.append(False)

    print("Updating DB..")
    load_to_db(files_uploaded)
    print("Pass")
    return "pass"
