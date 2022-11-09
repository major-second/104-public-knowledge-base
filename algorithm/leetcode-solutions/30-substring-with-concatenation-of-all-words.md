- https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
- [[sliding-window]], [[hash]]
```cpp
class Solution {
public:
    static constexpr long numAlphabets = 26;
    static constexpr long modNum = 1000000007;
    long hashForChar(const char& c) {
        return c-'a';
    }
    vector<long> hashesForSubStrings(const string& str, const int interval) {
        long greatestPower = 1;
        for (int p = 0; p<interval-1; p++) {
            greatestPower *= numAlphabets;
            greatestPower %= modNum;
        }

        long hashForFirstStr = 0;
        int strLength = str.size();
        int i=0;
        for (; i<interval; i++){
            hashForFirstStr *= numAlphabets;
            hashForFirstStr += hashForChar(str[i]);
            hashForFirstStr %= modNum;
        }
        vector<long> hashes{hashForFirstStr};
        long lastHash = hashes[0];
        for(; i<strLength; i++){
            lastHash += -hashForChar(str[i-interval]) * greatestPower + modNum * greatestPower;
            lastHash %= modNum;
            lastHash *= numAlphabets;
            lastHash += hashForChar(str[i]);
            lastHash %= modNum;
            hashes.push_back(lastHash);
        }
        return hashes;
    }
    vector<int> findSubstring(string s, vector<string>& words) {
        int wordsCount = words.size();
        int wordLength = words[0].size();
        int totalLength = wordsCount * wordLength;
        int stringLength = s.size();
        if (totalLength > stringLength) return vector<int>{};

        vector<long> hashes = hashesForSubStrings(s, wordLength);

        multiset<long> hashesSetForComparison;
        for (auto word:words) hashesSetForComparison.insert(hashesForSubStrings(word, wordLength)[0]);
        
        int pointers[wordsCount];
        for (int i=0; i<wordsCount; i++) pointers[i] = i * wordLength;

        vector<int> ans;
        while(pointers[wordsCount-1] + wordLength <= stringLength) {
            multiset<long> hashesSet;
            for (int i=0; i<wordsCount; i++) hashesSet.insert(hashes[pointers[i]]);
            
            bool flag = true;
            for (auto it=hashesSet.begin(); it!=hashesSet.end(); it++){
                if (hashesSet.count(*it) != hashesSetForComparison.count(*it)) {
                    flag = false;
                    break;
                }
            }
            if (flag) ans.push_back(pointers[0]);
            for (int i=0; i<wordsCount; i++) pointers[i]++;
        }
        return ans;
    }
};
```
- 这里手动实现了[[hash]]，可以控制细节进行[[sliding-window]]滚动，能加快速度
- 注意：$a+b,a-b,a*b$都可以$a,b$同时取模，答案也取模，而$a\%b$不可以，例如$27\%12 = 5, 7\%2 = 1$
- 所以：滚动哈希往下滚时不能对$26^{\alpha}$取模
  - 而是减$a*26^\alpha$这样
  - 当然“减”会导致负数，引发麻烦。应该完了之后再加某个能被模数整除的大正数。参考[[op]]中对`%`的说明