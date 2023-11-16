def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            left = mid + 1  # Discard the left half
        else:
            right = mid - 1  # Discard the right half

    return -1  # Target not found

# Example list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

'''
for non-sorting list, we'll do sorted binary search
my_list.sort()
'''

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the list")
