`ffmpeg`是各种视频编解码、压缩抽帧……的首选，大名鼎鼎
- 基础示例：转格式和压缩
  - `ffmpeg -y -i output.avi -c:v libx264 -crf 28 -an output_c.mp4`
  - 直接承接了[[video]]的无压缩视频，用于压缩。压缩效果拔群
  - `-y`不询问，直接覆盖
  - `-i`输入
  - `-c:v`就是`-vcodec`，视频编码！
    - 参考https://www.cnblogs.com/mushan/p/12275550.html?msclkid=14517024cf5c11ec9fa47a5f1f8624dd
  - `-crf`越大质量越差，参考https://blog.csdn.net/happydeer/article/details/52610060?msclkid=c035a643cf5b11ecad367be71da382e0
  - `-an`静音
  - 效果：
```text
-rw-rw-r-- 1 <redacted> <redacted> 7845290526 <redacted> ./output.avi
-rw-rw-r-- 1 <redacted> <redacted>    3694643 <redacted> ./output_c.mp4
```

- 进阶：使用filter
  - `ffmpeg -y -i <输入路径> -c:v libx264 -crf 28 -vf "scale=320:320:force_original_aspect_ratio=increase,pad='iw+mod(iw,2)':'ih+mod(ih,2)'" -an <输出路径>`
  - `-vf`：核心部分处理
    - 参考https://blog.csdn.net/weixin_36249804/article/details/113071641?msclkid=3968bc86cf5c11ec8fc6dd9cf2960be4
    - 新手参考示例https://zhuanlan.zhihu.com/p/67878761?msclkid=95bb142acf5d11ec845bcff9ff47fb90
    - 官方文档http://ffmpeg.org/ffmpeg-filters.html
    - `scale`当然是缩放
    - `pad`填充（这里就是填充成偶数）