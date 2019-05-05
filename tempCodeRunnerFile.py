x = 5
step = 2
count = 2
print(2, 3, sep='\n')
while x < 100000:
    for i in range(3, int(x**0.5) + 1, 2):
        if not x % i:
            break
    else:
        print(x)
        count += 1
    x += step
    step = 4 if step == 2 else 2
print(count)