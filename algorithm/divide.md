快速选择时需要特判pivot就是待求的情况，并且在选择右边时，需要排除pivot，否则出现很多相同元素时会爆栈
取随机数参考[[rand]]，即`int randnum = rand() % s;`.（头文件：`<stdlib.h>`）