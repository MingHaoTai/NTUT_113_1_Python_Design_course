def quick_sort(arr):
    # 如果陣列長度為 0 或 1，直接返回，因為已經是排序好的
    if len(arr) <= 1:
        return arr
    
    # 選擇基準點（這裡選擇中間的元素作為基準）
    pivot = arr[len(arr) // 2]
    
    # 將陣列分為三部分：小於基準點、等於基準點、大於基準點
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 遞迴排序左邊和右邊，然後合併
    return quick_sort(left) + middle + quick_sort(right)

# 測試
arr = [3, 6, 8, 10, 1, 2, 1, 11, 15, 12, 13, 4, 5, 9, 3]
sorted_arr = quick_sort(arr)
print("排序後的陣列：", sorted_arr)