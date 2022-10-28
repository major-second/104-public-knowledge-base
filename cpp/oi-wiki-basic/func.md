前置[[var]]

https://oiwiki.org/lang/func/

- 若先声明再定义。声明只需要`int some_function(int, int);`这种
- 也可以声明和定义放一起
- 注意：
  - 传值vs**传引用**：`foo(int& x, int& y)`
  - `main`的参数和返回值和外部（`shell`调用之类）有关，比如命令行参数
  - 非`void`函数必须每个路径都有返回值（否则编译不通过）
  - 返回：只要运行到`return`，后面的就都不管
    - 所以可以少很多`else`
    - 尽量减少`else`的[典型例子](https://leetcode.cn/problems/regular-expression-matching)，基本思想就是“特判直接返回”
```cpp
class Solution {
public:

    bool matchChar(char a, char b){
        return a==b || b=='.';
    }
    bool isMatch(string s, string p) {
        int np = p.size();
        int ns = s.size();
        if (!np) return !ns;

        bool hard = np==1 || p[1]!='*';

        if (hard) {
            if (!ns) return false;
            if (not matchChar(s[0],p[0])) return false;
            return isMatch(s.substr(1,ns-1),p.substr(1,np-1));
        }

        char p_first = p[0];
        p = p.substr(2,np-2);
        if (isMatch(s,p)) return true;
        while(!s.empty()){
            if (not matchChar(s[0],p_first)) return false;
            s = s.substr(1,ns);
            if (isMatch(s,p)) return true;
        }
        return false;
    }
};
```
注：最佳方法参见[[dp]]