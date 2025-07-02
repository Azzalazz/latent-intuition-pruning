from latent_intuition_pruning import build_sample_tree, IntuitionPruner

def test_hover_behavior():
    print("Running Test Case: Prioritized Exploration")
    root = build_sample_tree()
    pruner = IntuitionPruner()
    pruner.simulate_hover("C", 3.0)
    pruner.simulate_hover("E", 2.5)
    pruner.explore(root)
    expected_order = ["A", "C", "E", "F"]
    actual_order = [node_id for node_id, _ in pruner.path_log]
    assert actual_order == expected_order, f"Expected {expected_order}, got {actual_order}"
    print("✅ Passed.")

test_hover_behavior()
