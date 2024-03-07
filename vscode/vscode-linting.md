- [[linting]]
- 下方栏，打开python文件时python字样左侧大括号就是
- 功能
    - [[isort]]
    - [[ruff]]插件则可用[[ruff]]
    - [[python-typing]]
      - 自带checker
      - [[mypy]]
    - 自动补充[[python-import]]
      - [[settings-json]]
        ```json
        "python.analysis.autoImportCompletions": true,
        "python.analysis.autoSearchPaths": true,
        // if "false", may be problematic regarding relative / absolute imports
        ```