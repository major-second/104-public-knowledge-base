- 参考[[shell-export]]
## source
- `source`和直接运行不同
- [参考](https://blog.csdn.net/weixin_44815943/article/details/109353439)
- 在[[shell]]用不了`source`时的[[workaround]]：`eval $(cat my-script.sh)`，是[[meta-programming]]
## 其它
- 作用域：进程！
  - [[process-thread]]
- [[CRUD]]
  - 查询
    - `set`可以查询所有，还可以结合[[find-grep]]
    - [[python]] [[os-shutil]]
  - 增加参考[[shell-export]]（`export K=V`区分`K=V`）
  - 删除使用`unset`
## 6.7 数组变量
- [[shell-array]]
## 特殊变量
- `BASH_SOURCE`
  - 应用：`SCRIPT_DIR=$(dirname $(realpath "${BASH_SOURCE[0]}"))`
- `HOSTNAME`：不是所有[[shell-type]]都有哈
- `PATH`
- `LD_LIBRARY_PATH`