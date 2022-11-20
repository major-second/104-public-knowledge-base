- https://leetcode.cn/problems/pizza-with-3n-slices
- [[memo]]不行
  - 一开始以为只有$O(n^2)$个子问题，即枚举begin和end
  - 后来发现不是！因为你取中间就会把原来的整段分为两半
- 答案：[[化归]]成找（环形意义）不相邻的$3n$个元素，使和最大
  - 用到[[construction]]思想。凡是不相邻的$3n$个元素，一定有一种合法的取出方式
- 具体怎么做？典型的“01”型[[dp]]且可以用状态压缩，参考[[dp]]解说
- 注意[[algorithm/trivial-mistakes]]：首尾相接！
```cpp
class Solution {
public:
    int maxSizeSlicesExcludingTail(vector<int>& slices){
        int numSlices = slices.size();

        int currEnd = 0;
        vector<int> maxExcludingTail(numSlices / 3 + 1, 0);
        vector<int> maxForAll(numSlices / 3 + 1, 0);

        while(++currEnd <= numSlices){
            for (int i = numSlices / 3; i >= 1; i--){
                int includingResult = slices[currEnd-1] + maxExcludingTail[i-1];
                maxExcludingTail[i] = maxForAll[i];
                maxForAll[i] = max(includingResult, maxForAll[i]);
            }
        }

        return maxExcludingTail[numSlices / 3];
    }
    int maxSizeSlices(vector<int>& slices) {
        vector<int> newSlices(slices.begin() + 1, slices.end());
        newSlices.push_back(slices[0]);
        return max(maxSizeSlicesExcludingTail(slices), maxSizeSlicesExcludingTail(newSlices));
    }

};
```