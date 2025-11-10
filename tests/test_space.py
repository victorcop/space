"""Unit tests for space.py module."""

from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from space.space import fetch_people_in_space


class TestFetchPeopleInSpace:
    """Tests for fetch_people_in_space function."""

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_success(self, mock_get: Any) -> None:
        """Test successful API call returns people list."""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {
            "number": 3,
            "people": [
                {"name": "John Doe", "craft": "ISS"},
                {"name": "Jane Smith", "craft": "ISS"},
                {"name": "Bob Johnson", "craft": "Tiangong"},
            ],
            "message": "success",
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Act
        result = fetch_people_in_space()

        # Assert
        assert len(result) == 3
        assert result[0]["name"] == "John Doe"
        assert result[0]["craft"] == "ISS"
        assert result[1]["name"] == "Jane Smith"
        assert result[2]["craft"] == "Tiangong"
        mock_get.assert_called_once_with(
            "http://api.open-notify.org/astros.json", timeout=10
        )

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_empty_list(self, mock_get: Any) -> None:
        """Test API call with no people in space."""
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {
            "number": 0,
            "people": [],
            "message": "success",
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Act
        result = fetch_people_in_space()

        # Assert
        assert len(result) == 0
        assert result == []

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_network_error(self, mock_get: Any) -> None:
        """Test network error handling."""
        # Arrange
        mock_get.side_effect = requests.exceptions.ConnectionError("Network error")

        # Act & Assert
        with pytest.raises(requests.exceptions.RequestException):
            fetch_people_in_space()

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_timeout(self, mock_get: Any) -> None:
        """Test timeout error handling."""
        # Arrange
        mock_get.side_effect = requests.exceptions.Timeout("Request timeout")

        # Act & Assert
        with pytest.raises(requests.exceptions.RequestException):
            fetch_people_in_space()

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_http_error(self, mock_get: Any) -> None:
        """Test HTTP error handling (4xx, 5xx)."""
        # Arrange
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Not Found"
        )
        mock_get.return_value = mock_response

        # Act & Assert
        with pytest.raises(requests.exceptions.RequestException):
            fetch_people_in_space()

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_invalid_json(self, mock_get: Any) -> None:
        """Test handling of invalid JSON response."""
        # Arrange
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        # Act & Assert
        with pytest.raises(ValueError):
            fetch_people_in_space()

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_missing_people_key(self, mock_get: Any) -> None:
        """Test handling when 'people' key is missing from response."""
        # Arrange
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"number": 3, "message": "success"}
        mock_get.return_value = mock_response

        # Act & Assert
        with pytest.raises(KeyError):
            fetch_people_in_space()

    @patch("space.space.requests.get")
    def test_fetch_people_in_space_logs_data(self, mock_get: Any, caplog: Any) -> None:
        """Test that fetched data is logged."""
        # Arrange
        import logging

        caplog.set_level(logging.INFO)

        mock_response = Mock()
        mock_response.json.return_value = {
            "number": 1,
            "people": [{"name": "Test Person", "craft": "ISS"}],
            "message": "success",
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Act
        fetch_people_in_space()

        # Assert
        assert "Fetched data:" in caplog.text
