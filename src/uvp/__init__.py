"""UVP - All-in-one tool for managing and deploying Python projects."""

__version__ = "0.0.1"

# Import core module and create app instance
from uvp.core import app as app

# Import commands to ensure they're registered early


def hello() -> str:
    return "Hello from uvp!"
