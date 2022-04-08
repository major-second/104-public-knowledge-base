- 前置[[var]]

https://oiwiki.org/lang/loop/
`while(){}`
`for(;;){}`（特别注意不是逗号）
`break`在`for`循环中也能用，但是是到“更新”（`i++`）那里，而非直接跳出
- 一个好用的snippet：排除重复元素的循环！
https://leetcode-cn.com/problems/4sum/submissions/
4行一组。例如
```cpp
int former_i = INT_MAX; //数据里不会出现这么大的数
for (int i...){
    if (nums[i] == former_i) continue;
    former_i = nums[i];

    int former_j = INT_MAX; //注意作用域。这个变量不能定义在最外层，想想为什么
    for (int j...){
        if (nums[j] == former_j) continue;
        former_j = nums[j];
    }
}
```