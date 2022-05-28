`pip install opencv-python`

用于把图片变成video：[参考](https://zhuanlan.zhihu.com/p/128616339)
其实是很简单的几行脚本，[[interact]]都行
```python
>>> import cv2
>>> video = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), 80, (1280, 720))
# fourcc当成magic记住即可，80是fps, 后面元组是大小
>>> for i in range(<总图片数>):
...     video.write(cv2.imread(f'./frame{i:04d}.jpg'))
... 
>>> video.release()
```
参考[[format-string]]，`{i:04d}`表示补零到四位整数
这样完了之后是没有任何压缩的`.avi`，非常大，可以用[[ffmpeg]]压缩