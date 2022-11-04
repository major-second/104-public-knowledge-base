- https://leetcode.cn/problems/largest-divisible-subset/description/
```cpp
class Solution {
public:
    struct node {
        int coverNum;
        int prevIndex;
        node(int cN, int pI): coverNum(cN), prevIndex(pI) {}
    };

    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<node> dpNode;
        int length = nums.size();
        for (int i = 0; i < length; i++){
            int coverNumMax = 1;
            int prevIndex = i;
            for (int j = i-1; j >= 0; j--){
                if (dpNode[j].coverNum >= coverNumMax && nums[i] % nums[j] == 0){
                    coverNumMax = dpNode[j].coverNum + 1;
                    prevIndex = j;
                }
            }
            dpNode.push_back(node(coverNumMax, prevIndex));
        }

        int coverNumMax = 1;
        int currentIndex = 0;
        for (int i = 0; i < length; i++) if (dpNode[i].coverNum > coverNumMax){
            coverNumMax = dpNode[i].coverNum;
            currentIndex = i;
        }

        vector<int> ans;
        for (; dpNode[currentIndex].prevIndex != currentIndex; currentIndex = dpNode[currentIndex].prevIndex) {
            ans.push_back(nums[currentIndex]);
        }
        ans.push_back(nums[currentIndex]);
        return ans;
    }
};
```
- 尝试使用[[struct]]来让[[dp]]的返回找解过程清晰
- 不能贪心的[[counter-examples]]：`1,2,4,6,18`，你不能有了`4`就不考察`2`