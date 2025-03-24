"""Base commands for the uvp CLI application."""

from typing import List

import typer

from uvp.core import app


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """UVP: All-in-one tool for managing and deploying Python projects.

    Built with uv as the main package manager.
    """
    # Show help message if no subcommand is invoked
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


@app.command()
def version() -> None:
    """Show the version of uvp."""
    import importlib.metadata as metadata

    try:
        version = metadata.version("uvp")
        typer.echo(f"uvp version: {version}")
    except metadata.PackageNotFoundError:
        typer.echo("uvp version: development")


@app.command()
def info() -> None:
    """Show information about the uvp installation."""
    import platform
    import sys

    typer.echo("UVP Information:")
    typer.echo(f"Python version: {sys.version}")
    typer.echo(f"Platform: {platform.platform()}")
    typer.echo(f"Commands: {', '.join(app.get_registered_commands())}")

    # Display uv version if available
    try:
        import subprocess

        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            typer.echo(f"uv version: {result.stdout.strip()}")
        else:
            typer.echo("uv: Not found")
    except FileNotFoundError:
        typer.echo("uv: Not installed")


# Create a group for package management commands
pkg_app = app.create_group("pkg", help_text="Package management commands")


@pkg_app.command("install")
def pkg_install(
    package: List[str] = typer.Argument(..., help="Package(s) to install"),
    dev: bool = typer.Option(
        False, "--dev", "-d", help="Install as development dependency"
    ),
) -> None:
    """Install packages using uv."""
    import subprocess
    import sys

    cmd = ["uv", "pip", "install"]
    if dev:
        cmd.append("--dev")
    cmd.extend(package)

    typer.echo(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        typer.echo("✅ Packages installed successfully")
    except subprocess.CalledProcessError:
        typer.echo("❌ Failed to install packages", err=True)
        sys.exit(1)
