- 前置[[python-import]]
- [[init-dot-py]]中常用，参考[[init-dot-py]]

## Python Relative Import

 ### Typical Usage
 Relative import in Python is typically used in `__init__.py` files to import modules from the same package. This is done using the syntax `from .module import name`. Here, `.` represents the current package, `module` is the name of the module in the same package, and `name` is the name of the function, class, or variable you want to import.

 For example, if you have a function `func` in a module `mod` in the same package, you can import it in the `__init__.py` file as follows:
 ```python
 from .mod import func
 ```

 ### Common Errors and When Not to Use
 A common error when using relative import is attempting to use it without a parent package. This usually happens when you try to run a module inside a package individually as a script. In such cases, Python doesn't recognize the parent package and hence, the relative import fails. Therefore, relative import is not appropriate to use when you want to run modules individually as scripts. Since relative import depends on the parent package, running modules individually breaks the relative import. In such cases, it's better to use absolute import by specifying the full path to the module.