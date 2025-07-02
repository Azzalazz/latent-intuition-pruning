# Latent Intuition Pruning

*A real-time adaptive search algorithm that dynamically prunes a decision tree based on subtle user behavior like hesitation, hover time, and interest fading.*

---

## 📌 Overview

**Latent Intuition Pruning (LIP)** is an adaptive, zero-training search algorithm that intelligently traverses decision trees based on real-time interaction signals. It leverages implicit cues like hover duration to infer interest, adjusts exploration paths accordingly, and incorporates both depth-awareness and exploration randomness. Unlike machine learning models, LIP operates without datasets or training phases, enabling instant, lightweight personalization.

---

## ✨ Key Features

- **Interaction-Driven Weights** – Simulates user interest through hover durations.
- **Temporal Interest Decay** – Older interactions fade in influence over time.
- **ε-Greedy Exploration** – Occasionally explores less likely branches to avoid local bias.
- **Depth-Aware Scoring** – Prefers closer options unless strong interest lies deeper.
- **Zero ML Dependency** – Runs without any model training or labeled data.
- **Comprehensive Logging** – Includes raw weights, effective scores, and traversal metrics.

---

## ▶️ Run the Project

```bash
python main.py           # Adaptive traversal based on hover interest
python baseline_dfs.py   # Baseline depth-first search (no prioritization)
python test_cases.py     # Validates key traversal behavior
```

---

## 🔍 Evaluation Plan

- Simulates hover times for nodes (e.g., "Explore Beaches" = 3.0s).
- Traverses the tree adaptively, logging visited nodes and computed scores.
- Includes summary metrics: total nodes visited, traversal time, decay rate, epsilon rate.
- Comparison with baseline DFS shows reduction in irrelevant exploration.

---

## 🔖 Tag for Grading

- **Final Version**: `v1.0-final`
- Fully self-contained and reproducible

---

## 🛠 Requirements

- Python 3.x  
- No external libraries required  
- Cross-platform compatible

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Simulates adaptive search with decay and random exploration |
| `latent_intuition_pruning.py` | Core algorithm with interest scoring and traversal |
| `baseline_dfs.py` | Standard DFS for behavioral comparison |
| `test_cases.py` | Verifies interest-based traversal behavior |
| `README.md` | Project description, run guide, and grading tag info |

---

Let me know if you want visuals added (e.g. using `networkx`) or to generate a demo video!
