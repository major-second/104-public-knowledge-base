- [文档](https://intel.github.io/scikit-learn-intelex/latest/)
- 牺牲灵活，换取速度
- 前置
  - [[sklearn]]
  - [[python-m]]
  - [[pip-install]]
    - `pip install scikit-learn-intelex`

- Without editing the code of a scikit-learn application by using the following command line flag:
    ```
    python -m sklearnex my_application.py
    ```
- Directly from the script:
    ```
    from sklearnex import patch_sklearn
    patch_sklearn()
    ```