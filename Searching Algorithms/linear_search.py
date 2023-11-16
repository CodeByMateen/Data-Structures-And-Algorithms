def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return the index

    return -1  # Target not found

# Example List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

'''
for non-sorting list, we'll do sorted linear search
my_list.sort()
'''

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the list")
