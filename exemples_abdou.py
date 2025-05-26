import networkx as nx
import matplotlib.pyplot as plt

def welsh_powell(G):
    nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    colors = {}  
    for node in nodes:
        used_colors = {colors.get(neighbor) for neighbor in G.neighbors(node) if neighbor in colors}
        color = 1
        while color in used_colors:
            color += 1
        colors[node] = color
    return colors , len(set(colors.values()))


def draw_graph(G, colors, title):
    fig, ax = plt.subplots(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)
    node_colors = [colors[node] for node in G.nodes()]
    chromatic_number = len(set(colors.values()))

    nx.draw(G, pos, ax=ax, with_labels=True,
            node_color=node_colors, cmap=plt.cm.Set1,
            edge_color='gray', node_size=800)

    ax.set_title(title, fontsize=16, fontweight='bold', color='darkblue', pad=20)

    fig.text(0.92, 0.5, f"γ = {chromatic_number}", ha='left', va='center',
             fontsize=14, bbox=dict(facecolor='white', edgecolor='black'))
    plt.show()




''' si C est un cycle alors : γ (C) = 2 si C est un cycle pair
 y(C) = 3 si C est un cycle impair  '''

G_cycle_pair = nx.cycle_graph(6)
colors, num_colors = welsh_powell(G_cycle_pair)
draw_graph(G_cycle_pair, colors, f"Cycle Pair (6 sommets) - Couleurs utilisées: {num_colors}")


G_cycle_impair = nx.cycle_graph(7)
colors, num_colors = welsh_powell(G_cycle_impair)
draw_graph(G_cycle_impair, colors, f"Cycle Impair (7 sommets) - Couleurs utilisées: {num_colors}")


G_star = nx.star_graph(5)  
colors, num_colors = welsh_powell(G_star)
draw_graph(G_star, colors, f"Graphe en étoile - Couleurs utilisées: {num_colors}")


G_big = nx.Graph()
edges = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(3,7),(4,6),(5,7)]
G_big.add_edges_from(edges)
colors, num_colors = welsh_powell(G_big)
draw_graph(G_big, colors, f"Graphe complexe - Couleurs utilisées: {num_colors}")


G_tree = nx.balanced_tree(r=2, h=3)  # arbre binaire
colors, num_colors = welsh_powell(G_tree)
draw_graph(G_tree, colors, f"Arbre (sans cycle) - Couleurs utilisées: {num_colors}")

#auto : 

G_auto = nx.gnp_random_graph(12, 0.3, seed=42)
colors, num_colors = welsh_powell(G_auto)
draw_graph(G_auto, colors, f"Graphe aléatoire - Couleurs utilisées: {num_colors}")


''' γ (Kn) = n '''

G1 = nx.Graph()
G1.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5)])
colors1, num_colors1 = welsh_powell(G1)
print("Graphe 1 - Petit graphe manuel :")
print("Couleurs :", colors1)
print("Nombre de couleurs :", num_colors1)
draw_graph(G1, colors1, f"Graphe 1 - Manuel (Couleurs : {num_colors1})")


# 2. Graphe complet K8 → γ(K8) = 8
G2 = nx.complete_graph(8)
colors2, num_colors2 = welsh_powell(G2)
print("Graphe 2 - Complet K8 :")
print("Couleurs :", colors2)
print("Nombre de couleurs :", num_colors2)
draw_graph(G2, colors2, f"Graphe 2 - Complet K8 (Couleurs : {num_colors2})")



# 3. Grille 4x4

G3 = nx.grid_2d_graph(4, 4)
G3 = nx.convert_node_labels_to_integers(G3)  # relabel to 0..15
colors3, num_colors3 = welsh_powell(G3)
print("Graphe 3 - Grille 4x4 :")
print("Couleurs :", colors3)
print("Nombre de couleurs :", num_colors3)
draw_graph(G3, colors3, f"Graphe 3 - Grille 4x4 (Couleurs : {num_colors3})")


# 4. Graphe pondéré
G4 = nx.Graph()
G4.add_weighted_edges_from([
    (0, 1, 3), (0, 2, -2), (1, 2, 4), (2, 3, 1),
    (3, 4, -1), (4, 5, 2), (5, 0, 1)
])
colors4, num_colors4 = welsh_powell(G4)
print("Graphe 4 - Pondéré :")
print("Couleurs :", colors4)
print("Nombre de couleurs :", num_colors4)
draw_graph(G4, colors4, f"Graphe 4 - Pondéré (Couleurs : {num_colors4})")



G5 = nx.gnp_random_graph(10, 0.4, seed=42)
colors5, num_colors5 = welsh_powell(G5)
print("Graphe 5 - Aléatoire :")
print("Couleurs :", colors5)
print("Nombre de couleurs :", num_colors5)
draw_graph(G5, colors5, f"Graphe 5 - Aléatoire (Couleurs : {num_colors5})")