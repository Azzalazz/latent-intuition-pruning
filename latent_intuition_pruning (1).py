class DecisionNode:
    def __init__(self, node_id, label):
        self.id = node_id
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class IntuitionPruner:
    def __init__(self):
        self.weights = {}
        self.visited = set()
        self.path_log = []

    def simulate_hover(self, node_id, hover_time):
        self.weights[node_id] = self.weights.get(node_id, 0) + hover_time

    def explore(self, node):
        if node.id in self.visited:
            return
        self.visited.add(node.id)
        self.path_log.append((node.id, self.weights.get(node.id, 0)))
        sorted_children = sorted(node.children, key=lambda c: -self.weights.get(c.id, 0))
        for child in sorted_children:
            self.explore(child)

def build_sample_tree():
    root = DecisionNode("A", "Start")
    node_b = DecisionNode("B", "Explore Mountains")
    node_c = DecisionNode("C", "Explore Beaches")
    node_d = DecisionNode("D", "Hiking Trails")
    node_e = DecisionNode("E", "Surfing Spots")
    node_f = DecisionNode("F", "Hidden Waterfalls")

    root.add_child(node_b)
    root.add_child(node_c)
    node_b.add_child(node_d)
    node_c.add_child(node_e)
    node_e.add_child(node_f)
    return root
