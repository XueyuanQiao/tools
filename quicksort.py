def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    before = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    after = [x for x in arr if x > pivot]
    return quicksort(before) + middle + quicksort(after)

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1, 4, 5, 9]
    sorted_arr = quicksort(arr)
    print(sorted_arr)
