arr = list(map(int, input("Enter elements: ").split()))

unique_arr = list(set(arr))

if len(unique_arr) < 2:
    print("Second largest element does not exist")
else:
    unique_arr.sort(reverse=True)
    print("Second largest element is:", unique_arr[1])
