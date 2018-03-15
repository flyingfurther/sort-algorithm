def bucket_sort(lst):
    # 桶排序，基数排序
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        buckets[lst[i]-min(lst)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res


if __name__ == "__main__":
    lists = [2, 3, 56, 3, 2, 5, 67, 4, 6]
    a = bucket_sort(lists)
    print(a)