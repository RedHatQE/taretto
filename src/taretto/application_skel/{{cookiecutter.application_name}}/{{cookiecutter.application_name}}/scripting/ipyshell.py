import click
from IPython.terminal.interactiveshell import TerminalInteractiveShell

# TODO
IMPORTS = [
    "from {{cookiecutter.application_name}}.base.application.implementations.web_ui import ViaWebUI",
]


@click.command(help="Open an IPython shell")
def main():
    print("Welcome to IPython designed for running {{cookiecutter.application_real_name}} code.")
    ipython = TerminalInteractiveShell.instance()
    for code_import in IMPORTS:
        print("> {}".format(code_import))
        ipython.run_cell(code_import)
    from {{cookiecutter.application_name}}.utils.path import CONF_PATH

    custom_import_path = CONF_PATH / "{{cookiecutter.application_name}}_python_startup.py"
    if custom_import_path.exists():
        with open(custom_import_path, "r") as custom_import_file:
            custom_import_code = custom_import_file.read()
        print("Importing custom code:\n{}".format(custom_import_code.strip()))
        ipython.run_cell(custom_import_code)
    else:
        print(
            "You can create your own python file with imports you use frequently. "
            "Just create a conf/{{cookiecutter.application_name}}_python_startup.py file in your repo. "
            "This file can contain arbitrary python code that is executed in this context."
        )
    ipython.interact()


if __name__ == "__main__":
    main()
