from multiprocessing import Pool
from time import sleep, time
def f(x):
    sleep(0.2)
    return x**2 
l = list(range(10))

if __name__ == '__main__':
    t = time()
    with Pool(2) as p:
        print(list(p.map(f, l)))
    print(time() - t)

    t = time()
    with Pool(5) as p:
        print(list(p.map(f, l)))
    print(time() - t)

    t = time()
    print(list(map(f, l)))
    print(time() - t)