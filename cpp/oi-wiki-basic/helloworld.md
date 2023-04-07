- 本文 https://oi-wiki.org/lang/helloworld/
配置基础环境和做minimun working example
- 如果懒得本地搞，可以上各种在线编译器
  - https://wandbox.org/
      - 选择C++，然后如图，发现可以正常使用
      - ![](helloworld.png)
        - 注意右边有`stdin`
      - 参考可用代码（表示了基本输入输出格式）
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
  - [[coderpad]]