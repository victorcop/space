"""Configuration settings for the space application."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
# Look for .env in the project root (two levels up from this file)
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# API Configuration
# Must be set via .env file or environment variables
API_BASE_URL = os.getenv("SPACE_API_BASE_URL")
ASTROS_ENDPOINT = os.getenv("SPACE_ASTROS_ENDPOINT")

# Validate required configuration (skip during pytest runs)
if not os.getenv("PYTEST_CURRENT_TEST"):
    if not API_BASE_URL:
        raise ValueError(
            "SPACE_API_BASE_URL must be set in .env file or environment variables"
        )
    if not ASTROS_ENDPOINT:
        raise ValueError(
            "SPACE_ASTROS_ENDPOINT must be set in .env file or environment variables"
        )

# Full API URL
ASTROS_API_URL = f"{API_BASE_URL}{ASTROS_ENDPOINT}"
