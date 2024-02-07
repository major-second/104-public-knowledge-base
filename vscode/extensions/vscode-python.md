- 注意版本可能要和`python`版本相适配
- 任意打开`.py`文件，右下角就可选解释器
- [[settings-json]]
  - `pylance`解析时，如果你这个库有需要额外添加的[[sys-path]]，想让`pylance`能识别到，就不妨在这个库的`.vscode/settings.json`添加这种
  ```json
  {
      "python.analysis.extraPaths": [
      "${workspaceFolder}/pattern_recognition"
      ],
  }
  ```
- 解析不到东西，没法`ctrl + 左键`点进去很烦！
  - 除了刚刚的[[settings-json]]问题外，还有可能[[refresh]]一下就好了（`ctrl + W`关掉然后重新打开文件）
- [[launch]]中`launch.json`可能配置的东西：
  - 运行什么文件
  - 在什么目录下运行（防止`python`找不到包）
    - 例如
      - `"cwd": "${workspaceFolder}/anticipation"`
      - `"cwd": "${fileDirname}"`
      - 就不在项目根目录运行
    - 这里参考[[sys-path]]
    - 时至2023.1 vscode个别时候（我自己的wsl中就有）有个bug：对于python debug [[terminal]]，第一次launch时没法正常读取`cwd`. 需要关了重新launch，让他自动在这个python debug终端再跑一次。不能垃圾桶掉这个终端
  - 参数`"args"`
    - 这样就不用每次重新复制长串命令
    - 例如本来的参数列表为`--id 1 --learning-rate 0.0001`，对应的你要写成`"args": ["--id", "1", "--learning-rate", "0.0001"]`
    - `"args": "${command:pickArgs}"`：手动输入
  - `"justMyCode": false`：逐步运行进第三方库
  - `"python"`
    - 指定[[python-interpreter]]
    - 可以
      - 先`conda env list` / `which`（linux专用）
      - 快速找到解释器路径
      - 再填入这里
  - `"env"`: [[6-env]]环境变量
    - 一个用途：设置`PYTHONPATH`环境变量（参考[[sys-path]]），防止找不到包
    - 此处可以使用`${workspaceFolder}`变量，方便表示当前目录
  - `"logToFile": true`选项：[[general-programming/logs]]中提到过