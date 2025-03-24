from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

import typer

T = TypeVar("T")


class SingletonMeta(type):
    """A metaclass for creating singleton classes."""

    _instances: Dict[Type, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseApp(ABC):
    """Abstract base class for application instances."""

    @abstractmethod
    def register_command(self, command: Any) -> None:
        """Register a command with the application."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Run the application."""
        pass


# Create a proper metaclass that combines ABC and Singleton functionality
class AppMeta(SingletonMeta, type(ABC)):
    """Metaclass that combines SingletonMeta and ABC metaclass."""

    pass


class App(BaseApp, metaclass=AppMeta):
    """Singleton application class wrapping Typer CLI functionality.

    This class implements the Singleton pattern to ensure only one App instance
    exists throughout the application. It wraps Typer's CLI functionality
    and provides a consistent interface for registering commands and running the app.
    """

    def __init__(
        self,
        name: str = "uvp",
        help_text: str = "All-in-one tool for managing and deploying Python projects",
    ) -> None:
        """Initialize the App instance.

        Args:
            name: The name of the CLI application.
            help_text: The help text to display.
        """
        self._app = typer.Typer(
            name=name,
            help=help_text,
            add_completion=True,
        )
        self._commands: List[str] = []

    @property
    def app(self) -> typer.Typer:
        """Get the Typer application instance.

        Returns:
            The Typer application instance.
        """
        return self._app

    def command(self, *args: Any, **kwargs: Any) -> Callable:
        """Decorator to register a command with the application.

        Args:
            *args: Arguments to pass to the Typer command.
            **kwargs: Keyword arguments to pass to the Typer command.

        Returns:
            The command decorator.
        """
        return self._app.command(*args, **kwargs)

    def register_command(self, command: Any) -> None:
        """Register a command with the application.

        Args:
            command: The command to register.
        """
        self._app.add_typer(command)
        if hasattr(command, "name"):
            self._commands.append(command.name)

    def callback(self, *args: Any, **kwargs: Any) -> Callable:
        """Decorator to register a callback with the application.

        Args:
            *args: Arguments to pass to the Typer callback.
            **kwargs: Keyword arguments to pass to the Typer callback.

        Returns:
            The callback decorator.
        """
        return self._app.callback(*args, **kwargs)

    def create_group(self, name: str, help_text: Optional[str] = None) -> typer.Typer:
        """Create a new command group.

        Args:
            name: The name of the command group.
            help_text: The help text to display for the group.

        Returns:
            A new Typer instance representing the command group.
        """
        group_app = typer.Typer(name=name, help=help_text)
        self.register_command(group_app)
        return group_app

    def get_registered_commands(self) -> List[str]:
        """Get the list of registered command names.

        Returns:
            A list of registered command names.
        """
        return self._commands

    def run(self) -> None:
        """Run the application."""
        self._app()


# Create the singleton app instance
app = App()
