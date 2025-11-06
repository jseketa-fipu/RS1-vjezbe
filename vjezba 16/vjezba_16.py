# Vježba 16: Implementacija Dijsktra algoritma za pronalaženje najkraćeg puta

# Napišite funkciju dijkstra(graph, start) koja prima graf predstavljen kao rječnik susjedstva i početni čvor te vraća rječnik s najkraćim udaljenostima od početnog čvora do svih ostalih čvorova u grafu koristeći Dijsktra algoritam.

# Za rješavanje zadatka možete koristiti modul heapq za gotovu implementaciju prioritetnog reda.

# Primjer ulaznih podataka

# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 2), ('D', 5)],
#     'C': [('A', 4), ('B', 2), ('D', 1)],
#     'D': [('B', 5), ('C', 1)]
# }

# Primjer poziva funkcije:

# print(dijkstra(graph, 'A'))
# # {'A': 0, 'B': 1, 'C': 3, D': 4}
import heapq


def dijkstra(graph, start):
    # dist will store the shortest known distance from start to each node
    # all nodes have a distance of infinity until discovered
    dist = {node: float("inf") for node in graph}
    # start node always has a distance of 0 to itself
    dist[start] = 0

    # priority queue: pairs (current_distance, node)
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # if popped worse distance, skip
        if curr_dist > dist[node]:
            continue

        # Iterate over neighbors
        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            # if shorter path to the neighbor found, update and push to the queue
            if new_dist < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


# Example
if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }

    print(dijkstra(graph, "A"))
    # Expected: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
