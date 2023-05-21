import numpy as np

# Tạo 10 bộ dữ liệu
data = []
for i in range(10):
    arr = np.random.randint(0, 1000000, size=1000000)
    data.append(arr)

# In ra từng phần tử trong mỗi bộ dữ liệu
for i, arr in enumerate(data):
    print(f"Data {i}:")
    for j, val in enumerate(arr):
        print(f"{j}: {val}")
