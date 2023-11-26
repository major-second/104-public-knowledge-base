from multiprocessing import Process
from time import sleep
if __name__ == '__main__':
    p = Process(target=print, args=('p starts, 一元元组请注意逗号',))
    timer = Process(target=sleep, args=(5,))
    p.start()
    timer.start()
    p.join()
    print('p ends')
    timer.join()
    print('timer ends')

    p = Process(target=print, args=('p starts, 一元元组请注意逗号',))
    timer = Process(target=sleep, args=(5,))
    p.start()
    timer.start()
    timer.join()
    print('timer ends')
    p.join()
    print('p ends')