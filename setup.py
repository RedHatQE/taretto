from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

LONG_DESC = """
Targetted tooling for testing, currently offering tools for Web UI navigation and interaction.
"""

if __name__ == "__main__":
    setup(
        name="taretto",
        description="Targetted tooling for testing, currently offering tools for Web UI navigation and interaction.",
        license="GPL",
        url="https://github.com/RedHatQE/taretto",
        version="0.5",
        author="RedHatQE",
        author_email="psavage@redhat.com",
        maintainer="Pete Savage",
        maintainer_email="psavage@redhat.com",
        keywords=['Testing', 'Widget', 'Navigation'],
        long_description=LONG_DESC,
        packages=['taretto'],
        package_dir={"": "src"},
        classifiers=CLASSIFIERS,
)
