- [参考](https://oi-wiki.org/lang/helloworld/)
# 在线编译运行
- [[wandbox]]
    - 选择C++，然后如图，发现可以正常使用
      - ![](helloworld.png)
      - 注意右边有`stdin`，可以有输入
    - 以上代码的文字版
      - 代码
        ```cpp
        #include<iostream>
        #include<stdio.h>
        using namespace std;
        int main(){
            int a;
            cin>>a;
            cout<<a+2<<endl;
            cout<<4;
            int n=0;
            printf("%d", n);
            scanf("%d", &n);
            printf("%d", n);
            return 0;
        }
        ```
      - 输入：`8`，`5`
- [[coderpad]]
# linux
- `sudo apt update && sudo apt install g++` 安装
- `g++ -v`查看[[version]]
- `g++ test.cpp -o test`输出，`./test`运行