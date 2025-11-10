# Contributing to Space 🚀

Thank you for your interest in contributing to Space! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant logs or screenshots

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Use cases and benefits
- Any implementation ideas you have

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Set up your development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\Activate.ps1 on Windows
   pip install -e ".[dev]"
   ```

3. **Make your changes**:
   - Write clear, readable code
   - Follow the existing code style
   - Add or update tests as needed
   - Update documentation if necessary

4. **Run the test suite**:
   ```bash
   pytest
   ```

5. **Format your code**:
   ```bash
   black .
   isort .
   ```

6. **Check for linting errors**:
   ```bash
   flake8 src
   mypy src
   ```

7. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Follow conventional commit format if possible:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `docs:` for documentation changes
     - `test:` for test additions/changes
     - `refactor:` for code refactoring
     - `style:` for formatting changes

8. **Push to your fork** and submit a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

9. **In your pull request**:
   - Provide a clear description of the changes
   - Reference any related issues
   - Include screenshots if applicable
   - Ensure CI checks pass

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for modules, classes, and functions
- Keep functions focused and concise
- Use meaningful variable and function names

### Testing

- Write tests for new features
- Maintain or improve code coverage
- Test edge cases and error conditions
- Use descriptive test names

### Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions/classes
- Update type hints
- Comment complex logic

### Commit Messages

Good commit message example:
```
feat: add support for filtering by spacecraft

- Add --spacecraft CLI argument
- Implement filtering logic in fetch_people_in_space
- Add tests for filtering functionality
- Update documentation
```

## Project Structure

```
space/
├── src/
│   └── space/           # Main package
│       ├── __init__.py  # Package initialization
│       ├── __main__.py  # CLI entry point
│       └── space.py     # Core functionality
├── tests/               # Test files
├── .github/
│   └── workflows/       # GitHub Actions workflows
├── pyproject.toml       # Project configuration
├── requirements.txt     # Dependencies
├── README.md
└── CONTRIBUTING.md
```

## Getting Help

If you need help:
- Check existing issues and pull requests
- Create a new issue with your question
- Provide as much context as possible

## Recognition

Contributors will be acknowledged in the project. Thank you for helping make Space better!
