Latent Intuition Pruning
A real-time adaptive search algorithm guided by subtle user behavior cues.

📌 Overview
Latent Intuition Pruning (LIP) is an adaptive, heuristic search technique that intelligently explores a decision tree by monitoring real-time user behavior—such as hover duration, hesitation, or path revisits. Unlike traditional rule-based or ML-heavy approaches, LIP dynamically updates its traversal priorities using live interaction data, without requiring any training phase or labeled datasets.

This algorithm is particularly useful for UI/UX personalization tools, exploratory decision-making systems, or interactive design assistants where implicit feedback is more informative than explicit user choices.

🔍 Key Features
Interaction-Aware Tree Search: Prioritizes traversal based on implicit user interest (e.g., pause time, hover frequency).

Zero ML Dependence: Does not require training, labeling, or batch learning—everything happens live.

Pluggable Heuristics: Can incorporate any measurable interaction metric into the weighting function.

Baseline Comparison: Includes standard DFS for comparison to quantify gains in relevance and efficiency.

▶️ Running the Project
bash
Copy
Edit
python main.py           # Runs the adaptive LIP algorithm
python baseline_dfs.py   # Runs the baseline DFS for comparison
python test_cases.py     # Executes a simple test case validating behavior
🧪 Evaluation Plan
Simulates user interaction by assigning hover times to tree nodes.

Demonstrates that LIP explores fewer irrelevant branches while converging faster on user-preferred options.

Outputs traversal path and interest scores to validate adaptivity.

Includes test cases where baseline DFS fails to prioritize relevant paths.

🔖 Git Tag for Grading
Version: v1.0-final
This tag marks the exact commit submitted for grading. All code and test results are reproducible from this state.

🛠 Requirements
Python 3.x

No external dependencies

Runs on any standard Python environment (no install/setup required)

| File                          | Description                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------- |
| `main.py`                     | Runs the core LIP algorithm and logs weighted traversal                      |
| `baseline_dfs.py`             | Runs traditional DFS for comparison                                          |
| `latent_intuition_pruning.py` | Contains all reusable algorithm logic and data structures                    |
| `test_cases.py`               | Verifies expected vs. actual traversal behavior under interaction simulation |
| `README.md`                   | Project documentation and usage guide                                        |
