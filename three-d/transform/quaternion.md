四元数（模长为1）可代表“旋转”
分为`x, y, z, w`四个分量，$w=1$表示不转
- `pyquaternion`w在前
`pip install pyquaternion`
`python`
```python 
>>> from quaternion import quaternion
>>> quaternion(1,0,0,0).x
0.0
>>> quaternion(1,0,0,0).w # w在前
1.0
```
- `pybullet`w在后，[参考](https://usermanual.wiki/Document/pybullet20quickstart20guide.479068914/html)
- 有些地方会明确写出`w`是多少。比如[[hand-eye-calibration]]和[[aruco]]的结果
- `rosrun tf tf_echo`的w在后