import re

path = "day7.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()

graph = { }

for z in data:
    m = re.match(r'(\w+ \w+) bags contain (.*).', z)
    if(m):
        node = m.group(1)
        neighbours = []
        for edge in m.group(2).split(', '):
            e = re.match(r'(\d) (\w+ \w+) bag', edge)
            if(e):
                neighbours.append(e.group(2))
        graph[node] = neighbours

edges = []

for node in graph:
    for neighbour in graph[node]:
        edges.append((node, neighbour))

def find_edge_paths(neighbour):
    # todo recurse 'up' from shiny gold
    other_nodes = list(map(lambda y: y[0], filter(lambda x: neighbour in x[1], edges)))
    
    if(len(other_nodes) == 0):
        return [neighbour]

    for other_node in other_nodes:
        if(len(other_node) > 0):
            edge_paths = find_edge_paths(other_node)
            if(edge_paths is True and len(edge_paths) > 0):
                return edge_paths.extend(neighbour)

print(find_edge_paths('shiny gold'))