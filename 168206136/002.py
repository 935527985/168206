def 判断水仙花数(num):
        '判断一个数是否是水仙花数'
        num = int(num)
        if num < 100 or num > +1000:
            print("不是水仙花数")
        else:
            个位 = num % 10
            百位 = int(num / 100)
            十位 = int((num - 百位 * 100) / 10)
            # print(个位)
            # print(十位)
            # print(百位)
            sum = 个位 * 个位 * 个位 + 十位 * 十位 * 十位 + 百位 * 百位 * 百位
            if sum == num:
                print("%d是水仙花数" % num)
            else:
                print("不是水仙花数")

num = input(“请输入一个数”)
判断水仙花数(num)
