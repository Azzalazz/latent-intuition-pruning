from latent_intuition_pruning import build_sample_tree, IntuitionPruner
import time

# Build the tree
root = build_sample_tree()

# Initialize the pruner with epsilon (exploration chance) and decay (fading attention)
pruner = IntuitionPruner(epsilon=0.15, decay=0.85)

# Simulated user interest: hover durations per node (in seconds)
hover_data = {
    "C": 3.0,   # User paused longer on beaches
    "E": 2.5,   # User showed interest in surfing spots
    "G": 1.5,   # Mild interest in snorkeling caves
    "B": 0.5    # Very low interest in mountains
}

# Apply simulated hover behavior to each node
for node_id, duration in hover_data.items():
    pruner.simulate_hover(node_id, duration)

# Start the adaptive exploration
print("\n🌿 Starting Latent Intuition Pruning traversal...")
start = time.time()
pruner.explore(root)
end = time.time()

# Output the traversal path and interest scores
print("\n✅ Traversal Log (with interest scores and depth):")
for node_id, raw_weight, depth, score in pruner.path_log:
    print(f"Visited {node_id} | Hover: {raw_weight:.2f} | Depth: {depth} | Score: {score:.2f}")

# Summary metrics
print("\n📊 Summary:")
print(f"Total nodes visited: {len(pruner.path_log)}")
print(f"Total time taken: {end - start:.5f} seconds")
print(f"Exploration epsilon: {pruner.epsilon}, Interest decay: {pruner.decay}")
