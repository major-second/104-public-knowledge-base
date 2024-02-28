- 参考链接
  - [[resource-management/commands]]
  - [[torch-cpu-usage]]
- [参考](https://zhuanlan.zhihu.com/p/372564248)
  - `cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l`物理cpu个数
  - `cat /proc/cpuinfo| grep "cpu cores"| uniq`核数
  - `cat /proc/cpuinfo| grep "processor"| wc -l`逻辑cpu个数
    - 可以提供多少[[process-thread]]
      - [参考](https://zhuanlan.zhihu.com/p/591815544)
    - [[python]]没有真正的多线程，只有[[multiprocessing]]，因此这就是可以开的进程数。关联：[[multiprocessing-minimum]]等
# num-threads
- 刚刚说的逻辑cpu个数就是这里的线程数
  ```
  os.environ ['OMP_NUM_THREADS'] = str(cpu_num)
  os.environ ['OPENBLAS_NUM_THREADS'] = str(cpu_num)
  os.environ ['MKL_NUM_THREADS'] = str(cpu_num)
  os.environ ['VECLIB_MAXIMUM_THREADS'] = str(cpu_num)
  os.environ ['NUMEXPR_NUM_THREADS'] = str(cpu_num)
  ```