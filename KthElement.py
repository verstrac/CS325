# Caleb Verstraete
# CS325
# Date 1/23/23

def kthElement(arr1, arr2, k):
    arr1_pointer = 0
    arr2_pointer = 0
    new_combined_arr = []

    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        if arr1[arr1_pointer] < arr2[arr2_pointer]:
            new_combined_arr.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else:
            new_combined_arr.append(arr2[arr2_pointer])
            arr2_pointer += 1

    while arr1_pointer < len(arr1):
        new_combined_arr.append(arr1[arr1_pointer])
        arr1_pointer += 1

    while arr2_pointer < len(arr2):
        new_combined_arr.append(arr2[arr2_pointer])
        arr2_pointer += 1

    return new_combined_arr[k - 1]



if __name__ == '__main__':
    print(kthElement([-1, 2, 3, 5, 6, 7, 9, 10], [-3, 4, 5, 6, 7], 1))
