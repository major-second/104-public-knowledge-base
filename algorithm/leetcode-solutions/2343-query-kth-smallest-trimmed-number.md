- https://leetcode.com/problems/query-kth-smallest-trimmed-number/
- 前置[[radix-sort]]
# 我的基数排序
```cpp
class Solution {
public:
    vector<pair<string, int>> subKeySort(vector<pair<string, int>>& pairs, int stringsNum, int i){
        vector<int> partialSum;
        vector<int> bucket(10, 0);
        vector<pair<string, int>> ans(stringsNum, make_pair("", 0));
        for (int j=0;j<stringsNum;j++) {
            int key = pairs[j].first[i]-'0';
            bucket[key]++;
        }
        partial_sum(bucket.begin(), bucket.end(), back_inserter(partialSum));
        
        for (auto p:pairs) {
            int key = p.first[i]-'0';
            int goingToIndex = 0;
            if (key) goingToIndex = partialSum[key-1];
            while(ans[goingToIndex].first.size()) goingToIndex++;
            ans[goingToIndex] = p;
        }
        return ans;
    }
    
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        vector<int> answers;
        int stringsNum = nums.size();
        int length = nums[0].size();
        int indicesList[length][stringsNum];
        vector<pair<string, int>> pairs;
        for (int i=0; i<stringsNum; i++) pairs.push_back(make_pair(nums[i], i));
        for (int i=1; i<=length; i++){
            pairs = subKeySort(pairs, stringsNum, length-i);
            for (int j=0; j<stringsNum; j++) indicesList[i-1][j] = pairs[j].second;
        }
        for (auto q:queries){
            answers.push_back(indicesList[q[1]-1][q[0]-1]);
        }
        return answers;
    }
};
```
- 要点
  - 有[[oi-wiki/simulate]]的意味
    - 这个输入输出有点绕，并不是输入未排序，输出排序的，而是和脚标有关，比较复杂
    - 所以先要在草稿纸上画好
    - 先写主函数再写[[radix-sort]]的那部分
  - 使用[[pair]]，加入脚标用于排序，防重
  - 差1错误
    - 注意[[partial-sum]]定义是$S_0=a_0$
    - 为了维持稳定，考虑重复，需要考察`partialSum[key - 1]`，且注意`0`始终对应0
    - query问`1`，最小元素，对应0号位
- 其它注意
  - [[oi-wiki-stl/string]]需要取`.size()`才能作为判断条件