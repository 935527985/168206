s = [4523, 786, 45, 452, 457, 783, 70, 878, 725]

# 选择排序函数
for i in range(0, len(s) - 1):
    index = i
    for j in range(i + 1, len(s)):
        if s[index] > s[j]:
            index = j
    s[i], s[index] = s[index], s[i]

# 输出结果
for m in range(0, len(s)):
    print(s[m])
