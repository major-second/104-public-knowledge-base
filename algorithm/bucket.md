- 桶排序：先分桶。桶间自然有序，桶内再排，减小规模
https://baike.baidu.com/item/%E6%A1%B6%E6%8E%92%E5%BA%8F/4973777
如果$N/M$为常数量级，那么$O(N)$
- https://leetcode-cn.com/problems/maximum-gap/
这题桶内可以忽略，只需看桶间信息
- https://leetcode-cn.com/problems/contains-duplicate-iii/

## 总结
映射到桶：快速（$O(n)$）地获取粗略信息。接下来，可以像桶排序一样细化，也可以像maximum-gap一样直接只用粗略信息即可。
contains-duplicate-iii也是只用粗略信息就足够了
