import click

from {{cookiecutter.application_name}}.scripting.ipyshell import main as shell_main


@click.group()
def cli():
    pass


cli.add_command(shell_main, name="shell")


if __name__ == "__main__":
    cli()
