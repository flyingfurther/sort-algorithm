def bubble_sort(lists):
    """冒泡排序"""
    count = len(lists)
    for i in range(0, count):
        for j in range(0, count - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


def bubble_sort_yield(lists):
    """
    冒泡排序
    使用yield输出为整个排序的过程
    """
    count = len(lists)
    for i in range(0, count):
        for j in range(0, count - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
                yield lists

if __name__ == '__main__':
    lists = [2,3,1,5]
    for x in bubble_sort_yield(lists):
        print(x)
    print(bubble_sort(lists))
