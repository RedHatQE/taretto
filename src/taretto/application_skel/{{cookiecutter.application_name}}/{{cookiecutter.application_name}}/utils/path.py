"""Project path helpers

Contains `pathlib.Path` objects for accessing common project locations.

Paths rendered below will be different in your local environment.
"""
import importlib.util
from pathlib import Path

_{{cookiecutter.application_name}}_package_dir = Path(importlib.util.find_spec("{{cookiecutter.application_name}}").origin).parent

#: The project root, ``{{cookiecutter.application_name}}/``
PROJECT_PATH = _{{cookiecutter.application_name}}_package_dir

#: conf yaml storage, ``{{cookiecutter.application_name}}/conf/``
CONF_PATH = PROJECT_PATH / "conf"

#: datafile storage, ``{{cookiecutter.application_name}}/data/``
DATA_PATH = PROJECT_PATH / "data"

#: doc root, where these file came from! ``{{cookiecutter.application_name}}/docs/``
DOCS_PATH = PROJECT_PATH / "docs"

#: log storage, ``{{cookiecutter.application_name}}/log/``
LOG_PATH = PROJECT_PATH / "log"

#: results path for performance tests, ``{{cookiecutter.application_name}}/results/``
RESULTS_PATH = PROJECT_PATH / "results"

#: patch files (diffs)
PATCHES_PATH = DATA_PATH / "patches"

#: interactive scripts, ``{{cookiecutter.application_name}}/scripts/``
SCRIPTS_PATH = PROJECT_PATH / "scripts"

#: interactive scripts' data, ``{{cookiecutter.application_name}}/scripts/data``
SCRIPTS_DATA_PATH = SCRIPTS_PATH / "data"

#: jinja2 templates, use with ``jinja2.FileSystemLoader``
TEMPLATE_PATH = DATA_PATH / "templates"

#: orchestration datafile storage, ``{{cookiecutter.application_name}}/data/orchestration``
ORCHESTRATION_PATH = DATA_PATH / "orchestration"

#: resource files root directory, ``{{cookiecutter.application_name}}/data/resources``
RESOURCES_PATH = DATA_PATH / "resources"


def get_rel_path(absolute_path):
    """Get a relative path for object in the project root

    Args:
        absolute_path: An absolute path to a file anywhere under `PROJECT_PATH`

    Note:

        This will be a no-op for files that are not in `PROJECT_PATH`

    """
    # Convert the path to a Path object (if it's already a Path, this line does nothing)
    target_path = Path(absolute_path)
    try:
        # Path.relative_to() raises ValueError when a relative path cannot be calculated
        return target_path.relative_to(PROJECT_PATH)
    except ValueError:
        return absolute_path
