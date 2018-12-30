def 合并(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def 合并排序(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = 合并排序(lists[:middle])
    right = 合并排序(lists[middle:])
    return 合并(left, right)


if __name__ == '__main__':
    a = [45, 783, 738, 3452, 451, 454]
    print (合并排序(a))
