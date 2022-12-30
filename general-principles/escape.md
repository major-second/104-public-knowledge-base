# 理论
- [[encode-decode]]“码”不够了
# 实例
- [[meta-programming]]
- [[regex]]中`\.`才是一个点字符，等等
- shell转义非常繁琐，有时你可能都得考虑[[workaround]]……
  - [[11-basic-scripting-partA]]中例子（单双引号区别）
    - `echo "$SHELL"; echo '$SHELL'; echo "\$SHELL"`
  - [[shrc]]中例子
    - `alias monitor-disk="watch -d -n 60 'du -h ~/ | grep \"[0-9]G\\s\"; echo; du -h ${ak_path} | grep \"[0-9]G\\s\"; echo; ls ${ak_path}; echo; ls ~'"`
  - [[linux/zip-unzip]]中例子
    - `zip -r tmp.zip dir -x "dir/subdir/*"`
      - 可以尝试`echo ./*; echo "./*"`看区别
  - [[wsl-command]]中的例子
    - 这是[[powershell/basics]]转义和[[echo]]转义结合
    - `wsl -e bash -c 'echo -e "[boot]\\nsystemd=true" | sudo tee /etc/wsl.conf'`，共转义2次
- `python`的[[f-string]]中，大括号等需要转义