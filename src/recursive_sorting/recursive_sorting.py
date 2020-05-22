# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(A, B):
    # init the combined list that will hold the sorted elements from both A and B
    # combined = [0] * (len(A) + len(B))
    # combined = [0 for _ in range(len(A) + len(B))]
    combined = []

    # init the two pointers that start at each list
    a = 0
    b = 0


    while a < len(A) and b < len(B):
        # compare the elements that a and b point at
        if A[a] < B[b]:
            combined.append(A[a])
            a += 1
        else:
            combined.append(B[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list
    while a < len(A):
        combined.append(A[a])
        a += 1
    while b < len(B):
        combined.append(B[b])
        b += 1

    return combined
    
def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # begin with the first element in the right
    # half of th elist
    start2 = mid + 1

    # if the two halves we are merging are alredy sorted
    # we do not have to do anything
    if arr[mid] <= arr[start2]:
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # now shift all the element between element 1
            # element 2, right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r)/2, but avoids overflow
        # for large l and r
        m = l + (r - l)//2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
