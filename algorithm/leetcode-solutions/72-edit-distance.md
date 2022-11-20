- [[dp]]思想
  - 这个完美符合[[dp]]原始思想：把前面的一部分去除后，对后面执行的动作仍然是“最优”动作
    - 比如`hep`和`hehep`，你两边开头`h`同时扣除，不会比左边`h`配右边`2`号位`h`更差！
  - 子问题[[self-similarity]]性质！
  - 可以使用状态压缩！
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = word1.size();
        int len2 = word2.size();
        vector<int> minDistanceForSuffices(len2+1, 0);
        for (int i=0; i<len2; i++) minDistanceForSuffices[i] = len2 - i;
        for (int j=len1-1; j>=0; j--) {
            vector<int> next(len2+1, len1-j);
            for (int i=len2-1; i>=0; i--){
                if (word2[i] == word1[j]) next[i] = minDistanceForSuffices[i+1];
                else next[i] = min(min(minDistanceForSuffices[i+1], minDistanceForSuffices[i]), next[i+1]) + 1;
            }
            minDistanceForSuffices = next;
        }

        return minDistanceForSuffices[0];
    }
};
```