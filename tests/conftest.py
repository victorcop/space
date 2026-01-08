"""Pytest configuration and fixtures."""

import logging
import os
from typing import Any, Dict, Generator

import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_test_env() -> None:
    """Set up environment variables for testing."""
    os.environ["SPACE_API_BASE_URL"] = "http://api.open-notify.org"
    os.environ["SPACE_ASTROS_ENDPOINT"] = "/astros.json"


@pytest.fixture
def reset_logging() -> Generator[None, None, None]:
    """Reset logging configuration before test."""
    # Get the root logger
    logger = logging.getLogger()
    # Remove all handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    # Reset level
    logger.setLevel(logging.NOTSET)
    # Force basicConfig to be reconfigurable
    logging.root.handlers = []
    yield
    # Cleanup after test
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    logger.setLevel(logging.WARNING)


@pytest.fixture
def mock_api_response() -> Dict[str, Any]:
    """Fixture providing a standard mock API response."""
    return {
        "number": 3,
        "people": [
            {"name": "John Doe", "craft": "ISS"},
            {"name": "Jane Smith", "craft": "ISS"},
            {"name": "Bob Johnson", "craft": "Tiangong"},
        ],
        "message": "success",
    }


@pytest.fixture
def mock_empty_api_response() -> Dict[str, Any]:
    """Fixture providing an empty mock API response."""
    return {"number": 0, "people": [], "message": "success"}
