- https://leetcode.com/problems/longest-mountain-in-array/
# 我的
```cpp
class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        int WAIT = 2;
        int UP = 1;
        int DOWN = 0;
        
        int phase = WAIT;
        int begin = 0;
        int longest = 0;
        for (int i=1;i<n;i++){
            if (phase==WAIT){
                if (arr[i] <= arr[i-1]) continue;
                begin = i-1;
                phase = UP;
            } else if (phase==UP){
                if (arr[i] > arr[i-1]) continue;
                if (arr[i] == arr[i-1]) phase = WAIT;
                else phase = DOWN;
            } else {
                if (arr[i] < arr[i-1]) continue;
                if (arr[i] == arr[i-1]) phase = WAIT;
                else phase = UP;
                longest = max(longest, i-begin);
                if (arr[i] > arr[i-1]) begin = i-1;
            }
        }
        if (phase==DOWN) longest = max(longest, n-begin);
        return longest;
    }
};
```
- 里面体现很多[[algorithm/trivial-mistakes]]
  - 如果循环体中有获取结果的代码，那要小心最后是否一定获取了结果（这里的`if (phase==DOWN) longest = max(longest, n-begin);`）
  - 等于的情况造成麻烦！
- 体现[[DFA]]的思想
- 一个粗心点：注意`DOWN`直接转`UP`时不要忘记更新`begin`