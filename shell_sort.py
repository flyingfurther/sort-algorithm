def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = count // 2
    while step > 0:
        for i in range(step, count):
                while i >= step and lists[i - step] > lists[i]:
                    lists[i], lists[i - step] = lists[i - step], lists[i]
                    i -= step
        step = step // 2
    return lists


if __name__ == '__main__':
    lists = [2, 3, 1, 5, 4, 6]
    print(shell_sort(lists))
