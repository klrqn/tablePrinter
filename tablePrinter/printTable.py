#! python3
# formats and screen prints a table

exTable = tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
longestItem = 0
rowLen = 0
bffer = 5

for row in exTable:
    if isinstance(row, list):
        concat = ''
        for item in row:
            if len(item) > longestItem:
                longestItem = len(item)
            concat += " | " + item.center(longestItem + bffer)
        print(concat + " | ")
        if rowLen < (len(concat) + 3):
            rowlen = (len(concat) + 3)
    print(rowlen * "=")

