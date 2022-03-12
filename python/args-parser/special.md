一些特别的参数怎么添加
- 匹配所有剩余参数
```python
    parser.add_argument(
        "overrides",
        nargs="*",
        help="Any key=value arguments to override config values (use dots for.nested=overrides)",
    )
```
- 选择
```python
    parser.add_argument(
        "--cfg",
        "-c",
        choices=["job", "hydra", "all"],
        help="Show config instead of running [job|hydra|all]",
    )
```