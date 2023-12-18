def bubble_sort(arr):
  l = len(arr)
  for i in range(l):
    for j in range(l-1):
      if arr[j] > arr[j+1]:
        # temp = arr[j]
        # arr[j] = arr[j+1]
        # arr[j+1] = temp
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

lst = [3, 7, 5, 2, 1, 4, 6]
print(bubble_sort(lst))
