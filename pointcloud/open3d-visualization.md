https://blog.csdn.net/weixin_43486780/article/details/108578048
我们得到`.ply`文件，比如[[python-wrapper]]
`pip install open3d`
然后`python`中
```python 
import open3d as o3d
pcd = o3d.io.read_point_cloud('name.ply')
o3d.visualization.draw_geometries([pcd])
```