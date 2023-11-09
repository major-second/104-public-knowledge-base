- Preparatory Knowledge
  - [[python-import]]
  - [Reference](https://www.geeksforgeeks.org/create-access-python-package/)

# Overview
- A directory is identified as a package in Python if it includes an `__init__.py` file. This file is executed when the package is imported and can contain any Python code.
- The [[python-import]] mainly focuses on individual files.

## Automatic Import of Variables

To access a variable directly from a file within a package, it needs to be imported in the `__init__.py` file.

For instance, to access the variable `a_number` from the file `b.py` within the `example` package, add the following line to your `__init__.py` file:

```python
from .b import a_number
```

Then, `a_number` can be accessed like this:

```python
import example
print(example.a_number)
```

- The syntax `import .a` is not correct.
- Using `import a` might lead to a runtime error due to the issues outlined in [[python-import]].
  - Even if you import something from a non-local path, the entire program still operates on the local path.

## An Empty `__init__.py` and Manual Import of Variables

An empty `__init__.py` file indicates to Python that a directory should be considered as a package. This allows you to import modules from that directory using the package import syntax.

`a` in [this file](example/a.py) was not imported in the [init-dot-py file](example/__init__.py), but it can still be accessed by importing it manually.

```python
from example.a import a

print(a)
```

However, an empty `__init__.py` file doesn't automatically import variables, functions, or classes from other files in the package. You need to explicitly import them in the `__init__.py` file if you want them to be directly accessible from the package.
