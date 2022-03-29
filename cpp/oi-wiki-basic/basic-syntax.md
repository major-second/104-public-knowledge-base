- 前置[[helloworld]]

https://oiwiki.org/lang/basic/
## 关于头文件
- `cstdio`就是`stdio.h`的意思
- 自己的头文件用`"文件名.h"`，引号而不是尖括号
  - 放到`.cpp`同一个目录，或者通过编译命令`-I`指定路径
## 输入输出snippet
```cpp
int a;
cin >> a;
cout << a << endl;
```
```cpp
int x, y;
scanf("%d%d", &x, &y);
printf("%d\n%d", y, x);
```
## `#define`
### 带参数的宏
`#define sum(x, y) ((x) + (y))`
是傻瓜暴力文本替换，所以要狂加括号
### 常见带参数宏
```cpp
#define int long long
#define For(i, l, r) for (int i = (l); i <= (r); ++i)
#define pb push_back
#define mid ((l + r) / 2)
```
### `#define`和`-D`关系
```cpp
#ifdef LINUX
// code for linux
#else
// code for other OS
#endif
```
编译时`-DLINUX`选项和其呼应