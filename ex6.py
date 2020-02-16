import networkx as nx

f = open("ex6input.txt","r")
orbit_map = f.read().split('\n')
print("input: ", orbit_map)
print("lenght of input:", len(orbit_map))

total_orbits = 0
G = nx.Graph()
for orbit in orbit_map:
    planet, orbiter = orbit.split(")")
    print("planet:",planet)
    print("orbiter:",orbiter)
    G.add_edge(planet,orbiter)

print(G.nodes)
print(G.edges)

for node in G.nodes:
    total_orbits += nx.shortest_path_length(G,"COM", node)

print(total_orbits)