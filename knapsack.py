def knapsack(v,w,n,W):
	V = [[None for x in range(W+1)] for x in range(len(v)+1)]
	keep = [[0 for x in range(W+1)] for x in range(len(v)+1)]
	take = []
	for wy in range(W+1):
		V[0][wy] = 0
	for i in range(1,n+1):
		for wx in range(W+1):
			if w[i-1] <= wx:
				V[i][wx] = max(V[i-1][wx], v[i-1]+V[i-1][wx-w[i-1]])
				keep[i][wx] = 1
			else:
				V[i][wx] = V[i-1][wx]
				keep[i][wx] = 0
	i,k = len(v), W
	while i>0 and k>0:
		if V[i][k] != V[i-1][k]:
			take.append(i)
			i -= 1
			k -= w[i]
		else:
			i -= 1
	temp = [0]*n
	take = sorted(take)
	for i in range(len(take)):
		temp[take[i]-1] = 1
	result = str(V[n][W]) + ' ' + str(1) + '\n'
	result += ' '.join(map(str,temp))
	return result

# print knapsack(v = [16,19,23,28], w=[2,3,4,5],n=4,W=6)
def format_data(file_chunks):
    lines = file_chunks.split('\n')
    firstLine = lines[0].split()
    n = int(firstLine[0])
    W = int(firstLine[1])
    items = []
    v,w = [],[]
    for i in range(1,n+1):
    	if lines[i].split()[0]:
    		v.append(int(lines[i].split()[0]))
    	if lines[i].split()[1]:
    		w.append(int(lines[i].split()[1]))

    return knapsack(v,w,n,W)


