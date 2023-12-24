- 实现：可以用标准库[[algorithm]]，参考：`partial_sum(v.begin(), v.end(), back_inserter(v2));`
  - 注意定义是$S_0=a_0$
- 应用：线性空间复杂度存储所有“子串”和。每次要取出时用两个相减即可
  - 相当于一种[[encode-decode]]
# 例题
- https://www.quora.com/How-can-someone-find-the-year-with-the-most-people-alive
  - 输入很多线段，用前缀和（一阶差分）观点相当于很多+1和-1
  - 相当于利用了[[linearity]]，差分和求和交换顺序
  - 通过计算$\sum Df_i$计算$D\sum f_i$，再求和得到$\sum f_i$
  - 拓展题：每次flip一段。那实际上每个位置只要储存0或1即可。[[boolean-arithmetics]]
# [[high-dimension]]
- 二维前缀和例题：左闭右闭矩形中黑块数量
```cpp
/* Sample Input1
3 2
WWB
BBW
WBW
1 2 3 4
0 3 4 5

Sample Output1
4
7 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long singleCornerQuery(long long y, long long x, const vector<vector<long long>>& arr, const long long N){
    if (y < 0 || x < 0) {
        return 0;
    }
    long long y_repeated = y / N;
    long long x_repeated = x / N;
    y %= N;
    x %= N;
    long long res = x_repeated * y_repeated * arr[N-1][N-1]; 
    res += arr[y][x];
    res += x_repeated * arr[y][N-1];
    res += y_repeated * arr[N-1][x];
    return res;
}

int main(){
    long long N, Q;
    cin >> N >> Q;
    string curr_row;
    vector<vector<long long>> p_sum;

    for (long long i=0; i<N; i++){
        cin >> curr_row;
        vector<long long> row_sum;
        long long curr_row_sum = 0;
        for (long long j=0; j<N; j++){
            if (curr_row[j] == 'B'){
                curr_row_sum++;
            }
            row_sum.push_back(curr_row_sum);
        }
        if (i>0){
            for (long long j=0; j<N; j++){
                row_sum[j] += p_sum[i-1][j];
            }
        }
        p_sum.push_back(row_sum);
    }
    for (long long q=0; q<Q; q++){
        long long curr_res = 0;
        long long y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;
        y1--;
        x1--;
        curr_res += singleCornerQuery(y2, x2, p_sum, N);
        curr_res += singleCornerQuery(y1, x1, p_sum, N);
        curr_res -= singleCornerQuery(y1, x2, p_sum, N);
        curr_res -= singleCornerQuery(y2, x1, p_sum, N);
        cout << curr_res << endl;
    }
    return 0;
}
```
- 有几个坑
  - [[off-by-one-errors]]: 问的是左闭右闭，则`y1--`. 否则左开右闭
  - 注意重复部分，除了完整的密铺pattern重复，还有x和y两“条”的部分重复，比如 `res += x_repeated * arr[y][N-1];`
  - 特判负数