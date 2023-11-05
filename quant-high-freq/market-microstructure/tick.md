- [参考](https://www.investopedia.com/terms/t/tick.asp)
1. [[tick-size]]
2. uptick / downtick
   1. > The term tick can also be used to describe the direction of the price of a stock. An uptick indicates a trade where the transaction has occurred at a price higher than the previous transaction and a downtick indicates a transaction that has occurred at a lower price.
   2. [参考csdn](https://blog.csdn.net/weixin_38753422/article/details/95699776)
      1. 只要增删单，交易，量价变化，就产生tick
      2. 所以实际上可能有价格不变的tick
         1. 该文章利用了[[2-financial-data-structures]]的思想（具体地，[[bar-data]]中的info driven bar），对于价格不变的tick标记为ZeroMinusTick等
   3. 从而[[tick-data]]