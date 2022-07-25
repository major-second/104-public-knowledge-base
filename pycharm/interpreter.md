右上角齿轮 - Settings - 搜索Interpreter
看到添加解释器、选择项目所用解释器的方法
- “添加”（加号按钮）
  - 可能是新建虚拟环境（New environment）
    - 注意，你已经用[[commands]]创建好的环境不属于此类，属于下面一类
  - 也可能是用已有的虚拟环境（Existing environment）
    - 已有解释器所在目录：例如对于[[commands]]得到的环境，名字是`foo`，则在linux下`conda`安装目录的`envs/foo/bin/python`
    - 其中，`conda`安装目录往往是默认的`~/anaconda3`（也有可能是`miniconda`等，常用于docker中的[[conda]]）