import json
import pytest
from app.app import execute_logic


def test_execute():
    status = execute_logic()

    assert status == "pass"
