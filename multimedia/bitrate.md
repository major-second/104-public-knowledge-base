前置：
- [[player]]

比特率：每秒传输多少比特
逐帧抽出图片大小是视频大小的多少倍？
$图片宽*图片高*每个像素多少比特(bpp)*帧率(fps)/比特率(以bit为单位) * \alpha$
其中$\alpha$指未经压缩的位图压缩成`.jpg`等时大小变成了原来的$\alpha$倍（和抽图抽出的格式和质量设置等都有关）
实操(Ubuntu)：
`sudo apt install mplayer`
`mplayer -vo null -ao null -identify -frames 0 <视频文件名> | more`
参考
https://qastack.cn/superuser/55780/how-can-i-obtain-the-bitrate-of-a-video-from-a-command-line-in-linux