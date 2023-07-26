# Linear search
def linear_search(l, e):
    return l.index(e) if e in l else -1

# Binary search (works on a sorted list)
def binary_search(l, e):
    low, high = 0, len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if l[mid] == e:
            return mid
        elif l[mid] < e:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Selection sort
def selection_sort(l):
    return sorted(l)

# Insertion sort
def insertion_sort(l):
    sorted_list = l.copy()
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
    return sorted_list

# Merge sort
def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left_half = merge_sort(l[:mid])
    right_half = merge_sort(l[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list

# Example usage:
sample_list = [4, 2, 7, 1, 9, 5]
element_to_find = 7

print("Linear Search:", linear_search(sample_list, element_to_find))
print("Binary Search:", binary_search(sorted(sample_list), element_to_find))
print("Selection Sort:", selection_sort(sample_list))
print("Insertion Sort:", insertion_sort(sample_list))
print("Merge Sort:", merge_sort(sample_list))
