# 🧳 Fractional Knapsack (Greedy Algorithm) in Python

This Python project implements a greedy algorithm to solve a simplified 0/1 **Knapsack problem**. It selects the most "valuable per unit volume" items to pack into a container with limited space.

## 💡 How It Works

Given a list of items with:

- A name  
- A value in dollars  
- Dimensions (height, width, depth)  

The script calculates each item's volume and chooses which items to include in the knapsack based on the highest **value-to-volume ratio**, without exceeding the user-specified capacity.

### Algorithm Type
Greedy (not guaranteed to find the absolute best solution, but efficient and fast).

---

## 📂 File Structure

├── knapsack.py # Main script with algorithm and logic ├── items.csv # Input file with item data └── README.md # Project overview and usage
---

## 📥 Input File Format (`items.csv`)

Each line should contain **5 comma-separated values** in the following order:


Example:


*Volume is calculated as `height × width × depth`.*

---

## ▶️ How to Run

1. Clone this repository or download the files.
2. Make sure you have Python installed.
3. Open a terminal and run the script:

```bash
python knapsack.py
Enter maximum volume (in cubic inches): 300

The suggested items are: 1 Watch, 2 Books with a total value of $400.
There were 15 cubic inches left unused.

Let me know if you want a version with a table, screenshots, or setup instructions for a specific platform!
