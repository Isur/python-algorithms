"""
    Find max
"""


def loadFromFile(path):
    with open(path) as file:
        data = file.read()
    return data


def parseData(data):
    text = data.split(";")
    array = []
    for num in text:
        array.append(float(num))
    return array


def findMax(data):
    maxVal = data[0]
    for item in data:
        if maxVal < item:
            maxVal = item
    return maxVal


fileData = loadFromFile("./I_01.txt")
parsedData = parseData(fileData)
maxValue = findMax(parsedData)
print(maxValue)
