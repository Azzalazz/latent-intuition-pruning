# Latent Intuition Pruning

*A real-time adaptive algorithm that prunes decision trees based on subtle user behaviors like hesitation, hover time, and interest fading.*

---

## 🔍 Problem Statement & Use Case

Most applications only respond to explicit user choices (like clicks), but subtle behaviors like pausing, hovering, or returning to certain content often reveal more about a user’s interests. This project introduces a novel adaptive search algorithm—**Latent Intuition Pruning**—that uses real-time behavioral cues to explore a decision tree more intelligently. It’s especially useful in systems like interactive content recommenders, exploratory design tools, or UX prototypes that offer many options but want to minimize irrelevant choices.

---

## ⚙️ Algorithm Overview

**Latent Intuition Pruning (LIP)** dynamically adapts tree traversal based on:
- **Hover/interest duration** (user hesitation or attention)
- **Temporal decay** (older interest fades over time)
- **Depth-awareness** (accounts for cognitive cost of deep branches)
- **ε-Greedy exploration** (adds occasional randomness for discovery)

This is done without any machine learning models or training phase, making it lightweight, interpretable, and testable in real-time.

---

## 💡 Key Features

- ✅ **User-Driven Scoring** – Uses simulated hover data to score nodes
- ⏳ **Interest Decay** – Scores gradually fade as time passes
- 🎲 **ε-Greedy Randomness** – Occasionally explores less likely branches
- 📉 **Depth-Aware Scoring** – Penalizes deep paths without strong interest
- 🧠 **No ML Dependency** – All adaptation is rule-based and transparent

---

## 🧪 Evaluation & Test Plan

We simulate a user interacting with a decision tree:
- Hover times are assigned to various nodes
- Adaptive pruning runs from the root and logs the visited nodes
- Compared against a **baseline DFS** to show improved prioritization

### ✔️ Example Test Cases
- **Test 1**: User hovers on “Explore Beaches” and “Surfing Spots” → LIP prioritizes those
- **Test 2**: Tie between two interests → LIP explores both, adaptively
- **Test 3**: Minimal interest given → LIP still visits all paths like DFS

See `test_cases.py` for details. All test cases pass and output expected paths.

---

## 📈 Runtime & Space Complexity

- **Traversal Time**: O(n log d), where d = average branching factor
- **Per-node Work**: O(log d) due to sorting children
- **Memory**: O(n) for tracking visited nodes and scores

Profiling with `time` module and logging included in `main.py`.

---

## 📂 Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Runs full simulation with pruning, scoring, and logs |
| `latent_intuition_pruning.py` | Core algorithm: scoring, decay, and tree logic |
| `baseline_dfs.py` | Standard DFS for performance comparison |
| `test_cases.py` | Contains 3+ unit tests validating pruning behavior |
| `README.md` | This document |

---

## ▶️ Run Instructions

```bash
python main.py           # Runs the adaptive pruning system
python baseline_dfs.py   # Runs baseline DFS (no heuristics)
python test_cases.py     # Executes unit tests (3+ cases)
```

No external dependencies required (just Python 3.x).

---

## 🔖 Git Tag for Grading

Final submission version is tagged as:  
**`v1.0-final`**  
[Link to Release](https://github.com/YOUR_USERNAME/YOUR_REPO/releases/tag/v1.0-final)

---

## 🎥 Optional Demo Video (Coming Soon)

I will include a brief 1–3 min screencast demonstrating:
- The traversal paths with and without pruning
- Hover-based adaptation in real time
- Comparison results in logs

Link will be added here upon upload.

