- 前置[[oi-wiki-basic/var]]
- 参考https://oi-wiki.org/lang/loop/

`while(){}`
`for(;;){}`（特别注意不是逗号）
范围`for`：`for (auto x:s)`，在[[container-intro]]中用到
`break`在`for`循环中也能用，直接跳出，也就是最后`i`不会再加一（`continue`当然让`i`正常加）
# 拓展
## 连续重复元素只取一次
- [[18-4sum]]中用到
- 原始版本循环（这里没写反花括号）
```cpp
for (int i=0;i<n;i++){
    for (int j=i+1;j<n;j++){
```
- snippet版：4行一组，原来1行变成现在4行
  - 注意假设`INT_MAX`始终不在`nums`内
  - 注意作用域（思考：`former_j_value`为何不能在更外面一层）
```cpp
int former_i_value = INT_MAX;
for (int i=0;i<n;i++){
    if (nums[i]==former_i_value) continue;
    former_i_value = nums[i];

    int former_j_value = INT_MAX;
    for (int j=i+1;j<n;j++){
        if (nums[j]==former_j_value) continue;
        former_j_value = nums[j];
```
## 常用搭配
- `while(i--) ...`
  - `i`一来先减一，所以从初值减一开始执行
  - 如果减一之前等于0，那么就不执行循环体，所以就执行到0（包含0）为止
  - 结束之后`i`是`-1`
  - 在[[10-regular-expression-matching]]中能看到`while(s_pointer--) match[s_pointer] = 0;`
## 常用注意事项
- 如果循环体中有获取结果的代码，要注意是否一定被执行了，是否需要结尾补获取结果
  - 例[[845-longest-mountain-in-array]]，[[21-merge-two-sorted-lists]]，[[68-text-justification]]