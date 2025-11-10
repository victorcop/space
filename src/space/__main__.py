import argparse
import logging
from typing import Optional

from rich.console import Console
from rich.table import Table

from space import __version__
from space.space import fetch_people_in_space


def setup_logging(verbose: bool, debug: bool) -> None:
    """
    Configure logging based on verbosity level.

    Args:
        verbose: Enable INFO level logging.
        debug: Enable DEBUG level logging.
    """
    if debug:
        level = logging.DEBUG
    elif verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_args(args: Optional[list] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: List of arguments to parse. If None, uses sys.argv.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(description="Space Module CLI")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output"
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser.parse_args(args)


def main() -> int:
    args = parse_args()
    setup_logging(verbose=args.verbose, debug=args.debug)
    logger = logging.getLogger(__name__)

    logger.info("Space module CLI started.")

    people = fetch_people_in_space()
    logger.info(f"Number of people in space: {len(people)}")

    console = Console()

    console.print(
        f"\n[bold cyan]🚀 People currently in space: {len(people)}[/bold cyan]\n"
    )

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=6)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Spacecraft", style="green")

    for i, person in enumerate(people, 1):
        table.add_row(str(i), person["name"], person["craft"])

    console.print(table)
    console.print()

    return 0
