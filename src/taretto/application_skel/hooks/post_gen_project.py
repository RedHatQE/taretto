import subprocess

git_init = "{{cookiecutter.initialize_git}}"
git_init = git_init.lower()
git_init = git_init[0]

if git_init == 'y':
    args = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Initial Commit"],
        ["git", "tag", "0.0.1"],
    ]
    for arg_list in args:
        proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE)
        proc.wait()
        assert proc.returncode == 0

elif git_init == "n":
    print(
        "Before this plugin is installable you are required to"
        " initialize a git repo, add/commit changes to it and add an initial tag."
    )
else:
    print("Invalid option deleting plugin")
    raise Exception("Invalid option given")
