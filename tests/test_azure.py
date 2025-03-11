import json
import pytest
import azure.functions as func
from function_app import TestFunction


@pytest.fixture
def mock_request():
    """Fixture to create a mock HttpRequest."""

    def _mock_request(params=None, body=None):
        req = func.HttpRequest(
            method="GET",
            url="http://localhost:7071/api/TestFunction",
            headers={},
            params=params or {},
            body=json.dumps(body).encode("utf-8") if body else None,
        )
        return req

    return _mock_request


def test_azure_function_response(mock_request):
    """Test function with a valid query parameter."""
    req = mock_request(params={"name": "Alice"})
    response = TestFunction(req)

    assert response.status_code == 200
    assert response.get_body().decode() == "pass"


def test_valid_param(mock_request):
    """Test function with a valid JSON body."""
    req = mock_request(params={"mode": "0"})
    response = TestFunction(req)

    assert response.status_code == 200
    assert response.get_body().decode() == "pass"

def test_missing_name(mock_request):
    """Test function with missing 'name' parameter."""
    req = mock_request()
    response = TestFunction(req)

    assert response.status_code == 400
    assert "Please pass a name" in response.get_body().decode()
