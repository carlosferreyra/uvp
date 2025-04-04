# UVP (UV Project)

All-in-one tool for managing and deploying Python projects using the modern `uv` package manager.

## Features

- Modern Python project management using `uv`
- Simplified dependency management
- Fast project setup and configuration
- PEP standards compliant

## Installation

```bash
uv tool install uvp # Install the latest version
```

```bash
uvx uvp # run the tool in an isolated environment
```

## Requirements

- Python 3.10 or higher
- `uv` package manager

## Usage

```bash
uvp [command] [options]
```

See the command reference below for available commands and options.

## Development

To set up the development environment:

```bash
uv sync
uv pip install -e ".[dev]"
uv run uvp --help
```

### Running Tests

```bash
uv run pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
