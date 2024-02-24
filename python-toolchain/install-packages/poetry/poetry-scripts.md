```toml
[tool.poetry.scripts]
my_command = "my_package_name.module_name:func_name"
```

- 然后在[[poetry-shell-run]]中，`my_command args`
- 相当于python作为[[shell]]的[[backend]]
- [[argparse]]使得可以加参数

    - ```python
      import argparse
      def main():
          parser = argparse.ArgumentParser(description='Show example dataframe for a dataset type.')
          parser.add_argument('dataset_type_id', type=str, help='Dataset type id', choices=FUTURE_DATASET_TYPE_IDS)
          args = parser.parse_args()
          show_example_df(args.dataset_type_id)
      ```