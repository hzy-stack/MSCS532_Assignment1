def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # shift all elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        # place key into right position
        arr[j + 1] = key
    return arr


def test():
    data = [5, 2, 9, 1, 5, 6]
    print("Original:", data)

    sorted_desc = insertion_sort_desc(data)
    print("Sorted descending order:", sorted_desc)


if __name__ == "__main__":
    test()
