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
        edges.append((neighbour, node))

def find_edges(bag_color):
    res = [bag_color]
    for edge in filter(lambda x: bag_color in x[0], edges):
        res.extend(find_edges(edge[1]))
    return res


res = set(find_edges('shiny gold'))
res.remove('shiny gold')
print(len(res))


