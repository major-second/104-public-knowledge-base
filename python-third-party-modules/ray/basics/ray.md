- 前置
  - [[pip]]
  - 了解[[process-thread]] [[memory]]
    - ray就是很好的共享内存，多进程，并行手段
- 安装
  - `pip install ray[default]`
  - python脚本中
    - ```python
      import ray
      ray.init()
      ```
    - 注意`init`不能两次
      - 特别[[jupyter-notebook]]中需要注意
- https://docs.ray.io/en/latest/ray-core/walkthrough.html