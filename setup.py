from setuptools import setup

setup(
    name="pyachem",
    version="1.0.0",
    author="Adam Faulconbridge",
    author_email="afaulconbridge@googlemail.com",
    packages=["pyachem"],
    description="Artificial Chemistry utilities and algorithms.",
    long_description=open("README.md").read(),
    install_requires=["python-igraph"],
    extras_require={
        "dev": [
            "pytest-cov",
            "flake8",
            "pylint",
            "pip-tools",
            "pipdeptree",
            "pre-commit",
            "mypy",
        ],
    },
)
