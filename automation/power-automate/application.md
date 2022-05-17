前置：
- [[power-automate/var]]

- 开：
    - 丑的：桌面打开、开始菜单打开
    - 本质的方法：启动app，存储变量，再Focus window
      - 但同时有多个窗口时retrieve handle可能有问题
- 关：
  - UI按叉
  - `Alt+F4`
  - 本质的方法：用handle或类型关