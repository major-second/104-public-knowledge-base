- 前置[[matplotlib/basics]]
- `fig = plt.figure()`或者[[subplots]]中`fig, axs = plt.subplots(...)`都可得到figure
  - 其层次比[[axes]]高
- 可以`plt.figure(figsize=(x, y))`指定大小
  - 注意单位是英寸！默认`dpi=72`，所以`x=1`表示72个像素
  - 可以自己再传入`dpi`参数