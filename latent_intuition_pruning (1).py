
import random

class DecisionNode:
    def __init__(self, node_id, label):
        self.id = node_id              # Unique identifier for the node
        self.label = label            # Human-readable label
        self.children = []            # Child nodes in the decision tree

    def add_child(self, child):
        self.children.append(child)


class IntuitionPruner:
    def __init__(self, epsilon=0.1, decay=0.9):
        self.weights = {}             # Hover-based interest weights
        self.visited = set()          # Set of visited node IDs
        self.path_log = []            # Logs visited nodes with metadata
        self.epsilon = epsilon        # Probability of exploring randomly
        self.decay = decay            # How much weights decay each step

    def simulate_hover(self, node_id, hover_time):
        """
        Simulates a user hovering over a node, increasing its interest score.
        """
        self.weights[node_id] = self.weights.get(node_id, 0) + hover_time

    def decay_all_weights(self):
        """
        Gradually decreases all interest weights to reflect fading attention.
        """
        for node in self.weights:
            self.weights[node] *= self.decay

    def explore(self, node, depth=0):
        """
        Recursively explores the decision tree, prioritizing high-interest paths,
        and optionally injecting randomness for exploration.
        """
        if node.id in self.visited:
            return

        self.visited.add(node.id)

        # Compute effective score factoring in depth to penalize deep paths
        raw_weight = self.weights.get(node.id, 0)
        effective_score = raw_weight / (depth + 1)
        self.path_log.append((node.id, raw_weight, depth, effective_score))

        # Apply decay after visiting each node
        self.decay_all_weights()

        # No children: leaf node
        if not node.children:
            return

        # ε-greedy behavior: with ε probability, randomly shuffle children
        if random.random() < self.epsilon:
            children = list(node.children)
            random.shuffle(children)
        else:
            # Otherwise, prioritize children by highest interest weight
            children = sorted(node.children, key=lambda c: -self.weights.get(c.id, 0))

        # Recursively explore children
        for child in children:
            self.explore(child, depth + 1)


def build_sample_tree():
    """
    Constructs a sample decision tree used for testing and demonstration.
    """
    root = DecisionNode("A", "Start")
    node_b = DecisionNode("B", "Explore Mountains")
    node_c = DecisionNode("C", "Explore Beaches")
    node_d = DecisionNode("D", "Hiking Trails")
    node_e = DecisionNode("E", "Surfing Spots")
    node_f = DecisionNode("F", "Hidden Waterfalls")
    node_g = DecisionNode("G", "Snorkeling Caves")
    node_h = DecisionNode("H", "Beachside Restaurants")

    # Building tree structure
    root.add_child(node_b)
    root.add_child(node_c)
    node_b.add_child(node_d)
    node_c.add_child(node_e)
    node_e.add_child(node_f)
    node_e.add_child(node_g)
    node_c.add_child(node_h)

    return root
