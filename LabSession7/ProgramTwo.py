def binarySearch(lst, low, high, searchElement):
    if low <= high:
        mid = (low + high) // 2
        if lst[mid] == searchElement:
            return mid + 1
        elif lst[mid] <= searchElement:
            return binarySearch(lst, mid + 1, high, searchElement)
        else:
            return binarySearch(lst, low, mid - 1, searchElement)
    return -1
        
l = ["alex", "lara", "joe", "orion", "clark"]
l.sort()
print(l)
inp = input("Enter the name to find from the list: ").lower()
res = binarySearch(l, 0, len(l) - 1, inp)
if res == -1:
    print(f"Name {inp} not found in the list.")
else:
    print(f"Name {inp} found at position: {res}")