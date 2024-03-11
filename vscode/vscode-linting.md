- [[linting]]
- 下方栏，打开python文件时
  - python字样左侧大括号就是
  - 大括号右侧是语言种类，可以自己选择
    - 应用：当错误把有注释的[[json]]-with-comments文件当作[[json]]文件，报错时，可以选择
- 功能
    - [[isort]]
    - [[ruff]]插件
      - 则可用[[ruff]] [[linting]]
    - [[python-typing]]
      - vscode自带type checker
      - [[mypy]]（规则集等可能不同）
    - 自动补充[[python-import]]
      - [[settings-json]]
        ```json
        "python.analysis.autoImportCompletions": true,
        "python.analysis.autoSearchPaths": true,
        // if "false", may be problematic regarding relative / absolute imports
        ```