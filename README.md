# 📈 Simple Linear Regression in Python

This is a beginner-friendly Python project that demonstrates how to implement a simple **Linear Regression** model using the **slope and intercept formula** (no libraries like scikit-learn). The model is then visualized using **Matplotlib**.

## 🔍 What It Does

- Calculates the **best-fit line** for a set of data points using:
  - **Slope (m)** formula:  
    \[
    m = (n * Σ(xy) - Σx * Σy) / (n * Σ(x²) - (Σx)²)
    \]
  - **Intercept (b)** formula:  
    \[
    b = (Σy - m * Σx) / n
    \]
- Uses these to define the linear equation `y = mx + b`
- Plots:
  - Original data points
  - The regression line

## 🧠 Concepts Used

- Basic statistics (mean, sum)
- Python lists and loops
- Data visualization with `matplotlib`

## 📦 Requirements

- Python 3.x
- Matplotlib

Install dependencies with:

```bash
pip install matplotlib
