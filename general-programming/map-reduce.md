- [参考](https://zhuanlan.zhihu.com/p/82399103)
- 实现
  - [[functools]]
  - Spark, Hadoop （虽然有点年头了）
  - [[find-grep]]
    - `while [[ 1 -eq 1 ]]; do sleep 2; nvidia-smi | grep "[4-7]\s\+N/A\s\+N/A" | awk '{print $5}' | xargs sudo kill -9; done`定期清理后4张卡程序
    - 这个在写脚本思想上有map reduce意味
- 理论
  - [[rnn#parallelizing]]中用到！
  - 联系[[stream-computing]]