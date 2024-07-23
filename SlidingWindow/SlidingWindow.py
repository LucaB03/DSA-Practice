def fixSizeSlidingWindow(size, arr, sum):
    if len(arr) < size:
        return -1
    p1 = 0
    p2 = size - 1
    while p2 < len(arr):
        ans = 0
        for i in range(p1, p2 + 1):
            ans += arr[i]
        if ans == sum:
            return [p1, p2]
        p1 += 1
        p2 += 1
    return -1


def vSizeSlidingWindow(arr, sum):
    # TODO
    return -1


arr = [2, 1, 4, 1, 3, 1, 7, 1]
print(fixSizeSlidingWindow(3, arr, 9))
