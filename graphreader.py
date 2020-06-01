
def readgraph(file, countvertex=False, countedges=False):
    datainput = open(file, "r")  # replace first argument with wanted graph

    graph = []

    linereader = datainput.readlines()  # Create object so the .readlines() method is only called once
    datainput.close()

    # DO NOT EDIT THESE LINES!!
    line = int(0)
    indexread = int(0)

    # This loop reads each line of the file.
    while True:  # Not ideal. Change ASAP/Find better approach.
        try:
            graph.append(linereader[line].split())
            line += 1
        except IndexError:
            break  # Stop loop after file runs out of lines

    printer_list = []  # Auxiliary list to help print the relations
    for i in range(0, len(graph)):  # this is to print the relations in a graph list way.
        while True:  # Use while since the lenght of a relationship is unknown.
            try:  # run these lines until program finds an exception. Occurs when there's no more relationships.
                printer_list.append(graph[i][indexread])
                indexread += 1  # this is needed to trigger an exception.
            except IndexError:
                print(printer_list[0], ": ", end='')  # end='' means no new line appended to string
                printer_list.remove(printer_list[0])  # Remove index 0 so it is not printed (Avoid self loop)
                print(printer_list)  # Print only the relationships
                printer_list = []  # Clear the list to receive new values
                indexread = 0  # Zero the index to read, since new values will be read.
                break

    if countvertex:
        vertexcountlist = []
        print("WARNING! HIGH COMPLEXITY OPERATION. THIS MAY TAKE A WHILE")
        for k in range(0, len(graph)):
            for j in range(0, len(graph[k])):
                if graph[k][j] not in vertexcountlist:
                    vertexcountlist.append(graph[k][j])
        countingvertex = len(vertexcountlist)
        print("Number of vertex: ", countingvertex)

    if countedges:
        countingedges = int(0)
        for m in range(0, len(graph)):
            countingedges += len(graph[m])
        countingedges -= len(graph)
        print("Number of edges:", countingedges)

    if countedges and countvertex:
        print("Complexity: ( {} + {} )".format(countingvertex, countingedges))
