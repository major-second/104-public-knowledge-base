## `launch.json`
`launch.json`可以指定运行时的各种配置。比如
- 运行什么文件
- 在什么目录下运行（防止`python`找不到包）
  - 例如`"cwd": "${workspaceFolder}/anticipation"`，就不在项目根目录运行
  - 参考[[sys-path]]
- 参数`"args"`
  - 这样就不用每次重新复制长串命令
  - 例如本来的参数列表为`--id 1 --learning-rate 0.0001`，对应的要写成`"args": ["--id", "1", "--learning-rate", "0.0001"]`
- `"justMyCode": false`：逐步运行进第三方库
- `"python"`: 指定python解释器（可以结合`which`命令快速找到解释器）
- `"env"`: [[6-env]]环境变量
  - 一个用途：设置`PYTHONPATH`环境变量（参考[[sys-path]]），防止找不到包
  - 此处可以使用`${workspaceFolder}`变量，方便表示当前目录
- `"logToFile": true`选项：[[logs]]中提到过
## 新建配置
- 比如想要用`launch.json`中的一套配置去表示一个`python -m 某某`命令以方便复用。假设目前还没有`launch.json`文件，第一次创建
  - `python -m`含义参考[[module-launch]]
  - `Ctrl + Shift + D` - 左侧create a launch.json file - 上方选择Module - 选择源码文件路径
  - 进去`launch.json`之后，可以看到`"name"`字段，可以自定义名称，就能显示在左上角绿色播放键旁边![](launch.png)
- 已有`launch.json`时
  - 编辑器打开`launch.json`，旁边有蓝色`Add Configuration...`按钮
  - 点击后，也可以上方选择相应模板，快速添加configuration
## 解释器
比如`conda activate <名字>`，`which python`找到python解释器
然后`Ctrl + Shift + P`，打`interpreter`，就找到选解释器的命令了。对照着刚刚`which python`的输出选解释器即可
- 注：刚刚说`launch.json`中的`"python"`字段会覆盖这里的设置。当两者不同时，可能造成vscode无法解析你的`import`. 所以不推荐两者不同