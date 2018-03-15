def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


if __name__ == '__main__':
    lists = [2, 3, 1, 5, 4, 6]
    print(select_sort(lists))
