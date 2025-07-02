
from latent_intuition_pruning import build_sample_tree, IntuitionPruner
import time

# Build the decision tree
root = build_sample_tree()
pruner = IntuitionPruner()

# Simulated user behavior
hover_data = {
    "C": 3.0,  # User hovers longer on "Explore Beaches"
    "E": 2.5,  # Interest in "Surfing Spots"
    "G": 1.5   # Some curiosity for "Snorkeling Caves"
}

for node_id, duration in hover_data.items():
    pruner.simulate_hover(node_id, duration)

# Explore with pruning
start = time.time()
pruner.explore(root)
end = time.time()

# Print traversal and weights
print("\nTraversal Order with Behavior Weights:")
for node_id, weight in pruner.path_log:
    print(f"Visited {node_id} with interest score {weight:.2f}")

# Print performance metrics
print(f"\nTotal nodes visited: {len(pruner.path_log)}")
print(f"Time taken: {end - start:.5f} seconds")
