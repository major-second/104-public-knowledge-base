- [参考](https://zhuanlan.zhihu.com/p/108477489)
  - > gflags的flags可以分散到各个源文件而不是只在一个地方，也就是说只要是和定义了指定flags的源文件链接的其他文件都可以使用这个flags，这是灵活而又强大的，但这也是危险的，如果两个文件定义的flags一样，那么当它们链接在一起的时候将会出错
- 用法
  - 安装库
    - `sudo apt-get install libgflags-dev`
  - [写法](gflags_example.cpp)参考
  - [[linux-cpp-compilers]]使用
    - 需[[cpp-linking]]库
    - `g++ gflags_example.cpp -lgflags -o test`
  - 结果：`test` [[binary-executable]]
    - 输入
      - `./test -test_b -test_s 1`
    - 输出
      - `1default`
- 应用
  - [[cpp-debug]]
# 其它
## 设置方式
- bool
```sh
a.out --is_handsome
a.out --nois_handsome
a.out --is_handsome=true
a.out --is_handsome=false
```
- string
```sh
a.out --hobby="play football"
a.out -hobby="play football"
a.out --hobby "play football"
a.out -hobby "play football"
```
## 不影响[[cpp-cmd-line-args]]
```cpp
int main(int argc, char** argv) {
    gflags::ParseCommandLineFlags(&argc, &argv, true);
    ...
```