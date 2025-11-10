"""Unit tests for the config module."""

import os
import sys
from unittest.mock import patch

import pytest


def test_config_missing_base_url() -> None:
    """Test that ValueError is raised when SPACE_API_BASE_URL is missing."""
    # Remove the config module if already imported
    if "space.config" in sys.modules:
        del sys.modules["space.config"]

    with patch("dotenv.load_dotenv"):
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="SPACE_API_BASE_URL must be set"):
                import space.config  # noqa: F401


def test_config_missing_endpoint() -> None:
    """Test that ValueError is raised when SPACE_ASTROS_ENDPOINT is missing."""
    # Remove the config module if already imported
    if "space.config" in sys.modules:
        del sys.modules["space.config"]

    with patch("dotenv.load_dotenv"):
        with patch.dict(
            os.environ, {"SPACE_API_BASE_URL": "http://api.example.com"}, clear=True
        ):
            with pytest.raises(ValueError, match="SPACE_ASTROS_ENDPOINT must be set"):
                import space.config  # noqa: F401


def test_config_valid_values() -> None:
    """Test that config loads successfully with valid environment variables."""
    # Remove the config module if already imported
    if "space.config" in sys.modules:
        del sys.modules["space.config"]

    with patch("dotenv.load_dotenv"):
        with patch.dict(
            os.environ,
            {
                "SPACE_API_BASE_URL": "http://api.example.com",
                "SPACE_ASTROS_ENDPOINT": "/test.json",
            },
            clear=True,
        ):
            import space.config

            assert space.config.API_BASE_URL == "http://api.example.com"
            assert space.config.ASTROS_ENDPOINT == "/test.json"
            assert space.config.ASTROS_API_URL == "http://api.example.com/test.json"
