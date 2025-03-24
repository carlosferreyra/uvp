"""Main entry point for the uvp CLI application."""

from uvp.core import app


def main() -> None:
    """Entry point for the application."""
    app.run()


if __name__ == "__main__":
    main()
