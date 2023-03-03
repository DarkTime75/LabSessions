#  Develop an iterative solution for binary search. 

lst = [10, 20, 30, 40, 50, 60]
toSearch = int(input("Enter the number to search: "))
low = 0
high = len(lst) - 1

while low <= high:
    mid = (low + high) // 2
    if lst[mid] == toSearch:
        print(f"The number {toSearch} was found at position: {mid + 1}")
        break
    elif lst[mid] <= toSearch:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"The number {toSearch} was not found in the list.")