def findtopological():
    adj_cycle = [[1], [2], [3, 0], [], [1], [4]]
    adj_DAG = [[], [], [3], [1], [0, 1], [2, 0]]

    stack = []

    prob = adj_cycle
    visited = [False for i in prob]

    for i in range(len(prob)):
        temp = []
        if not visited[i]:
            DFS(prob, stack, visited, i, temp)
    print(stack[::-1])

def DFS(adj, stack, visited, index, temp):
    visited[index] = True
    temp.append(index)

    for i in adj[index]:
        if len(temp) > 0 and i in temp[:-1]:
            start = temp.index(i)
            temp.append(i)
            print('cycle', temp[start:])
            temp = []
        if not visited[i]:
            DFS(adj, stack, visited, i, temp)

    stack.append(index)

findtopological()