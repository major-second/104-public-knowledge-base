- [[topo]]
## [[oi-wiki-basic/recursion]]深搜法
```python
class Solution:
    def dfs(self, visited, flag, answer, i, g):
        if visited[i] == 1:
            flag[0] = False
        if visited[i]:
            return
        visited[i] = 1
        for dst in g[i]:
            self.dfs(visited, flag, answer, dst, g)
            if not flag[0]: return
        visited[i] = 2
        answer.append(i)
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            g[pre[0]].append(pre[1])
        
        visited = [0 for _ in range(numCourses)]
        flag = [True]
        answer = []
        for i in range(numCourses):
            self.dfs(visited, flag, answer, i, g)
            if not flag[0]: return []
        return answer
```
- 注意可以用可变对象模仿cpp的引用功能
- 注意实际中可能不止一棵树，而且一来也未必在根，所以必须跑个循环每个都走一遍dfs
  - 但过程中碰到黑色点就提早退出
```cpp
class Solution {
public:
    void dfs(vector<int>& visited, bool& flag, vector<int>& answer,
            const int root, const vector<vector<int>> g){
        if (visited[root] == 1) flag = false;
        if (visited[root]) return;
        visited[root] = 1;
        for (int dst: g[root]){
            dfs(visited, flag, answer, dst, g);
            if (!flag) return;
        }
        visited[root] = 2;
        answer.push_back(root);
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        for (auto pre:prerequisites) g[pre[0]].push_back(pre[1]);
        
        vector<int> visited(numCourses, 0);
        bool flag = true;
        vector<int> answer;
        for (int i=0; i<numCourses; i++){
            dfs(visited, flag, answer, i, g);
            if (!flag) return vector<int>{};
        }
        return answer;
    }
};
```
- 思想完全一样但是超时了，可能是对cpp要求更高
## 非递归深搜法
- 第一版通过的cpp
```cpp
class Solution {
public:
    void dfs(vector<int>& visited, bool& flag, vector<int>& answer,
            const int root, const vector<vector<int>> g, vector<int>& pointers){
        stack<int> s;
        if (visited[root]==0) s.push(root);
        while(!s.empty()) {
            int top = s.top();
            visited[top] = 1;
            if (pointers[top]==g[top].size()){
                answer.push_back(top);
                visited[top] = 2;
                s.pop();
                if (!s.empty()) pointers[s.top()]++; else return;
            } else {
                int next = g[top][pointers[top]];
                if (visited[next]==1) {
                    flag = false;
                    return;
                }
                if (visited[next]==2) {
                    pointers[s.top()]++;
                    continue;
                }
                s.push(next);
            }
        }
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        for (auto pre:prerequisites) g[pre[0]].push_back(pre[1]);
        
        vector<int> visited(numCourses, 0);
        bool flag = true;
        vector<int> answer;
        vector<int> pointers(numCourses, 0);
        for (int i=0; i<numCourses; i++){
            dfs(visited, flag, answer, i, g, pointers);
            if (!flag) return vector<int>{};
        }
        return answer;
    }
};
```
## [[greedy]]思想
- 从出度为0的开始。出度为0的课不上白不上
- 称为Kahn算法
- 需要使用[[bfs]]