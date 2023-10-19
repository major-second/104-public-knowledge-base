import my_sum
MySum = my_sum.MySum

assert __name__ == '__main__'
ma = MySum(1.1)
ma.Update(1)
ma.Update(0.1)
sum = ma.Get()
print(sum)
ma.Update(0.1)
sum = ma.Get()
print(sum)