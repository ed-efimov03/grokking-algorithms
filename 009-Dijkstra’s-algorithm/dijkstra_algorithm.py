import math

graph = {}

graph["начало"] = {}
graph["начало"]["a"] = 6
graph["начало"]["b"] = 2

graph["a"] = {}
graph["a"]["конец"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["конец"] = 5

graph["конец"] = {}


infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["конец"] = infinity


parents = {}
parents["a"] = "начало"
parents["b"] = "начало"
parents["конец"] = None


processed = set()


def find_lowest_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node 
    return lowest_cost_node


node = find_lowest_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_node(costs)

if __name__ == "__main__":
    print("Минимальные стоимости:", costs)