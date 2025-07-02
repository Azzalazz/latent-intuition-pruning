from latent_intuition_pruning import build_sample_tree

def plain_dfs(node, visited, depth=0):
    if node.id in visited:
        return
    print(f"Visited {node.id} | Depth: {depth}")
    visited.add(node.id)
    for child in node.children:
        plain_dfs(child, visited, depth + 1)

# Run plain DFS traversal
root = build_sample_tree()
visited = set()
print("\n🔍 Starting Baseline DFS Traversal...")
plain_dfs(root, visited)

print(f"\nTotal nodes visited in baseline DFS: {len(visited)}")
