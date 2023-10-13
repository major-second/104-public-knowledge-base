- 前置[[hash]]
- [参考](https://www.liaoxuefeng.com/wiki/1207298049439968/1311929706479649)
    > 区块链依靠安全的哈希算法保证所有区块数据不可更改
    > 交易数据依靠Merkle Hash确保无法修改，整个区块依靠Block Hash确保区块无法修改
        - 关键的[[general-principles/recursion]]：block hash = hash (..., prev block hash, merkle hash)
          - 所以想要恶意篡改必须连续一大串（“链”）
        - 第一个：“创世区块”，类似[[general-principles/recursion]]出口
    > 工作量证明机制（挖矿）保证修改区块链的难度非常巨大从而无法实现