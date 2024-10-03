"""
*Д4.5.* Каких 7-значных чисел больше: тех, у которых каждая из трёх средних цифр больше каждой из
остальных четырёх цифр, или тех, у которых каждая из трёх средних цифр меньше каждой из остальных четырёх цифр?
01 234 -1-0

count_sr_b, count_sr_m
2501334 6498666
"""

count_sr_b = 0
count_sr_m = 0

for i in range(1000000, 10000000):
    s = list(map(int, str(i)))
    if (s[2] > s[0] and s[2] > s[1] and s[2] > s[-1] and s[2] > s[-2]) and \
            (s[3] > s[0] and s[3] > s[1] and s[3] > s[-1] and s[3] > s[-2]) and \
            (s[4] > s[0] and s[4] > s[1] and s[4] > s[-1] and s[4] > s[-2]):
        count_sr_b += 1
    elif (s[2] < s[0] and s[2] < s[1] and s[2] < s[-1] and s[2] < s[-2]) and \
            (s[3] < s[0] and s[3] < s[1] and s[3] < s[-1] and s[3] < s[-2]) and \
            (s[4] < s[0] and s[4] < s[1] and s[4] < s[-1] and s[4] < s[-2]):
        count_sr_m += 1
print(count_sr_b, count_sr_m, count_sr_m > count_sr_m)
