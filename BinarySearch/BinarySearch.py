def binarySearch(lis, value, start=0, end=None):
    if not end:
        end = len(lis)-1
    if start <= end:
        midIndex = (start+end) // 2
        if value == lis[midIndex]:
            return midIndex
        if value < lis[midIndex]:
            return binarySearch(lis, value, start, midIndex-1)
        if value > lis[midIndex]:
            return binarySearch(lis, value, midIndex+1, end)
    else:
        return "Not found"
