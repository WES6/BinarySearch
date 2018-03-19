
"""
    二分法查找Python实现
"""


def binarySearch(arr, min, max, key):
    mid = int((max + min)/2)
    if key < arr[mid]:
        return binarySearch(arr, min, mid-1, key)
    elif key > arr[mid]:
        return binarySearch(arr, mid+1, max, key)
    elif key == arr[mid]:
        print("找到{0}了！是第{1}个数字！".format(key, mid))
    else:
        print("没找到！")


lis = [11, 22, 33, 44, 55, 66, 77, 88, 99]
result = binarySearch(lis, 0, 8, 66)
