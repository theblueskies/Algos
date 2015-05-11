graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def dfs(graph, start, end, path=[]):
    path = path+[start]
    if start==end:
        return path
    for node_next in graph.get(start,[]):
        if node_next not in path:
            newPath = dfs(graph,node_next,end,path)
            if newPath!=None:
                return newPath
    return None

print dfs(graph, '1', '11',[])
