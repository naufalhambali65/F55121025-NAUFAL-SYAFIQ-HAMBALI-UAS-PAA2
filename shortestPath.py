import networkx as nx
import matplotlib.pyplot as plt
import time

# Algoritma TSP (Travelling Salesman Problem)
def tsp(graph, start_vertex):
    num_vertices = len(graph)
    path = [start_vertex]
    visited = [False] * num_vertices
    visited[start_vertex] = True
    total_distance = 0
    start_time = time.time()

    for _ in range(num_vertices - 1):
        current_vertex = path[-1]
        nearest_vertex = None
        shortest_distance = float('inf')

        for neighbor_vertex in range(num_vertices):
            if not visited[neighbor_vertex] and graph[current_vertex][neighbor_vertex] < shortest_distance:
                nearest_vertex = neighbor_vertex
                shortest_distance = graph[current_vertex][neighbor_vertex]

        path.append(nearest_vertex)
        visited[nearest_vertex] = True
        total_distance += shortest_distance

    path.append(start_vertex)
    total_distance += graph[path[-2]][start_vertex]

    end_time = time.time()
    execution_time = end_time - start_time

    return path, total_distance, execution_time

# Algoritma Dijkstra
def dijkstra(graph, start_vertex):
    num_vertices = len(graph)
    distance = [float('inf')] * num_vertices
    distance[start_vertex] = 0
    visited = [False] * num_vertices
    path = [-1] * num_vertices
    start_time = time.time()

    for _ in range(num_vertices - 1):
        min_distance = float('inf')
        current_vertex = None

        for vertex in range(num_vertices):
            if not visited[vertex] and distance[vertex] < min_distance:
                min_distance = distance[vertex]
                current_vertex = vertex

        visited[current_vertex] = True

        for neighbor_vertex in range(num_vertices):
            weight = graph[current_vertex][neighbor_vertex]
            if not visited[neighbor_vertex] and weight > 0 and distance[current_vertex] + weight < distance[neighbor_vertex]:
                distance[neighbor_vertex] = distance[current_vertex] + weight
                path[neighbor_vertex] = current_vertex

    end_time = time.time()
    execution_time = end_time - start_time

    return path, distance, execution_time

# Fungsi untuk mencetak rute terpendek
def print_shortest_path(path, distance):
    print("Shortest Path:")
    print("Path:", path)
    print("Distance:", distance)

# Fungsi untuk mencetak waktu komputasi
def print_execution_time(time_taken):
    print("Execution Time:", time_taken, "seconds")

# Fungsi utama
def main():
    # Membuat graf
    graph = [
        [0, 12, 10, 0, 0, 0, 12],
        [12, 0, 8, 12, 0, 0, 0],
        [10, 8, 0, 11, 3, 0, 9],
        [0, 12, 11, 0, 0, 10, 0],
        [0, 0, 3, 0, 0, 7, 6],
        [0, 0, 0, 10, 7, 0, 9],
        [12, 0, 9, 0, 6, 9, 0]
    ]

    while True:
        print("\nMenu:")
        print("1. TSP")
        print("2. Dijkstra")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            start_vertex = int(input("Enter the starting vertex (0-6): "))
            path, distance, execution_time = tsp(graph, start_vertex)
            print_shortest_path(path, distance)
            print_execution_time(execution_time)
        elif choice == 2:
            start_vertex = int(input("Enter the starting vertex (0-6): "))
            path, distance, execution_time = dijkstra(graph, start_vertex)
            print_shortest_path(path, distance)
            print_execution_time(execution_time)
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
