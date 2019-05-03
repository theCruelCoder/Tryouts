count = 1
x = 2
print(x, count)
for x in range(3, 100000, 2):  # 排除所有偶数
    if x % 6 != 1 and x % 6 != 5:  # 质数6的性质
        continue
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            break
    else:
        count += 1
        print(x, count)
