- https://leetcode.com/problems/median-of-two-sorted-arrays
```cpp
class Solution {
public:
    // BF
    // int findNthLeast(const vector<int>& nums1, const vector<int>& nums2, const int n){
    //     vector<int> dst;
    //     merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), back_inserter(dst));
    //     return dst[n];
    // }
    
    int findNthLeast(const vector<int>& nums1, const vector<int>& nums2, const int n){
        int n1 = nums1.size();
        int n2 = nums2.size();
        if (n1<=2 && n2<=2 || !n1 || !n2) {
            vector<int> dst;
            merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), back_inserter(dst));
            return dst[n];
        }
        
        int m1 = n1/2, m2 = n2/2;
        int lessNums = m1+m2+1;
        int greaterNums = n1+n2-lessNums;
        
        vector<int> v1 = nums1;
        vector<int> v2 = nums2;
        int nextN;
        
        if (n>=lessNums){
            if (nums1[m1]<nums2[m2]) {
                v1 = vector<int>(nums1.begin()+m1+1, nums1.end());
                nextN = n-m1-1;
            } else {
                v2 = vector<int>(nums2.begin()+m2+1, nums2.end());
                nextN = n-m2-1;
            }
            return findNthLeast(v1, v2, nextN);
        } else {
            if (nums1[m1]<nums2[m2]) {
                v2 = vector<int>(nums2.begin(), nums2.begin()+m2);
                nextN = n;
            } else {
                v1 = vector<int>(nums1.begin(), nums1.begin()+m1);
                nextN = n;
            }
            return findNthLeast(v1, v2, nextN);
        }
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        if ((n1+n2)%2) return findNthLeast(nums1, nums2, (n1+n2)/2);
        return (findNthLeast(nums1, nums2, (n1+n2)/2)
                +findNthLeast(nums1, nums2, (n1+n2)/2-1)) / (double)2;
    }
};
```
- 要点
  - 每次以一个比例缩小问题规模，不一定是二分[[binary-search]]，结果仍然是对数
    - 这里如果强行“二分”就错了
      - 比如`[1,2,3],[4,5,6]`，找`2`号位
      - 你不能比较`2,5`后舍去`3,5,6`
      - 只能舍去`5,6`，因为已知它们大于`1,2,4`三个数了
  - 可以模块化，并先写暴力用于[[comparison]]
  - 注意[[oi-wiki-basic/recursion]]出口
    - 两类[[algorithm/special-case]]
    - 元素都很少或者一边是空！
- 可以发现这里用到[[sequence]]用迭代器初始化
  - `v1 = vector<int>(nums1.begin(), nums1.begin()+m1);`
- 另一个答案
  - https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation
  - 就是严格地每次二分[[binary-search]]而不是像我那样每次丢掉“四分之一”
  - 要点是：不一定在两个数组各自中间切，而是左边半边都小于右边半边
  - 不在中间，那在哪里？[[binary-search]]
  - 这个应该是