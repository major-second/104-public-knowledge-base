制造、查看日志非常重要！自己方便看[[readability]]，别人方便看和诊断
- 查看
  - 查看日志有用的例子
    - 比如[[assets]]中查看终端错误信息
    - 比如[[lightning/logs]]
    - 再比如[github issue](https://github.com/microsoft/debugpy/issues/102)说的打印并查看日志错误信息，解决问题
      - 核心：`"logToFile": true`选项
- 制造日志的方法
  - 例子
    - 比如[[11-basic-scripting-partA]]说的`>>`或`>`重定向
    - 比如商业软件[[aida64]]给出报告
  - 等级
    - 常见`[0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']`
    - 设置`DEBUG`也能看到`INFO`，以此类推
    - 例如[[nbextension]]中`jupyter contrib nbextension install --Application.log_level=30 --user`
    - 设置太高了可能就是[[silent]]，设置太低就太啰嗦