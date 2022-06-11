做事有头有尾特别重要！
- 方法
  - python的`try-finally`
  - python上下文管理器等
- 重要性：如果不做，可能导致
  - [[mujoco-py]]的锁没删掉
  - [[file-baton]]的锁没删掉
  - [[automation/trivial-mistakes]]
- 不做的反例：暴力[[process]]杀进程，可能导致[[process]]提到的不良后果。往往需要[[refresh]]解决