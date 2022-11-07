- https://leetcode.com/problems/group-anagrams/description/
- [[hash]]思想
```cpp
class Solution {

public:
    int hashFuncForString(const string s, const vector<long>& hash){
        int ans = 0;
        for (char c:s) {
            ans += hash[c-'a'];
            ans %= 1000000007;
        }
        return ans;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<long> hash(26, 1);
        for (int i=1; i<26; i++) hash[i] = hash[i-1] * 127 % 1000000007;
        int length = strs.size();
        unordered_map<long, int> hash2index;
        vector<vector<string>> ans;
        int ansIndex = 0;

        for (int i=0; i<length; i++) {
            string s = strs[i];
            int h = hashFuncForString(s, hash);
            if (!hash2index.count(h)) {
                hash2index[h] = ansIndex++;
                ans.push_back(vector<string>{s});
            } else {
                ans[hash2index[h]].push_back(s);
            }
        }
        return ans;
    }
};
```
- “127进制”和“对十位数取模”是常见手法，参考[[hash]]
- 当然python的话可以用现有的字典