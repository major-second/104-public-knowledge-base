前置：
- [[power-automate/var]]

- 开：
    - 丑的：桌面打开、开始菜单打开
      - 但也有好处：泛化性强，稳定，便于处理带参数[[快捷方式]]，如anaconda powershell prompt
    - 本质的方法：启动app，存储变量，再Focus window
      - 最典型的好处：方便定位window
      - 但同时有多个窗口时retrieve handle可能有问题
- 关：
  - UI按叉
  - `Alt+F4`
  - 本质的方法：用handle或类型关