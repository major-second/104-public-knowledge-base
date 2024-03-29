- https://leetcode.cn/problems/kth-largest-element-in-an-array/
- 用[[adapter#priority_queue]]直接调包解题：
```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > pq;
        int i = 0;
        for (;i < k; i++) pq.push(nums[i]);
        for (;i < nums.size(); i++){
            pq.push(nums[i]);
            pq.pop();
        }
        return pq.top();
    }
};
```
- 关于`push`和`pop`
  - 逻辑上：如果新的比原来的`top()`（最小数）大，那么可能产生改变，否则不变
  - 所以上解中`pop, push`不可交换顺序
    - 参考 [[heapq]]
- 头脑解题解说
  - 取最大的k个元素时应当小根堆，[[adapter#priority_queue]]中从大到小，因此传入`greater<int>`
  - $O(Nlogk)$
- 法二：[[quick-select]]出第`k`个，然后扫一遍，$O(N)$