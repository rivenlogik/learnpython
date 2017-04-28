
def printTable(table):
    colWidths = [0] * len(table)
    index = 0
    for i in table:
        itemLength = 0
        for v in i:
            if colWidths[index] < len(v):
                colWidths[index] = len(v)

        index += 1

    print(colWidths)

    for x in range(len(table[0])):
        for y in range(len(table)):
           print(table[y][x].rjust(colWidths[y] + 1), end='')

        print()
                  
              
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
