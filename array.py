# (=======================================) |- 1 -| (=====================================)

n = int(input("Array1 - Введите n (кол-во нечётных): "))
arr = [2*i+1 for i in range(n)]
print("Array1:", arr)

# (=======================================) |- 2 -| (=====================================)

n = int(input("Array2 - Введите n (кол-во степеней 2): "))
arr = [2**i for i in range(n)]
print("Array2:", arr)

# (=======================================) |- 3 -| (=====================================)

n = int(input("Array7 - Введите n (размер массива): "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
print("Array7 (в обратном порядке):", arr[::-1])

# (=======================================) |- 4 -| (=====================================)

n = int(input("Array8 - Введите n (размер массива): "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
x = int(input("Число для поиска: "))
print("Array8: есть" if x in arr else "Array8: нет")

# (=======================================) |- 5 -| (=====================================)

n = int(input("Array9 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
count_even = sum(1 for v in arr if v % 2 == 0)
print("Array9: количество чётных =", count_even)

# (=======================================) |- 6 -| (=====================================)

n = int(input("Array10 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
count = sum(1 for v in arr if v % 3 == 0 and v % 7 != 0)
print("Array10: количество =", count)

# (=======================================) |- 7 -| (=====================================)

n = int(input("Array11 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
s = sum(arr)
prod = 1
for v in arr:
    prod *= v
print("Array11: сумма =", s, ", произведение =", prod)

# (=======================================) |- 8 -| (=====================================)

n = int(input("Array12 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
sum_result = 0
found_odd = False
for v in arr:
    sum_result += v
    if v % 2 != 0:
        found_odd = True
        break
if not found_odd:
    if n > 2:
        sum_result = sum(arr[1:-1])
    else:
        sum_result = 0
print("Array12: результат =", sum_result)

# (=======================================) |- 9 -| (=====================================)

n = int(input("Array13 - Введите n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
k = int(input("k (1 <= k <= n): "))
delta = arr[k-1]
arr = [v + delta for v in arr]
print("Array13:", arr)

# (=======================================) |- 10 -| (=====================================)
n = int(input("Array14 - Введите n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
first_even = None
for v in arr:
    if v % 2 == 0:
        first_even = v
        break
if first_even is not None:
    arr = [v + first_even if v % 2 == 0 else v for v in arr]
print("Array14:", arr)

# (=======================================) |- 11 -| (=====================================)

n = int(input("Array15 - Введите n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
last_odd = None
for v in reversed(arr):
    if v % 2 != 0:
        last_odd = v
        break
if last_odd is not None:
    arr = [v + last_odd if v % 2 != 0 else v for v in arr]
print("Array15:", arr)

# (=======================================) |- 12 -| (=====================================)
n = int(input("Array16 - Введите n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
if n > 0:
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
print("Array16:", arr)

# (=======================================) |- 13 -| (=====================================)

n = int(input("Array17 - Введите n (чётное): "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
for i in range(0, n, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print("Array17:", arr)

# (=======================================) |- 14 -| (=====================================)

n = int(input("Array18 - Введите n (чётное): "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
half = n // 2
arr = arr[half:] + arr[:half]
print("Array18:", arr)

# (=======================================) |- 15 -| (=====================================)

n = int(input("Array19 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
k = int(input("k (0 <= k < n): "))
if 0 <= k < n:
    arr.pop(k)
print("Array19: новый массив (len={}): {}".format(len(arr), arr))

# (=======================================) |- 16 -| (=====================================)

n = int(input("Array20 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
k = int(input("k (0 <= k < n): "))
m = int(input("m (k < m < n): "))
if 0 <= k < m < n:
    del arr[k:m+1]
print("Array20: новый массив (len={}): {}".format(len(arr), arr))

# (=======================================) |- 17 -| (=====================================)
n = int(input("Array21 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
arr = [v for v in arr if v % 2 == 0]
print("Array21: новый массив (len={}): {}".format(len(arr), arr))

# (=======================================) |- 18 -| (=====================================)

n = int(input("Array22 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
# оставляем элементы с нечетными индексами: 1,3,5,...
new_arr = arr[1::2]
print("Array22: новый массив (len={}): {}".format(len(new_arr), new_arr))

# (=======================================) |- 19 -| (=====================================)
n = int(input("Array23 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
# оставляем элементы с чётными индексами: 0,2,4,...
new_arr = arr[0::2]
print("Array23: новый массив (len={}): {}".format(len(new_arr), new_arr))

# (=======================================) |- 20 -| (=====================================)
n = int(input("Array24 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
res = []
for v in arr:
    if not res or res[-1] != v:
        res.append(v)
print("Array24: новый массив (len={}): {}".format(len(res), res))

# (=======================================) |- 21 -| (=====================================)

n = int(input("Array25 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
seen = set()
res = []
for v in arr:
    if v not in seen:
        res.append(v)
        seen.add(v)
print("Array25: новый массив (len={}): {}".format(len(res), res))

# (=======================================) |- 22 -| (=====================================)

n = int(input("Array26 - Введите n: "))
arr = [int(input(f"Элемент {i}: ")) for i in range(n)]
seen = set()
res_rev = []
for v in reversed(arr):
    if v not in seen:
        res_rev.append(v)
        seen.add(v)
res = list(reversed(res_rev))
print("Array26: новый массив (len={}): {}".format(len(res), res))
