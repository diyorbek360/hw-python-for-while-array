# # (=======================================) |- 1 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print(f"{N} ning bo‘luvchilari:")
# for i in range(1, N + 1):
#     if N % i == 0:
#         print(i, end=" ")
# print()

# # (=======================================) |- 2 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# yigindi = 0
# for i in range(1, N + 1):
#     if N % i == 0:
#         yigindi += i
# print("Bo‘luvchilar yig‘indisi:", yigindi)

# # (=======================================) |- 3 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# yigindi = 0
# for i in range(1, N):
#     if N % i == 0:
#         yigindi += i
# if yigindi == N:
#     print("Mukammal son")
# else:
#     print("Mukammal emas")

# # (=======================================) |- 4 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print(f"{N} gacha bo‘lgan mukammal sonlar:")
# for num in range(2, N + 1):
#     yigindi = 0
#     for i in range(1, num):
#         if num % i == 0:
#             yigindi += i
#     if yigindi == num:
#         print(num, end=" ")
# print()

# # (=======================================) |- 5 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print("3 ga bo‘linadigan, lekin 5 ga bo‘linmaydigan sonlar:")
# for i in range(1, N + 1):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i, end=" ")
# print()

# # (=======================================) |- 6 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# tub = True
# if N < 2:
#     tub = False
# else:
#     for i in range(2, int(N ** 0.5) + 1):
#         if N % i == 0:
#             tub = False
#             break
# if tub:
#     print("Tub son")
# else:
#     print("Tub emas")

# # (=======================================) |- 7 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print(f"{N} gacha bo‘lgan tub sonlar:")
# for num in range(2, N + 1):
#     tub = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             tub = False
#             break
#     if tub:
#         print(num, end=" ")
# print()

# # (=======================================) |- 8 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print(f"{N} gacha bo‘lgan Pifagor sonlari (a, b, c):")
# for a in range(1, N + 1):
#     for b in range(a, N + 1):
#         for c in range(b, N + 1):
#             if a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c)
# print()

# # (=======================================) |- 9 -| (=====================================)
# N = int(input("N sonini kiriting: "))
# print(f"{N} gacha bo‘lgan do‘st sonlar:")
# for a in range(2, N + 1):
#     sum_a = sum(i for i in range(1, a) if a % i == 0)
#     for b in range(a + 1, N + 1):
#         sum_b = sum(i for i in range(1, b) if b % i == 0)
#         if sum_a == b and sum_b == a:
#             print(a, b)
# print()

# # (=======================================) |- 10 -| (=====================================)
# k = int(input("k sonini kiriting: "))
# n = int(input("n sonini kiriting (n > 0): "))
# for i in range(n):
#     print(k, end=" ")
# print()

# # (=======================================) |- 11 -| (=====================================)
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a < b): "))
# count = 0
# for i in range(a, b + 1):
#     print(i, end=" ")
#     count += 1
# print("\nChiqarilgan sonlar soni:", count)

# # (=======================================) |- 12 -| (=====================================)
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a < b): "))
# count = 0
# for i in range(b - 1, a, -1):
#     print(i, end=" ")
#     count += 1
# print("\nChiqarilgan sonlar soni:", count)

# # (=======================================) |- 13 -| (=====================================)
# narx = float(input("1 kg konfet narxini kiriting: "))
# for i in range(1, 11):
#     print(f"{i} kg konfet narxi: {narx * i:.2f}")

# # (=======================================) |- 14 -| (=====================================)
# narx = float(input("1 kg konfet narxini kiriting: "))
# x = 0.1
# while x <= 1.0:
#     print(f"{x:.1f} kg konfet narxi: {narx * x:.2f}")
#     x += 0.1

# # (=======================================) |- 15 -| (=====================================)
# narx = float(input("1 kg konfet narxini kiriting: "))
# x = 1.2
# while x <= 2.0:
#     print(f"{x:.1f} kg konfet narxi: {narx * x:.2f}")
#     x += 0.2

# # (=======================================) |- 16 -| (=====================================)
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a < b): "))
# yigindi = 0
# for i in range(a, b + 1):
#     yigindi += i
# print("Yig‘indi:", yigindi)

# # (=======================================) |- 17 -| (=====================================)
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a < b): "))
# kopaytma = 1
# for i in range(a, b + 1):
#     kopaytma *= i
# print("Ko‘paytma:", kopaytma)

# # (=======================================) |- 18 -| (=====================================)
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a < b): "))
# yigindi = 0
# for i in range(a, b + 1):
#     yigindi += i ** 2
# print("Kvadratlar yig‘indisi:", yigindi)
