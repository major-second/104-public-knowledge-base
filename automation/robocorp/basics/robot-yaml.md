- 前置
  - [[robocorp]], [[rcc]]
  - [[windows-python]]
  - 了解`python -c`，`python -V`
  - 体验[[my-first-robot]]中的两个robot
  - [[yaml]]
- [官网教程](https://robocorp.com/docs/setup/robot-structure)
## 典型设置
- minimal robot structure及`robot.yaml`的地位
  ```text
  ├── conda.yaml
  ├── .gitignore
  ├── output
  │   └── # Having a standard place for outputs is always good
  ├── robot.yaml
  └── tasks.robot
  ```
## 最简单的
- [官网教程](https://robocorp.com/docs/setup/robot-yaml-format)也很清楚
  - 至少需要`tasks - <任务名称> - <command | shell | robotTaskName>`和`artifactsDir`两个key
- 我们写出最小的能用的`robot.yaml`
  - [参考](../example/robot-yaml/minimal/robot.yaml)（虽然会报警告）
  - 各个key含义几乎都是自明的
- 这个robot
  - [[powershell-basics]]**进`robot.yaml`所在目录**后，用`rcc run`运行
  - 不能用vscode运行
    - vscode不够灵活，要求用conda环境，参考[[rcc]]
- 效果是使用默认`python`解释器`print`一行`hello world`
## 其他文件
- `ignoreFiles`字段用于指定忽略的文件
  - 参考[[special-files#dot-gitignore]]
  - 常用：
    ```yaml
    ignoreFiles:
      - .gitignore
    ```
- [[robocorp-conda-yaml]]
- [[dot-robot]]