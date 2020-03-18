PyAChem
=======

A library implementing various Artificial Chemistry utilities and algorithms


development
-----------

Install using pip including development extras

```sh
pip install -e .[dev]
```

Enable pre-commit hooks with:

```sh
pre-commit install
```

Freeze dependencies with:

```sh
pip-compile
```

Run tests with:

```sh
pytest
```

Test coverage with:

```sh
coverage run --source=pyachem -m pytest
coverage report -m
```

Type checking with:

```sh
mypy .
```

See dependencies with:

```sh
pipdeptree
```
