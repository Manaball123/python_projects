from network import network

n1 = network(5)

#init le connections

n1.vertices[0].connections.append(0)
n1.vertices[0].connections.append(1)
n1.vertices[0].connections.append(2)
n1.vertices[0].connections.append(3)

n1.vertices[1].connections.append(4)

n1.vertices[2].connections.append(1)
n1.vertices[2].connections.append(3)
n1.vertices[2].connections.append(4)

n1.vertices[3].connections.append(0)
n1.vertices[3].connections.append(4)

n1.vertices[4].connections.append(0)


print(n1.FindTotalConnections(2))



















