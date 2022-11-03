- https://leetcode.cn/problems/super-ugly-number/
```cpp
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<long> uglyNumbers(n, 1);
        int numPrimes = primes.size();
        vector<int> pointers(numPrimes, 0);

        for (int i=1; i<n; i++){
            int indexOfPointers = 0;
            long nextMin = INT_MAX;

            for (int j=0; j<numPrimes; j++){
                long candidate = uglyNumbers[pointers[j]] * primes[j];
                if (candidate < nextMin){
                    nextMin = candidate;
                    indexOfPointers = j;
                }
            }
            if (nextMin!=uglyNumbers[i-1]){
                uglyNumbers[i] = nextMin;
            } else {
                i--;
            }
            pointers[indexOfPointers]++;
        }
        return (int)uglyNumbers[n-1];
    }
};
```
- [[dp]]，每次从有限种可能中优中选优（选最小）
  - 具体：维护指针数组，表示这次由谁乘以2得到下个candidate，这次由谁乘以3得到……以此类推
- 注意[[algorithm/trivial-mistakes]]查重！