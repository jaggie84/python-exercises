arr = [2, 4, 5]
arr2 = [2, 3, 6]

def addVectors(list, list2):
    addList = []
    for i in range(0, len(list)):
        addList.append(list[i] + list2[i])    
    return addList

print(addVectors(arr, arr2))
