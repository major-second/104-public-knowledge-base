- https://leetcode.cn/problems/text-justification
- [[oi-wiki-basic/simulate]]，需要分模块
    - 主体[[greedy]]
      - 有[[algorithm/trivial-mistakes]]的“差一问题”，注意空格。后面有空格，第一个单词无空格
    - 低级模块就是模拟
      - 有[[algorithm/trivial-mistakes]]的“差一问题”，注意除数是单词数-1，注意不要除以0
      - 需要熟悉[[oi-wiki-stl/string]]操作，例如`push_back`, `insert`, `+`等
- 看清题意：最后一行需要左对齐！
  - 当然，这里即使最后一行不是左对齐，也需要注意[[loop]]结束的问题（结束循环后，需要专门收个尾）
```cpp
class Solution {
public:
    string generateRow(const vector<string>& words, int begin, int end, int maxWidth){
        if (end-begin==1) {
            string ans = words[begin];
            ans.insert(ans.size(), maxWidth-ans.size(), ' ');
            return ans;
        }
        string ans = "";
        int numSpacesTotal = maxWidth;
        for (auto it = words.begin() + begin; it != words.begin() + end; it++) numSpacesTotal -= (*it).size();
        int numSpacesBase = numSpacesTotal / (end-begin-1);
        int numSpacesRemainder = numSpacesTotal % (end-begin-1);
        for (auto it = words.begin() + begin; it != words.begin() + end; it++) {
            ans += *it;
            if (it+1 != words.begin() + end){
                for (int i = 0; i<numSpacesBase; i++) {
                    ans.push_back(' ');
                }
                if(it - words.begin() - begin < numSpacesRemainder) ans.push_back(' ');
            }
        }
        return ans;
    }

    string generateLastRow(const vector<string>& words, int begin, int end, int maxWidth){
        string ans = "";
        for (auto it = words.begin() + begin; it != words.begin() + end; it++) {
            ans += *it;
            if (it+1 != words.begin() + end){
                ans.push_back(' ');
            }
        }
        ans.insert(ans.size(), maxWidth-ans.size(), ' ');
        return ans;
    }

    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> rows;
        int numWords = words.size();

        int currRowLen = 0;
        int begin = 0;
        for (int i = 0; i < numWords; i++) {
            int currWordLen = words[i].size();
            int addingLen = currWordLen + (bool)currRowLen;
            if (currRowLen + addingLen <= maxWidth){
                currRowLen += addingLen;
            }
            else {
                rows.push_back(generateRow(words, begin, i, maxWidth));
                begin = i;
                currRowLen = currWordLen;
            }
        }
        rows.push_back(generateLastRow(words, begin, numWords, maxWidth));
        return rows;
    }
};
```