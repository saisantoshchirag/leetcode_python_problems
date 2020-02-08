def printPowerSet(arr, n):
    _list = []

    for i in range(2 ** n):
        subset = ""

        # consider each element in the set
        for j in range(n):

            # Check if jth bit in the i is set.
            # If the bit is set, we consider
            # jth element from set
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        # if subset is encountered for the first time
        # If we use set<string>, we can directly insert
        if subset not in _list and len(subset) > 0:
            _list.append(subset)
    print(_list)
    for subset in _list:

        # split the subset and print its elements
        arr = subset.split('|')
        for string in arr:
            print(string, end=" ")
        print() 
arr = [1,2,1]
n = 3
printPowerSet(arr,n)