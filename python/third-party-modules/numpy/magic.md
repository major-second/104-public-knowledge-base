一个对象有`__array__()`的[[python/magic]]方法，即可用`array(<对象>)`得到numpy数组
比如[[gym/wrapper]]的[gym源码中的例子](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py)