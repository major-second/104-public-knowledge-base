前置：
- [[realsense/installation]]

步骤：
https://pypi.org/project/pyrealsense2/
- 举例：如果你有[[conda/installation]]的话，可以
  - `conda create -n pointcloud python=3.6`
  - `conda activate pointcloud`
  - `pip install pyrealsense2`

然后官网示例
```sh
import pyrealsense2 as rs
pipe = rs.pipeline()
profile = pipe.start()
try:
  for i in range(0, 100):
    frames = pipe.wait_for_frames()
    for f in frames:
      print(f.profile)
finally:
    pipe.stop()
```