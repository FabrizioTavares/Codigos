datainput = open("graph.txt", "r")  # replace first argument with wanted graph

graph = []

linereader = datainput.readlines()  # Create object so the .readlines() method is only called once

# DO NOT EDIT THESE LINES!!
line = int(0)
indexread = int(0)
#

while True:  # Not ideal. Change ASAP/Find better approach.
    try:
        graph.append(linereader[line].split())
        line += 1
    except IndexError:
        break

# vertex count = len(graph)

printerList = []  # Auxiliary list to help print the relations

for i in range(0, len(graph)):  # this is to print the relations in a graph list way.
    while True:  # Use while since the lenght of a relationship is unknown. 'for' can also be used, only if lenght known
        try:  # run these lines until program finds an exception. Occurs when there's no more relationships.
            printerList.append(graph[i][indexread])
            indexread += 1  # this is needed to trigger an exception.
        except IndexError:
            print(printerList[0], ": ", end='')  # end='' means no new line appended to string
            printerList.remove(printerList[0])
            print(printerList)
            printerList = []
            indexread = 0
            break
