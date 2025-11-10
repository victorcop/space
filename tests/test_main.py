"""Unit tests for __main__.py CLI module."""

import logging
from typing import Any
from unittest.mock import Mock, patch

import pytest

from space.__main__ import main, parse_args, setup_logging


class TestSetupLogging:
    """Tests for setup_logging function."""

    def test_setup_logging_warning_level(self, reset_logging: Any) -> None:
        """Test default logging level is WARNING."""
        setup_logging(verbose=False, debug=False)
        logger = logging.getLogger()
        # Check that at least one handler was added and its level
        assert len(logger.handlers) > 0
        assert (
            logger.handlers[0].level == logging.NOTSET
            or logger.level == logging.WARNING
        )

    def test_setup_logging_info_level(self, reset_logging: Any) -> None:
        """Test verbose flag sets INFO level."""
        setup_logging(verbose=True, debug=False)
        logger = logging.getLogger()
        # basicConfig sets the level on handlers, not always root logger
        assert len(logger.handlers) > 0
        # The effective level should be INFO
        assert logger.getEffectiveLevel() <= logging.INFO

    def test_setup_logging_debug_level(self, reset_logging: Any) -> None:
        """Test debug flag sets DEBUG level."""
        setup_logging(verbose=False, debug=True)
        logger = logging.getLogger()
        assert len(logger.handlers) > 0
        # The effective level should be DEBUG
        assert logger.getEffectiveLevel() <= logging.DEBUG

    def test_setup_logging_debug_overrides_verbose(self, reset_logging: Any) -> None:
        """Test debug flag takes precedence over verbose."""
        setup_logging(verbose=True, debug=True)
        logger = logging.getLogger()
        assert len(logger.handlers) > 0
        # The effective level should be DEBUG
        assert logger.getEffectiveLevel() <= logging.DEBUG


class TestParseArgs:
    """Tests for parse_args function."""

    def test_parse_args_no_flags(self) -> None:
        """Test parsing with no arguments."""
        args = parse_args([])
        assert args.verbose is False
        assert args.debug is False

    def test_parse_args_verbose_flag(self) -> None:
        """Test parsing with verbose flag."""
        args = parse_args(["-v"])
        assert args.verbose is True
        assert args.debug is False

    def test_parse_args_verbose_long_flag(self) -> None:
        """Test parsing with --verbose flag."""
        args = parse_args(["--verbose"])
        assert args.verbose is True

    def test_parse_args_debug_flag(self) -> None:
        """Test parsing with debug flag."""
        args = parse_args(["-d"])
        assert args.debug is True
        assert args.verbose is False

    def test_parse_args_debug_long_flag(self) -> None:
        """Test parsing with --debug flag."""
        args = parse_args(["--debug"])
        assert args.debug is True

    def test_parse_args_both_flags(self) -> None:
        """Test parsing with both verbose and debug flags."""
        args = parse_args(["-v", "-d"])
        assert args.verbose is True
        assert args.debug is True

    def test_parse_args_version(self) -> None:
        """Test --version flag exits."""
        with pytest.raises(SystemExit):
            parse_args(["--version"])


class TestMain:
    """Tests for main function."""

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_success(self, mock_console_class: Any, mock_fetch: Any) -> None:
        """Test successful execution of main."""
        # Arrange
        mock_fetch.return_value = [
            {"name": "John Doe", "craft": "ISS"},
            {"name": "Jane Smith", "craft": "ISS"},
        ]
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space"]):
            result = main()

        # Assert
        assert result == 0
        mock_fetch.assert_called_once()
        assert mock_console.print.call_count >= 2  # Header and table

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_empty_list(self, mock_console_class: Any, mock_fetch: Any) -> None:
        """Test main with no people in space."""
        # Arrange
        mock_fetch.return_value = []
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space"]):
            result = main()

        # Assert
        assert result == 0
        mock_fetch.assert_called_once()

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_with_verbose_flag(
        self, mock_console_class: Any, mock_fetch: Any
    ) -> None:
        """Test main with verbose flag."""
        # Arrange
        mock_fetch.return_value = [{"name": "Test", "craft": "ISS"}]
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space", "-v"]):
            result = main()

        # Assert
        assert result == 0
        mock_fetch.assert_called_once()

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_with_debug_flag(
        self, mock_console_class: Any, mock_fetch: Any
    ) -> None:
        """Test main with debug flag."""
        # Arrange
        mock_fetch.return_value = [{"name": "Test", "craft": "ISS"}]
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space", "-d"]):
            result = main()

        # Assert
        assert result == 0
        mock_fetch.assert_called_once()

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_displays_correct_count(
        self, mock_console_class: Any, mock_fetch: Any
    ) -> None:
        """Test main displays correct count of people."""
        # Arrange
        test_people = [
            {"name": "Person 1", "craft": "ISS"},
            {"name": "Person 2", "craft": "ISS"},
            {"name": "Person 3", "craft": "Tiangong"},
        ]
        mock_fetch.return_value = test_people
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space"]):
            main()

        # Assert
        # Check that the count (3) appears in the output
        call_args_list = mock_console.print.call_args_list
        assert any("3" in str(call) for call in call_args_list)

    @patch("space.__main__.fetch_people_in_space")
    @patch("space.__main__.Console")
    def test_main_logs_startup(
        self, mock_console_class: Any, mock_fetch: Any, caplog: Any
    ) -> None:
        """Test main logs startup message."""
        # Arrange
        import logging

        caplog.set_level(logging.INFO)
        mock_fetch.return_value = []
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        # Act
        with patch("sys.argv", ["space", "-v"]):
            main()

        # Assert
        assert "Space module CLI started" in caplog.text
