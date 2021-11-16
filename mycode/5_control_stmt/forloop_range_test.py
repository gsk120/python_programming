import numpy as np

my_list = [10, 20, 40, 50]
for idx, val in enumerate(my_list, 1):
    print(idx, val)

print(range(10))
print(list(range(10)))
for val in range(10):
    print(val)
# 시작 값 + 증가 값
for val in range(1, 10, 2):
    print(val)

print(np.arange(10))
for val in np.arange(1,10,2):
    print(val)

