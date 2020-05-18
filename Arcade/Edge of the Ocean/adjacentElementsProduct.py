def adjacentElementsProduct(inputArray):
    productList = [] # store porducts of two adjacent numbers
    for index in range(0, len(inputArray) - 1): # before the last element -2 index
        productList.append(inputArray[index] * inputArray[index + 1])
    return max(productList)