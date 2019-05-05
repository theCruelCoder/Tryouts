import random

# random 模块
# randint(a, b) 返回[a,b]之间的整数
# choice(seq) 从非空序列的元素中随机挑选一个元素

random.choice([1, 3, 4, 5, 6])

# randrange([start,] stop [,step]) 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1。

random.randrange(1, 7, 2)

# random.shuffle(list) -> None 就地打乱列表元素

# sample(population, k) 从样本空间或总体（序列或者集合类型）中随机取出k个不同的元素，返回一个新的列表

print(random.sample(['a', 'b', 'c', 'd'], 2))
print(random.sample(['a', 'a'], 2))  # Output:
