import os

import click
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter


@click.group(help="Helper commands for application installation")
def main():
    """Main application group"""
    pass


@click.option("--path", default=".", help="Path to create the new application in")
@main.command("create", help="Makes a skeleton of a new application")
def make_application(path):
    print(
        "Git initialize is required for application to wo   rk, select 'y' at 'initialize_git' "
        "prompt to run this automatically."
    )
    package_dir, _ = os.path.split(os.path.dirname(os.path.realpath(__file__)))
    try:
        plugin_path = cookiecutter(os.path.join(package_dir, "application_skel"), output_dir=path)
        print("Application created at {}".format(plugin_path))
    except OutputDirExistsException:
        print("Output dir already exists, application create failed")
