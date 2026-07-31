"""
ShadowFox Data Science Internship — Beginner Level Task
=========================================================
Matplotlib & Seaborn Documentation Guide — Companion Script

This script reproduces every chart discussed in the accompanying report
(ShadowFox_Matplotlib_Seaborn_Report.docx). Running this file end-to-end
regenerates all 22 chart images (11 chart types x 2 libraries) into the
'output_images/' folder.

Author : ShadowFox Data Science Intern
Usage  : python visualization_guide.py
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

# ---------------------------------------------------------------------------
# 0. GLOBAL SETUP
# ---------------------------------------------------------------------------
OUTPUT_DIR = "output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

np.random.seed(42)
sns.set_theme(style="whitegrid")


def savefig(fig, name):
    """Save a figure into the output_images directory and close it."""
    fig.savefig(os.path.join(OUTPUT_DIR, name), dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# 1. BUILD SAMPLE DATASETS
# ---------------------------------------------------------------------------
# NOTE: The official Seaborn tutorial normally loads sample data with
# sns.load_dataset('tips') / sns.load_dataset('iris') / sns.load_dataset('flights').
# Those helpers require internet access. The code below builds statistically
# similar datasets locally so this script runs fully offline. If you have
# internet access, feel free to replace this block with sns.load_dataset(...).

def build_tips_dataset(n=244):
    days = np.random.choice(["Thur", "Fri", "Sat", "Sun"], size=n, p=[0.25, 0.08, 0.35, 0.32])
    sex = np.random.choice(["Male", "Female"], size=n)
    smoker = np.random.choice(["Yes", "No"], size=n, p=[0.38, 0.62])
    time_ = np.where(np.isin(days, ["Sat", "Sun"]), "Dinner",
                      np.random.choice(["Lunch", "Dinner"], size=n))
    total_bill = np.round(np.random.gamma(shape=5, scale=4, size=n) + 3, 2)
    tip_pct = np.random.normal(0.16, 0.05, n).clip(0.05, 0.35)
    tip = np.round(total_bill * tip_pct, 2)
    size_ = np.random.choice([1, 2, 2, 3, 4, 4, 5, 6], size=n)

    return pd.DataFrame({
        "total_bill": total_bill, "tip": tip, "sex": sex, "smoker": smoker,
        "day": pd.Categorical(days, categories=["Thur", "Fri", "Sat", "Sun"], ordered=True),
        "time": time_, "size": size_,
    })


def build_iris_dataset():
    species = np.repeat(["setosa", "versicolor", "virginica"], 50)
    sepal_length = np.concatenate([
        np.random.normal(5.0, 0.35, 50), np.random.normal(5.9, 0.5, 50), np.random.normal(6.6, 0.6, 50)
    ])
    sepal_width = np.concatenate([
        np.random.normal(3.4, 0.38, 50), np.random.normal(2.8, 0.3, 50), np.random.normal(3.0, 0.3, 50)
    ])
    petal_length = np.concatenate([
        np.random.normal(1.5, 0.17, 50), np.random.normal(4.3, 0.47, 50), np.random.normal(5.6, 0.55, 50)
    ])
    return pd.DataFrame({
        "sepal_length": sepal_length, "sepal_width": sepal_width,
        "petal_length": petal_length, "species": species,
    })


def build_flights_dataset():
    years = list(range(1949, 1961))
    return pd.DataFrame({
        "year": np.repeat(years, 12),
        "month": np.tile(range(1, 13), len(years)),
        "passengers": (np.linspace(112, 622, len(years) * 12) +
                        np.random.normal(0, 15, len(years) * 12)).round().astype(int),
    })


tips = build_tips_dataset()
iris = build_iris_dataset()
flights = build_flights_dataset()


# ===========================================================================
# 2. MATPLOTLIB CHART GALLERY
# ===========================================================================

def matplotlib_line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, color="#1f77b4", linewidth=2, label="sin(x) + noise")
    ax.set_title("Matplotlib Line Plot")
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.legend()
    savefig(fig, "mpl_line.png")


def matplotlib_scatter_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sc = ax.scatter(tips["total_bill"], tips["tip"], c=tips["size"], cmap="viridis", alpha=0.8)
    ax.set_title("Matplotlib Scatter Plot")
    ax.set_xlabel("Total Bill ($)")
    ax.set_ylabel("Tip ($)")
    fig.colorbar(sc, label="Party Size")
    savefig(fig, "mpl_scatter.png")


def matplotlib_bar_chart():
    day_avg = tips.groupby("day", observed=True)["total_bill"].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(day_avg.index, day_avg.values, color="#4c72b0")
    ax.set_title("Matplotlib Bar Chart")
    ax.set_xlabel("Day")
    ax.set_ylabel("Average Total Bill ($)")
    savefig(fig, "mpl_bar.png")


def matplotlib_histogram():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(tips["total_bill"], bins=20, color="#55a868", edgecolor="black")
    ax.set_title("Matplotlib Histogram")
    ax.set_xlabel("Total Bill ($)")
    ax.set_ylabel("Frequency")
    savefig(fig, "mpl_histogram.png")


def matplotlib_pie_chart():
    day_counts = tips["day"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(day_counts.values, labels=day_counts.index, autopct="%1.1f%%", startangle=90,
           colors=sns.color_palette("pastel"))
    ax.set_title("Matplotlib Pie Chart")
    savefig(fig, "mpl_pie.png")


def matplotlib_box_plot():
    categories = list(tips["day"].cat.categories)
    data_by_day = [tips.loc[tips["day"] == d, "total_bill"] for d in categories]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.boxplot(data_by_day, tick_labels=categories)
    ax.set_title("Matplotlib Box Plot")
    ax.set_xlabel("Day")
    ax.set_ylabel("Total Bill ($)")
    savefig(fig, "mpl_box.png")


def matplotlib_violin_plot():
    categories = list(tips["day"].cat.categories)
    data_by_day = [tips.loc[tips["day"] == d, "total_bill"] for d in categories]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.violinplot(data_by_day, showmedians=True)
    ax.set_xticks(range(1, len(categories) + 1))
    ax.set_xticklabels(categories)
    ax.set_title("Matplotlib Violin Plot")
    ax.set_xlabel("Day")
    ax.set_ylabel("Total Bill ($)")
    savefig(fig, "mpl_violin.png")


def matplotlib_heatmap():
    corr = tips[["total_bill", "tip", "size"]].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
    ax.set_title("Matplotlib Heatmap (Correlation Matrix)")
    fig.colorbar(im)
    savefig(fig, "mpl_heatmap.png")


def matplotlib_count_plot():
    counts = tips["day"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(counts.index.astype(str), counts.values, color="#c44e52")
    ax.set_title("Matplotlib 'Count Plot' (built via bar())")
    ax.set_xlabel("Day")
    ax.set_ylabel("Count")
    savefig(fig, "mpl_countplot.png")


def matplotlib_pair_plot():
    cols = ["sepal_length", "sepal_width", "petal_length"]
    species_colors = {"setosa": "#4c72b0", "versicolor": "#55a868", "virginica": "#c44e52"}
    fig, axes = plt.subplots(len(cols), len(cols), figsize=(7, 7))
    for i, ci in enumerate(cols):
        for j, cj in enumerate(cols):
            ax = axes[i, j]
            if i == j:
                for sp, color in species_colors.items():
                    ax.hist(iris.loc[iris["species"] == sp, ci], color=color, alpha=0.5, bins=10)
            else:
                for sp, color in species_colors.items():
                    subset = iris[iris["species"] == sp]
                    ax.scatter(subset[cj], subset[ci], color=color, s=10, alpha=0.7)
            if i == len(cols) - 1:
                ax.set_xlabel(cj)
            if j == 0:
                ax.set_ylabel(ci)
    fig.suptitle("Matplotlib 'Pair Plot' (manually constructed grid)")
    fig.tight_layout()
    savefig(fig, "mpl_pairplot.png")


def matplotlib_kde_plot():
    values = tips["total_bill"].values
    kde = gaussian_kde(values)
    xs = np.linspace(values.min(), values.max(), 200)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xs, kde(xs), color="#8172b2", linewidth=2)
    ax.fill_between(xs, kde(xs), alpha=0.3, color="#8172b2")
    ax.set_title("Matplotlib KDE Plot (via scipy.stats.gaussian_kde)")
    ax.set_xlabel("Total Bill ($)")
    ax.set_ylabel("Density")
    savefig(fig, "mpl_kde.png")


# ===========================================================================
# 3. SEABORN CHART GALLERY
# ===========================================================================

def seaborn_line_plot():
    avg_by_year = flights.groupby("year")["passengers"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=avg_by_year, x="year", y="passengers", marker="o", ax=ax)
    ax.set_title("Seaborn Line Plot")
    savefig(fig, "sns_line.png")


def seaborn_scatter_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="smoker", ax=ax)
    ax.set_title("Seaborn Scatter Plot")
    savefig(fig, "sns_scatter.png")


def seaborn_bar_chart():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=tips, x="day", y="total_bill", hue="sex", errorbar="sd", ax=ax)
    ax.set_title("Seaborn Bar Chart")
    savefig(fig, "sns_bar.png")


def seaborn_histogram():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(data=tips, x="total_bill", hue="time", kde=True, ax=ax)
    ax.set_title("Seaborn Histogram")
    savefig(fig, "sns_histogram.png")


def seaborn_pie_chart():
    # Seaborn has no native pie-chart function; Matplotlib's pie() is used,
    # styled with a Seaborn color palette.
    day_counts = tips["day"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(day_counts.values, labels=day_counts.index, autopct="%1.1f%%", startangle=90,
           colors=sns.color_palette("Set2"))
    ax.set_title("Pie Chart styled with a Seaborn Palette")
    savefig(fig, "sns_pie.png")


def seaborn_box_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", ax=ax)
    ax.set_title("Seaborn Box Plot")
    savefig(fig, "sns_box.png")


def seaborn_violin_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, ax=ax)
    ax.set_title("Seaborn Violin Plot")
    savefig(fig, "sns_violin.png")


def seaborn_heatmap():
    corr = tips[["total_bill", "tip", "size"]].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Seaborn Heatmap (Correlation Matrix)")
    savefig(fig, "sns_heatmap.png")


def seaborn_count_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=tips, x="day", hue="sex", ax=ax)
    ax.set_title("Seaborn Count Plot")
    savefig(fig, "sns_countplot.png")


def seaborn_pair_plot():
    g = sns.pairplot(iris, hue="species", vars=["sepal_length", "sepal_width", "petal_length"],
                      diag_kind="hist", height=2.2)
    g.fig.suptitle("Seaborn Pair Plot", y=1.02)
    g.savefig(os.path.join(OUTPUT_DIR, "sns_pairplot.png"), dpi=150, bbox_inches="tight")
    plt.close(g.fig)


def seaborn_kde_plot():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.kdeplot(data=tips, x="total_bill", hue="time", fill=True, ax=ax)
    ax.set_title("Seaborn KDE Plot")
    savefig(fig, "sns_kde.png")


# ---------------------------------------------------------------------------
# 4. MAIN — RUN THE FULL GALLERY
# ---------------------------------------------------------------------------

def main():
    matplotlib_functions = [
        matplotlib_line_plot, matplotlib_scatter_plot, matplotlib_bar_chart,
        matplotlib_histogram, matplotlib_pie_chart, matplotlib_box_plot,
        matplotlib_violin_plot, matplotlib_heatmap, matplotlib_count_plot,
        matplotlib_pair_plot, matplotlib_kde_plot,
    ]
    seaborn_functions = [
        seaborn_line_plot, seaborn_scatter_plot, seaborn_bar_chart,
        seaborn_histogram, seaborn_pie_chart, seaborn_box_plot,
        seaborn_violin_plot, seaborn_heatmap, seaborn_count_plot,
        seaborn_pair_plot, seaborn_kde_plot,
    ]

    print("Generating Matplotlib charts...")
    for fn in matplotlib_functions:
        fn()
        print(f"  - {fn.__name__} done")

    print("Generating Seaborn charts...")
    for fn in seaborn_functions:
        fn()
        print(f"  - {fn.__name__} done")

    print(f"\nAll 22 charts saved to '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    main()
