# Hello appsec world file
# Author: Butters7

import typer


def main(name: str = typer.Option(..., prompt="Enter your name")):
    """Main function that greets the user."""
    print(f"Hello appsec world from @{name}")


if __name__ == "__main__":
    # Run the CLI application
    typer.run(main)
