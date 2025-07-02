from latent_intuition_pruning import build_sample_tree, DecisionNode

def plain_dfs(node, visited):
    if node.id in visited:
        return
    print(f"Visited {node.id}")
    visited.add(node.id)
    for child in node.children:
        plain_dfs(child, visited)

root = build_sample_tree()

print("\n--- Baseline DFS (no interest weighting) ---")
plain_dfs(root, set())
