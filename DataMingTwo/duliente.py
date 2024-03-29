import math

def inputData():
    data = []

    data = list(map(int, input("Enter the list of data : ").split()))
    return data


def displayData(data):
    print(data)
    return

def displayResult(res):
    print(res)
    return

def binByWidth(data, k):
    w = math.ceil(float(max(data)-min(data))/k)

    binIndex = []
    for i in range(0, k+1):
        binIndex += [min(data) + w * i]

    binResult = []
    for i in range(0, k):
        bin =[]
        for j in data:
            if (j <= binIndex[i+1] and j >= binIndex[i]):
                bin.append(j)
        binResult.append(bin)
    return binResult

def binByFrequency(data, k):
    length = len(data)
    w = math.ceil(length / k)
    pos = 0

    binResult = []
    for i in range(0, k):
        bin = []
        for j in range(0, w):
            if (pos >= length):
                break
            elif (j >= length):
                break
            else:
                bin.append(data[pos])
                pos += 1
        binResult.append(bin)
    return binResult

def binByMeans(data, k):
    length = len(data)
    w = math.ceil(length / k)
    pos = 0
    
    binResult = []
    for i in range(0, k):
        total = 0
        size = 0
        bin = []
        for j in range(0, w):
            if (pos >= length):
                break
            elif (j >= length):
                break
            else:
                total += data[pos]
                pos += 1
                size += 1
        total /= size
        print(total)

        for k in range(0, w):
            bin.append(int(total))
        binResult.append(bin)
    return binResult

def binByBoundary(data, k):
    length = len(data)
    w = math.ceil(length / k)
    pos = 0
    
    binResult = []
    for i in range(0, k):
        lowest = 0
        highest = 0
        
        temp = []
        for j in range(0, w):
            if (pos >= length):
                break
            elif (j >= length):
                break
            else:
                temp.append(data[pos])
                pos += 1
        lowest = min(temp)
        highest = max(temp)
        
        bin = []
        for k in range(0, w-1):
            bin.append(lowest)
        bin.append(highest)
        
        binResult.append(bin)
    return binResult
  
def showMenuOptions():
    print("\nMain Menu")
    print("1. Enter new data")
    print("2. Display data")
    print("3. Display result")
    print("4. Bin data using width")
    print("5. Bin data using frequency")
    print("6. Exit")
    choice = int(input("Enter choice : "))
    return choice

def inputWidth():
    width = int(input("\nEnter bin width : "))
    return width

data = []
k = 0
binResult = []

while True:
    choice = showMenuOptions()
    if (choice == 1):
        data = inputData()
        continue
    elif (choice == 2):
        displayData(data)
        continue
    elif (choice == 3):
        displayResult(binResult)
    elif (choice == 4):
        k = inputWidth()
        binResult = binByWidth(data, k)
        continue
    elif (choice == 5):
        k = inputWidth()
        binResult = binByFrequency(data, k)
        continue
    elif (choice == 6):
        break
    else:
        print("\nError: The choice does not exist... try again.")
        continue
print("End of program")