import pytest
import sqlite3
from app.database.db import init_db
from app.app import insert_to_db, get_file_log_by_filename

@pytest.fixture
def mock_db():
    """Creates an in-memory SQLite database for testing."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create the file_logs table
    cursor.execute("""
        CREATE TABLE file_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    yield conn, cursor  # Provide both connection and cursor to tests
    conn.close()

def test_insert_and_get_file_log(mock_db, monkeypatch):
    """Tests inserting and retrieving a file log."""
    
    conn, cursor = mock_db

    # Patch the database connection
    monkeypatch.setattr("app.database.db.init_db", lambda: (conn, cursor))

    # Insert file log
    files_uploaded = ["test_file.txt"]
    insert_to_db(files_uploaded=files_uploaded, cursor=cursor)

    # Fetch file log
    file_log = get_file_log_by_filename("test_file.txt", cursor)

    print(file_log)

    assert file_log is not None
    assert len(file_log) > 0
    assert file_log[0][1] == "test_file.txt"
