
from latent_intuition_pruning import build_sample_tree, IntuitionPruner

def run_test(name, hover_map, expected_path):
    print(f"\n🧪 Running Test: {name}")
    root = build_sample_tree()
    pruner = IntuitionPruner(epsilon=0.0, decay=1.0)  # disable decay/random for test

    for node_id, duration in hover_map.items():
        pruner.simulate_hover(node_id, duration)

    pruner.explore(root)
    actual_path = [node_id for node_id, *_ in pruner.path_log]
    print("Expected:", expected_path)
    print("Actual:  ", actual_path)

    if actual_path == expected_path:
        print("✅ Test passed.")
    else:
        print("❌ Test failed.")

# Test Case 1
run_test(
    "Prioritize Beaches",
    hover_map={"C": 3.0, "E": 2.5},
    expected_path=["A", "C", "E", "F", "G", "H", "B", "D"]
)

# Test Case 2
run_test(
    "Tie Handling",
    hover_map={"B": 2.0, "C": 2.0},
    expected_path=["A", "B", "D", "C", "E", "F", "G", "H"]
)

# Test Case 3
run_test(
    "Minimal Interest",
    hover_map={"G": 1.0},
    expected_path=["A", "B", "D", "C", "E", "F", "G", "H"]
)
