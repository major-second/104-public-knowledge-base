- 计算几何
- 给定n个点（随机顺序，确保成凸多边形），和额外一个点，判定新的点在不在凸多边形中
  - [[化归]]：先随便取一个点做轴，[[symmetry#break]]，再atan2，[[sort]]，就知道考察哪个三角形了
  - 考察三角形和一个点？
    - 法一：算三个角，$\angle AOB, \angle BOC, \angle COA$求和是否等于$2\pi$
      - 此时注意细节[[float]]误差
    - 法二：三次考察$O$，$C$是否在$AB$同侧这样
    - 法三
      - 还是[[symmetry#break]]，随便取一个点做轴
      - 然后如果atan2不能直接判定在外，**则$ACOB$这样一定形成四边形**（**注意一般情况不是**），此时算四个“蚂蚁转角”求和是否$2\pi$即可
- 面积为指定数的格点三角形（全等的只算一个）
  - 分类讨论，[[化归]]到全在第一象限和坐标轴的情况，且有一个点是原点
  - [[algorithm/special-case]]处理有坐标轴点的情况，于是只剩下$(0,0), (2,1), (1,2)$这种形状情况
  - 外积计算三角形面积，给出等式
    - 从而论证[[enumerate]]的界
    - 然后[[enumerate]]并过滤
  - 边边边确保[[algorithm/trivial-mistakes#uniqueness]]
    - 注意平方防止[[float]]误差
  ```python
  from itertools import product
  DEBUG = False
  BOUND = 17
  EPSILON = 1e-4
  S = 8
  length_set = set()
  for ylarge, ysmall, xlarge, xsmall in product(*[range(1, BOUND+1) for _ in range(4)]):
      if ylarge <= ysmall or xlarge <= xsmall: continue
      if ylarge * xlarge - ysmall * xsmall != 2 * S: continue
      # SSS for equality
      s1, s2, s3 = ylarge**2 + xsmall**2, ysmall**2 + xlarge**2, (ylarge-ysmall)**2 + (xlarge-xsmall)**2
      length_set.add(tuple(sorted([s1, s2, s3])))
  if DEBUG:
      print(length_set)
      # Another calculation for validation
      for s1, s2, s3 in length_set:
          s1 = s1**0.5
          s2 = s2**0.5
          s3 = s3**0.5
          half_c = (s1+s2+s3) / 2
          assert abs(half_c * (half_c - s1) * (half_c - s2) * (half_c - s3) - S**2) < EPSILON
  print(len(length_set))
  ``` 