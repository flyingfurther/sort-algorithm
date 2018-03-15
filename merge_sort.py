def merge(left, right):
    # 二路归并过程
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# 归并排序
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[: num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == "__main__":
    lists = [2, 3, 56, 3, 2, 5, 67, 4, 6]
    a = merge_sort(lists)
    print(a)
