arr = [2, 4, 5]
arr2 = [2, 3, 6]
arr3 = [1, 1, 1]

def addVectors(list, list2, list3):
    addList = []
    for i in range(0, len(list)):
        addList.append(arr[i] + arr2[i] + arr3[i])    
    return addList

print(addVectors(arr, arr2, arr3))
