# ShadowFox Data Science Internship — Beginner Level Task
## Matplotlib & Seaborn: A Complete Python Data Visualization Guide

# ShadowFox Data Science Internship

## Student Details
- Name: Tushar Kumar Aastik
- University: Central University of Jammu
- Course: B.Tech (Cyber Security)

## Internship Details
- Company: ShadowFox
- Domain: Data Science
- Duration: 1 July 2026 – 31 July 2026

This repository contains the completed **Beginner Level Task** for the
ShadowFox Data Science Internship: a comprehensive documentation guide
comparing **Matplotlib** and **Seaborn**, the two most widely used Python
data visualization libraries.

---

## 📌 Project Overview

The task required producing:

1. A professional, ~30–40 page documentation report covering both libraries
   (overview, features, advantages/disadvantages, installation, use cases).
2. Eleven chart types implemented in **both** libraries (22 charts total),
   each with a description, "when to use" guidance, complete runnable
   Python code, and an explanation of the expected output.
3. A professional comparison table between the two libraries.
4. A conclusion and reference list (based on official documentation only).
5. A companion Jupyter Notebook, a standalone Python script, this README,
   a defined folder structure, and a final submission checklist.

---

## 📂 Repository Contents

| File / Folder | Description |
|---|---|
| `ShadowFox_Matplotlib_Seaborn_Report.docx` | The full ~38-page documentation report (Word format). |
| `notebooks/01_matplotlib_seaborn_guide.ipynb` | Jupyter Notebook with all 22 charts, fully executable. |
| `src/visualization_guide.py` | Standalone Python script that regenerates all 22 chart images. |
| `images/` | Pre-generated PNG output of all 22 charts (11 per library). |
| `README.md` | This file. |
| `SUBMISSION_CHECKLIST.md` | Final checklist used to verify task completeness before submission. |
| `requirements.txt` | Python dependencies needed to run the notebook/script. |

See **Folder Structure** below for the full recommended repository layout.

---

## 📊 Chart Types Covered (per library)

1. Line Plot
2. Scatter Plot
3. Bar Chart
4. Histogram
5. Pie Chart
6. Box Plot
7. Violin Plot
8. Heatmap
9. Count Plot
10. Pair Plot
11. KDE Plot

Each chart is implemented once in **Matplotlib** and once in **Seaborn**,
totalling **22 charts**, so the two approaches can be directly compared.

---

## 🛠️ Tech Stack

- Python 3.10+
- [Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Seaborn](https://seaborn.pydata.org/tutorial/introduction.html)
- pandas, NumPy, SciPy (for KDE computation)

---

## ▶️ How to Run

### Option 1 — Run the Python script

```bash
pip install -r requirements.txt
python src/visualization_guide.py
```

This regenerates all 22 chart images into `output_images/`.

### Option 2 — Run the Jupyter Notebook

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_matplotlib_seaborn_guide.ipynb
```

Run all cells (`Kernel > Restart & Run All`) to reproduce every chart
inline, with explanatory markdown alongside each one.

> **Note on datasets:** The official Seaborn tutorial usually loads sample
> data via `sns.load_dataset('tips')`, which requires internet access. To
> keep this project fully reproducible offline, the script/notebook build
> statistically similar `tips`, `iris`, and `flights` DataFrames locally.
> If you have internet access, you may swap in `sns.load_dataset(...)`
> instead — the plotting code itself is unchanged either way.

---

## 📈 Comparison Summary

| Criteria | Matplotlib | Seaborn |
|---|---|---|
| Ease of Use | Lower-level, more code | Higher-level, concise |
| Customization | Extremely high | Good, but deep tweaks may need Matplotlib |
| Performance | Fast for basic charts | Slightly slower on very large datasets |
| Interactivity | Limited natively | Same limitation (renders through Matplotlib) |
| Large Datasets | Efficient with NumPy arrays | Can slow down with built-in statistical estimation |
| Learning Curve | Steeper | Gentler, good defaults |
| Best Use Cases | Custom, publication-quality figures | Fast statistical EDA |

Full details, advantages/disadvantages, and installation instructions are
in the main report: `ShadowFox_Matplotlib_Seaborn_Report.docx`.

---

## 📚 References

- Matplotlib Development Team, *Quick Start Guide*:
  https://matplotlib.org/stable/users/explain/quick_start.html
- Waskom, M. et al., *An Introduction to Seaborn*:
  https://seaborn.pydata.org/tutorial/introduction.html

---

## 👤 Author

ShadowFox Data Science Intern — Beginner Level Task Submission.

## 📄 License

This project is submitted for educational purposes as part of the
ShadowFox Data Science Internship program.
