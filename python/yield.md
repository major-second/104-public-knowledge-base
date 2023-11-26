# python yield关键字
在函数中如果带有 #yield 关键字，这个函数就会变得可迭代！
每次迭代，函数都会运行到yield后，停下来返回yield的值，在下一次迭代后从上次停下来的地方继续执行！

如以下的函数可以用来返回斐波那契数列的前n项，并且只占用常数空间。
```py
def fab(max): 
    num, a, b = 0, 0, 1 
    while num < max: 
        yield b # 每迭代一次到此处即返回，下一次迭代从下一行开始继续运行
        a, b = b, a + b 
        num = num + 1

# 此时fab为可迭代对象！所以可以用for循环进行迭代，每次返回yield的值
for ans in fab(n): 
    print ans
```
运行结果为:
```
1
1 
2 
3 
5
```

我们还可以用send()方法来给带有yield的函数对象发送值。
调用f.send(x)意味着，程序执行流切换到函数f内部yield语句, f中的yield语句返回x，继续执行直到下一次yield或停止。
如将上述代码做以下修改：
```py
def fab(max): 
    num, a, b = 0, 0, 1 
    while num < max: 
        receive = yield b # 将每次yield后send过来的信息保存在receive中
        print(f"fab receive {receive}")
        a, b = b, a + b 
        num = num + 1

f = fab(5)
for i in range(5):
    if i == 0:
        # 刚开始迭代的时候必须发送None(与f.next()同义)来启动迭代
        ans = f.send(None) 
    else:
        ans = f.send(1000 + i)
    print(f"fab returns {ans}")
```

运行结果为:
```py
fab returns 1
fab receive 1001
fab returns 1
fab receive 1002
fab returns 2
fab receive 1003
fab returns 3
fab receive 1004
fab returns 5
```
(注：之前用for方法迭代时，每次迭代实际上执行一次fab.send(None))

## 以下为扩展知识
看到这里，你有没有觉得这个带yield的函数，它好像就是一个和主线程异步执行的线程，使用send和yield来和主线程通信并切换工作流！
没错，我们称其为[协程](../os-knowledge/coroutine.md)(即用户级线程)！
每次调用yield即阻塞该协程，直到收到send传来的消息继续运行！

注：在现代python版本中(>=3.5)，推荐使用[[async-await]]/await方法来实现上述功能


