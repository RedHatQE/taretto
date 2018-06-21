from setuptools import setup

if __name__ == "__main__":
    setup(
        setup_requires=["setuptools_scm"], use_scm_version=True, package_dir={"": "src"}
    )
