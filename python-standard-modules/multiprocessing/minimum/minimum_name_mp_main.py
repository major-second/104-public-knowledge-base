from multiprocessing import Pool
l = list(range(100))
def f(x):
    print(__name__)
    return x**2
print(f'imported in {__name__}')

if __name__ == '__main__':
    with Pool(2) as p:
        print(list(p.map(f, l)))