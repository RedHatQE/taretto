import click

from taretto.scripting.application import main as app_main


@click.group()
def cli():
    pass


cli.add_command(app_main, name="application")

if __name__ == "__main__":
    cli()
