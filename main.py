from latent_intuition_pruning import build_sample_tree, IntuitionPruner

root = build_sample_tree()

pruner = IntuitionPruner()
pruner.simulate_hover("C", 3.0)
pruner.simulate_hover("E", 2.5)

pruner.explore(root)

print("\nTraversal Order with Behavior Weights:")
for node_id, weight in pruner.path_log:
    print(f"Visited {node_id} with interest score {weight:.2f}")
