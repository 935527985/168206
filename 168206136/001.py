def QuickSort(myList,start,end):
    #判断数组是否为空
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

print("请输入一个数组，中间以空格隔开")
arr = input("")    #输入一个一维数组，每个数之间使空格隔开
myList = [int(n) for n in arr.split()]    #将输入每个数以空格键隔开做成数组

print("经过快速排序后的数组为")
QuickSort(myList,0,len(myList)-1)
print(myList)
