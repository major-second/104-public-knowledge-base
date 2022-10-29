- https://leetcode.com/problems/k-closest-points-to-origin
# 调[[adapter]]优先队列解法
- 参考[[215-kth-largest-element-in-an-array]]
```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int,int>> pq;
        int length = points.size();
        int pqSize = 0;
        
        for (int i=0; i<length; i++){
            vector<int> point = points[i];
            int distanceSquare = point[0]*point[0] + point[1]*point[1];
            pair<int, int> infoPair = make_pair(distanceSquare, i);
            if (pqSize<k) {
                pq.push(infoPair);
                pqSize++;
            } else if (infoPair<pq.top()){
                pq.pop();
                pq.push(infoPair);
            }
        }
        
        vector<vector<int>> ans;
        while (!pq.empty()) {
            ans.push_back(points[pq.top().second]);
            pq.pop();
        }
        return ans;
    }
};
```
# 调标准库[[algorithm]]的`nth_element`
```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        int length = points.size();
        vector<pair<int, int>> disSqIndexList(length);
        for (int i = 0; i < length; i++){
            vector<int> point = points[i];
            int disSq = point[0] * point[0] + point[1] * point[1];
            disSqIndexList[i] = make_pair(disSq, i);
        }
        nth_element(disSqIndexList.begin(), disSqIndexList.begin() + k, disSqIndexList.end());
        
        vector<vector<int>> ans(k);
        for (int i = 0; i < k; i++) ans[i] = points[disSqIndexList[i].second];
        return ans;
    }
};
```