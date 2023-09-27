from multiprocessing import Pool
from time import sleep

sleep(2)
print('loading')

f = str

with Pool(2) as p:
    print(p.map(f, [1, 2, 3]))