- 前置
  - [[encode-decode]]
  - [[7-the-power-of-2]]
# 智力题
- 总共有多少种状态，多少进制，决定有多少位
  - [[8-brain-teasers]]第12题，二进制；13题三进制
  - [[2-brain-teasers]] defective ball，三进制
## 猜扑克牌例题
- 五张牌，你有顺序展示四张，做好约定需要猜出剩下一张
- 前三张约定好序有6种状态可传递+1到+6
- 最后两张是抽屉原理约定的同花色且同余意义下离得近的那个，比如红桃8到红桃A距离6（比反过来7小）。结合前面传递的+6即可
# 热力学
- 状态数，$S=ln\Omega$
- [[entropy]]