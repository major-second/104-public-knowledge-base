前置：
- [[robocorp/installation]]中的命令行工具`rcc`安装（否则只能用vscode集成的不够灵活的rcc）
- 体验[[my-first-robot]]中的两个robot
- [[yaml]]
- [[create-env-yaml]]

内容
- [官网教程](https://robocorp.com/docs/setup/robot-structure)
## 典型minimal robot structure及`robot.yaml`的地位
```text
├── conda.yaml
├── .gitignore
├── output
│   └── # Having a standard place for outputs is always good
├── robot.yaml
└── tasks.robot
```
## 最简单的`robot.yaml`
- 在`example-google-image-search`中的各个key含义几乎都是自明的
- [官网教程](https://robocorp.com/docs/setup/robot-yaml-format)也很清楚
  - 至少需要`tasks - <任务名称> - <command | shell | robotTaskName>`和`artifactsDir`两个key
- 所以我们写出最小的能用的`robot.yaml`：在`104-public-knowledge-base\automation\robocorp\example\robot-yaml\minimal\robot.yaml`（虽然会报警告）
- 这个robot可以进`robot.yaml`所在目录用`rcc run`运行，不能用vscode运行（vscode不够灵活，要求conda环境）