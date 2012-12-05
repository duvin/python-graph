def loadGraph(file, bidirectional=True, dense=True):
    """Read edges from a file and return a tuple with the
    list of edges in the first position and a list of lists of
    edge positions (the position in the outer list corresponding
    to the node#) in the second position. In case of
    bidirectional being true, each edge is added twice to the
    node list (once for each end).
    In case of dense being false a third list is returned, which
    consists of node#s (corresponding to the edges in the second
    list)

    file -- a file open for reading
    """
    graph = [] #init empty list
    nodes = []
    node_edges = []
    i = 0
    file.readline()
    for line in file: #go through file one row at a time
        fields = line.split() #split row by commas
        fro = int(fields[0])
        to = int(fields[1])
        weight = int(fields[2])
        edge = (fro,to,weight)
        graph.append(edge)
        if fro in nodes: #do we have the originating node?
            node_edges[nodes.index(fro)].append(i)
        else: #add the originating node
            nodes.append(fro)
            node_edges.append([i])
        if bidirectional: #also do the other way around
            if to in nodes:
                node_edges[nodes.index(to)].append(i)
            else:
                nodes.append(to)
                node_edges.append([i])
        i += 1
    if dense: #reshuffle nodes to positions
        node_edges = [[] for x in range(max(nodes))]
        for i in range(len(graph)):
            node_edges[graph[i][0]-1].append(i)
            if bidirectional:
                node_edges[graph[i][1]-1].append(i)   
        return (graph,node_edges)
    else:
        return (graph,node_edges,nodes)