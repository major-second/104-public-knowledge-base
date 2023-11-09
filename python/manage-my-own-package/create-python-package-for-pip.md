- Prerequisites
  - [[pip]]
  - [[init-dot-py]]
  - [[version]]
  - [Reference](https://www.freecodecamp.org/news/build-your-first-python-package/)
  - [Reference](https://docs.python-guide.org/writing/structure/)

## Creating Your Own Python Package
  1. Create a new directory, this will be the root directory of your package.
  2. Inside this directory, create a new Python file named `__init__.py`. This file is crucial as it helps Python recognize your directory as a package.
     1. This file can be left empty but it is generally a good practice to include the essential classes and functions of your package here.
     2. [[init-dot-py#Automatic Import of Variables]]
  3. In the root directory of your package, create a file named `setup.py`. In this file, you need to define the metadata of your package, such as the name, version, author, etc. Here is a basic example:
     - ```python
       from setuptools import setup, find_packages
    
       setup(
           name='YourPackageName',
           version='0.1',
           packages=find_packages(),
           install_requires=[
               # list of packages your package depends on
           ],
       )
       ```
  4. The essential part
     1. Besides `setup.py`, create another Python file named `example.py` in the root directory of your package. This file will contain the essential scripts of your package.
     2. Alternatively, you can create a new directory in the root directory of your package. Inside this new directory, create another `__init__.py` file and add various multiple files containing the essential scripts of your package.
  5. In the root directory of your package, run `pip install -e .` to install your package.
     1. Of course, you can do this in a [[conda]] environment
  6. Results
     1. [[pip]]
        1. `pip list` will display packages with local directories on the right
        2. `pip uninstall` can uninstall the package
     2. [[python]]
        1. After running the interpreter
           1. If it's a single file, like `example.py`, you can directly `import example`
           2. If it's a directory, like `example_dir` (which contains `__init__.py`), you can `from example_dir.a import b`
           3. If the files are scattered (not recommended), like directly `a.py, b.py` next to setup.py, you can directly `import a`, etc.
              - [Reference](https://docs.python-guide.org/writing/structure/)

- The advantage of this is that your package directory is not limited to the current directory
- Advanced improvements
   - [Reference](https://docs.python-guide.org/writing/structure/)
   - [[read-doc]]: `docs` directory, `README.md` file
   - `LICENSE`
   - [[special-files]]
   - [[unittest]]: `tests` directory
