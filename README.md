# Space 🚀

A Python CLI application that fetches and displays information about astronauts currently in space.

## Features

- 🌌 Real-time data from the Open Notify API
- 🎨 Beautiful terminal output using Rich
- 📊 Formatted table display of astronauts and their spacecraft
- 🔧 Configurable logging levels (verbose, debug)
- ⚡ Error handling for API calls
- 🔄 Automatic retry with exponential backoff for transient failures
- 🔒 Security scanning with pip-audit and bandit
- 🎯 Pre-commit hooks for code quality enforcement
- ♻️ Automated dependency updates via Dependabot

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Install Globally (Recommended for Users)

Install the package globally to use the `space` command anywhere:

```bash
pip install space
```

Or install directly from the repository:

```bash
pip install git+https://github.com/yourusername/space.git
```

After installation, you can run `space` from anywhere in your terminal.

### Using Docker

Run the application using Docker without installing Python:

```bash
# Pull and run from GitHub Container Registry (once published)
docker run --rm ghcr.io/yourusername/space:latest

# Or build locally
docker build -t space .
docker run --rm space

# With custom environment variables
docker run --rm \
  -e SPACE_API_BASE_URL=http://api.open-notify.org \
  -e SPACE_ASTROS_ENDPOINT=/astros.json \
  space

# Using docker-compose
docker-compose up space

# With verbose logging
docker-compose up space-verbose
```

### Development Setup

For contributing or local development:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/space.git
cd space
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows (PowerShell):
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install the package with development dependencies:
```bash
pip install -e ".[dev]"
```

## Usage

Run the CLI application:

```bash
# Basic usage
space

# Verbose output (INFO level logging)
space -v

# Debug output (DEBUG level logging)
space -d

# Show version
space --version

# Show help
space --help
```

### Environment Variables

The application supports configuration via `.env` file for different environments (dev, staging, prod).

**Setup:**

1. Copy the example file to create your `.env`:
   ```bash
   cp .env.example .env
   ```

   On Windows:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit `.env` to configure your environment:
   ```bash
   # For development with a mock server
   SPACE_API_BASE_URL=http://localhost:8000
   SPACE_ASTROS_ENDPOINT=/api/v1/astros
   ```

3. Run the application (automatically loads `.env`):
   ```bash
   space
   ```

**Available Configuration:**

- `SPACE_API_BASE_URL` - API base URL (required)
- `SPACE_ASTROS_ENDPOINT` - Endpoint path (required)

**Note:**

- `.env` file is gitignored and safe for local configuration
- `.env.example` shows all available options (committed to git)
- Environment variables can also be set directly in your shell if preferred

## Development

### Project Structure

```
space/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── codeql.yml
│       └── release.yml
├── src/
│   └── space/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.py
│       └── space.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   └── test_space.py
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

### Running Tests

Run the test suite:

```bash
pytest
```

Run tests with coverage report:

```bash
pytest --cov=space --cov-report=term
```

Run tests with detailed coverage HTML report:

```bash
pytest --cov=space --cov-report=html
```

**Test Coverage:** The project maintains 100% code coverage with comprehensive unit tests.

### Code Formatting

Format code with Black and isort:

```bash
black .
isort .
```

### Pre-commit Hooks

Set up pre-commit hooks to automatically check code quality before commits:

```bash
# Install pre-commit hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

The pre-commit hooks will automatically run:
- Black (code formatting)
- isort (import sorting)
- flake8 (linting)
- mypy (type checking)
- bandit (security checks)
- Various file checks (trailing whitespace, YAML validity, etc.)

### Security Scanning

Run security checks:

```bash
# Check for known vulnerabilities in dependencies
pip-audit

# Run security analysis with bandit
bandit -r src -c pyproject.toml
```

### Type Checking

Run type checking with mypy:

```bash
mypy src
```

### Linting

Check code style with flake8:

```bash
flake8 src
```

## Dependencies

- **requests**: HTTP library for API calls
- **rich**: Terminal formatting and beautiful output
- **python-dotenv**: Load configuration from .env files
- **tenacity**: Retry logic with exponential backoff

### Development Dependencies

- **pytest**: Testing framework
- **pytest-cov**: Code coverage
- **black**: Code formatter
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Git hook scripts for code quality
- **bandit**: Security issue scanner
- **pip-audit**: Dependency vulnerability scanner

## Docker

### Building the Image

```bash
# Build the image
docker build -t space:latest .

# Build with specific version tag
docker build -t space:0.1.0 .
```

### Running with Docker

```bash
# Basic usage
docker run --rm space:latest

# With environment variables
docker run --rm \
  -e SPACE_API_BASE_URL=http://api.open-notify.org \
  -e SPACE_ASTROS_ENDPOINT=/astros.json \
  space:latest

# With verbose logging
docker run --rm space:latest -v

# With debug logging
docker run --rm space:latest -d
```

### Using Docker Compose

```bash
# Run default service
docker-compose up space

# Run with verbose logging
docker-compose up space-verbose

# Run with debug logging
docker-compose up space-debug

# Build and run
docker-compose up --build
```

### Image Details

- **Base Image**: python:3.11-slim
- **Size**: ~150MB (multi-stage build)
- **Security**: Runs as non-root user
- **Platforms**: linux/amd64, linux/arm64

## API

This project uses the [Open Notify API](http://open-notify.org/Open-Notify-API/People-In-Space/) to fetch real-time data about astronauts in space.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Victor Velasquez**
- Email: victorcop90@gmail.com

## Acknowledgments

- Open Notify API for providing space data
- Rich library for beautiful terminal output
