import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def welsh_powell_coloring(G):
    # Get vertices sorted by degree (descending)
    vertices = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    colors = {}  # Store vertex: color assignments
    color_count = 0  # Current color index
    
    for vertex in vertices:
        # Get colors of adjacent vertices
        used_colors = {colors.get(neighbor) for neighbor in G.neighbors(vertex) if neighbor in colors}
        # Find the smallest unused color
        color = 0
        while color in used_colors:
            color += 1
        colors[vertex] = color
        color_count = max(color_count, color + 1)
    
    return colors, color_count

def visualize_graph(G, colors, title, filename):
    pos = nx.spring_layout(G)
    # Define a color map for visualization
    color_map = plt.cm.get_cmap('tab10')
    node_colors = [color_map(colors[node] / 10) for node in G.nodes()]
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=12, font_weight='bold')
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def matrix_to_graph(matrix):
    # Convert adjacency matrix to networkx graph
    G = nx.from_numpy_array(np.array(matrix))
    return G

def create_test_graphs():
    graphs = []
    
    # Graph 1: Small bipartite graph (6 vertices)
    bipartite_matrix = [
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]
    ]
    graphs.append((bipartite_matrix, "Bipartite Graph (6 vertices)", "graph1.png"))
    
    # Graph 2: Cycle graph C7 (7 vertices)
    cycle_matrix = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        cycle_matrix[i][(i + 1) % 7] = 1
        cycle_matrix[(i + 1) % 7][i] = 1
    graphs.append((cycle_matrix, "Cycle Graph C7", "graph2.png"))
    
    # Graph 3: Complete graph K5 (5 vertices)
    complete_matrix = [[0 if i == j else 1 for j in range(5)] for i in range(5)]
    graphs.append((complete_matrix, "Complete Graph K5", "graph3.png"))
    
    # Graph 4: Sparse tree-like graph (10 vertices)
    tree_matrix = [[0 for _ in range(10)] for _ in range(10)]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 8), (5, 9)]
    for u, v in edges:
        tree_matrix[u][v] = 1
        tree_matrix[v][u] = 1
    graphs.append((tree_matrix, "Sparse Tree-like Graph (10 vertices)", "graph4.png"))
    
    # Graph 5: Random graph (20 vertices, edge prob 0.2)
    n = 20
    p = 0.2
    random_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                random_matrix[i][j] = 1
                random_matrix[j][i] = 1
    graphs.append((random_matrix, "Random Graph (20 vertices)", "graph5.png"))
    
    return graphs

def main():
    # Create test graphs
    test_graphs = create_test_graphs()
    
    # Process each graph
    for matrix, title, filename in test_graphs:
        # Convert matrix to graph
        G = matrix_to_graph(matrix)
        
        # Apply Welsh-Powell coloring
        colors, num_colors = welsh_powell_coloring(G)
        
        # Verify coloring
        valid = True
        for u, v in G.edges():
            if colors[u] == colors[v]:
                valid = False
                break
        
        # Print results
        print(f"\nGraph: {title}")
        print(f"Adjacency Matrix:")
        for row in matrix:
            print(row)
        print(f"Number of colors used: {num_colors}")
        print(f"Color assignments: {colors}")
        print(f"Valid coloring: {valid}")
        
        # Visualize and save graph
        visualize_graph(G, colors, title, filename)

if __name__ == "__main__":
    main()

# Execution Instructions:
# 1. Install required libraries: pip install networkx matplotlib numpy
# 2. Save this code as `welsh_powell_matrix.py`.
# 3. Run the script: python welsh_powell_matrix.py
# 4. Output: Console displays adjacency matrix, color assignments, number of colors, and validity for each graph.
#    Images are saved as graph1.png, graph2.png, etc., for inclusion in the report.