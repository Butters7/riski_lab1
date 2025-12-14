import typer


def main(name: str = typer.Option(..., prompt="Enter your name")):
    print(f"Hello appsec world from @{name}")


if __name__ == "__main__":
    typer.run(main)
