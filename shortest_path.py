from priodict import priorityDictionary

def Dijkstra(G,start,end=None):

	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()	# estimated distances of non-final vertices
	Q[start] = 0

	for v in Q:
		D[v] = Q[v]
		if v == end: break

		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError("Dijkstra: found better path to already-final vertex")
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v

	return (D,P)

def shortestPath(G,start,end):

	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path

G = {'s': {'u':10, 'x':5},'u': {'v':1, 'x':2},'v': {'y':4},	'x':{'u':3,'v':9,'y':2},'y':{'s':7,'v':6}}

#print(Dijkstra(G,'s'))
wein = shortestPath(G,'s','y')
weinlen = 0
for b in range(0,(len(wein)-1)):
	weinlen = weinlen + G[wein[b]][wein[b+1]]

print(weinlen)
