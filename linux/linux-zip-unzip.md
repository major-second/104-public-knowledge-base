- https://zhuanlan.zhihu.com/p/511765254
- zip, unzip
    - 前置：`sudo apt install zip unzip`
    - 压缩成`.zip`
      - `zip <名字>.zip <待压缩文件或文件夹列表>`
        - 有文件夹，需要递归压缩里面的东西，则`zip -r ...`
        - 排除：`-x`
          - 如果需要排除某个目录下所有，则`zip -r tmp.zip dir -x "dir/subdir/*"`
          - 不能是`dir/subdir`，因为`dir/subdir`不是文件
          - 不能是`dir/subdir/*`不加引号，因为你`echo dir/subdir/*`就知道什么意思了。这是没有[[escape]]的错误！
    - 解压：`unzip <名字>.zip`
      - `unzip <名字>.zip -d <新名字>`
- tar
    - `tar -xvf file.tar`
    - `tar -xzvf file.tar.gz`
- gzip
  - `gzip -d file.gz`
- 可以结合[[scp]]使用，加快跨机器拷贝速度
- 可以结合[[xxd-diff]]用文本传递整个文件夹