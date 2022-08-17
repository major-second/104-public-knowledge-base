这个文件夹放的是 #读书笔记
主要内容：市场微观结构
注：可以看[[26-intra-day-data]]快速入门一下，大致知道市场微观结构是个啥
- 封面 ![](cover.png)
- 书名：Market Microstructure in Practice
- ISBN：9789813231122
# Foreword
## 第一个人
- Traditional models of market microstructure have studied the highly simplified interaction between an idealized market-maker or specialist and a stream of external orders that may come from noise traders or informed traders.
  - 几个主体！一句话就说出来了
- 但modern: loosely coupled network of visible and hidden venues, linked together by high-frequency traders and by algorithmic strategies
  - venue此处做“聚点”讲？
  - 没有传统的提供、消耗流动性（market-makers vs. directional traders）的划分，而是不同人的latency, fill prob, cost等属性不同
  - 不是在传统简单结构上叠床架屋，而是直接基础地考察这些
- 市场“进化”（复杂）在equity最显著，原因有size, social prominence as indicators of value, variety of traders等
  - 其它市场（期货）等落后，但大方向是“进化”
  - 所有人包括监管者都想越来越理解市场
- liquidity: 大单怎么能被实际执行
  - 从而出现fragmentation, HFT等话题
  - 作者：交易员、和监管谈笑风生，了解多个利益方
## 2
- secular: 长期，世俗，缓慢……
- lift the obstacle
- 这个人让欧洲更像美国！整个paradigm都变了
- 观察分析理解预判！底层逻辑变化导致order book传递信息变化！
- 从学界找资源，找大佬
## 3
- 哈哈，谢邀！以前经常讨论！
- 举个例子让人们理解：和aviation对比
  - aviation：chief engineer也是test pilot，所以必须负责
- 张三（Mr.Smith）啥也不懂，不知道自己买的价格是哪来的，可能被HFT掠夺，对市场没信心
  - 和航空类比：本来窗户没必要（可以自动驾驶，不太可能对撞。窗户浪费钱）但是没人愿意不公开不透明
- 我们要找回张三的信心！uninformed trader
## 4
- 市场，古老（农贸市场）
- 现在：终端 -> 机器化，亚毫秒级别（人脑100毫秒）
- 这世界变化快，但真的好吗？经济学讲，应该提高资源配置效率，起到价格发现功能
- 主要关注欧洲、实际例子（不过对于全球有参考价值）
- 文学首尾呼应哈哈哈
> In the end, we might have gained from automated markets as costly human intermediaries are replaced by computers. And when a robot monitors the market for us, we will have more time to go out and enjoy the farmer’s market
# Introduction
## Liquidity in Question
- 定性定义：容易买卖
- 流动性风险：涨了卖不出去，然后价格降了
- 为了流动性，牺牲利益（降价卖）：market impact
- 量化评价：bid-ask spread（粗略，没考虑量）、指定量的round trip cost（即刻买卖的损失）（显然形成一条曲线）
- 