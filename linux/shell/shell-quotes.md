- 前置
  - [[escape]]
- 参考
    - https://www.cnblogs.com/loki717/p/7358125.html
    - https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash
# 单双引号
## 简单观察
- 必须双引号
  - 字符串中有单引号，你就只能用双引号括了
  - 需要[[shell-expansion]]等，只能用双引号
- 可能双引号
  - `echo "\"'\" \""`，反正里面什么都可能有，顶多丑
- 适合单引号
  - 没有单引号，全部[[verbatim]]，方便
## 应用
- [[ssh/env-var]]中需要往文件输入
    ```sh
    for item in `cat /proc/1/environ | tr '\0' '\n'`
    do
    export $item
    done
    ```
    - 那么你可以
    ```sh
    echo "for item in \`cat /proc/1/environ | tr '\\0' '\\n'\`
    do
    export \$item
    done" >> /etc/profile
    ```
- 注意`~`的问题，参考[[shell-expansion]]
  - `~`裸露才会表示家，双引号是原样
    - `echo ~; echo "~"; ls ~; ls "~"`
  - 对比：[[6-env]]，`$var`双引号中表示变量，单引号中才是原样，不展开
# 反引号
- [[markdown/snippets]]
- <code>&#96;&#96;</code>
- 等价于`$()`
- [[meta-programming]]