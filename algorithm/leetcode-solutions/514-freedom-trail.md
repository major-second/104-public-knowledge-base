- https://leetcode.cn/problems/freedom-trail/description/
- 可以状态压缩的[[dp]]
- 注意[[algorithm/trivial-mistakes]]所说首尾相接问题
```cpp
class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int ringSize = ring.size();
        vector<int> minSteps(ringSize, 0);
        for (int i=0; i<ringSize; i++){
            minSteps[i] = min(abs(i), abs(i-ringSize));
        }

        for (char k_char:key){
            vector<int> newMinSteps(ringSize, INT_MAX/2);
            for (int i=0; i<ringSize; i++) {
                if (ring[i] == k_char) {
                    for (int j=0; j<ringSize; j++){
                        int minDistance = min(min(abs(j-i), abs(j+ringSize-i)), abs(i+ringSize-j));
                        newMinSteps[i] = min(newMinSteps[i], minSteps[j] + minDistance + 1);
                    }
                }
            }
            minSteps = newMinSteps;
        }

        int minStep = INT_MAX;
        for (int cand:minSteps) minStep = min(cand, minStep);
        return minStep;
    }
};
```