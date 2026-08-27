# 一种转至行列式的代码
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    for row in range(len(tableData[0])):
        for col in range(len(tableData)) :
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()


printTable(tableData)


                 