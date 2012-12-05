f = open("/Users/johannesverwijnen/Downloads/edges.txt","r")
f.readline()
nodes = []
for i in range(500):
  	nodes.append([])
edges = []
line = f.readline()
i=0
while line!='':
	fields = line.split()
	e1 = int(fields[0])-1
	e2 = int(fields[1])-1
	w = int(fields[2])
	edge = (e1,e2,w)
	edges.append(edge)
	nodes[e1].append(i)
	nodes[e2].append(i)
	i+=1
	line=f.readline()

X=[0]
T=[]
while len(X)<500:
	mini = 0
	nextedge = None
	print("X: ",X)
	for node in X:
		print("Checking node: ",node)
		for e in nodes[node]:
			edge = edges[e]
			print("Looking at edge: ", edge)
			if nextedge==None or ((edge[0] not in X or edge[1] not in X) and edge[2]<mini):
				print("This is minimum!")
				nextedge=edge
				mini = edge[2]
	r_node=None
	if(nextedge[0] in X):
		r_node=nextedge[1]
	else:
		r_node=nextedge[0]
	print("Found minimum cost edge ", nextedge, "from node", r_node)
	X.append(r_node)
	T.append(nextedge)
cost=0
for edge in T:
	cost += edge[2]
print(cost)

