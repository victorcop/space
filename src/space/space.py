import logging
from typing import Any, Dict, List, cast

import requests
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from space.config import ASTROS_API_URL

logger = logging.getLogger(__name__)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(
        (requests.exceptions.ConnectionError, requests.exceptions.Timeout)
    ),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def fetch_people_in_space() -> List[Dict[str, Any]]:
    try:
        response = requests.get(ASTROS_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Fetched data: {data}")
        return cast(List[Dict[str, Any]], data["people"])
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {e}")
        raise
    except (KeyError, ValueError) as e:
        logger.error(f"Error parsing API response: {e}")
        raise
