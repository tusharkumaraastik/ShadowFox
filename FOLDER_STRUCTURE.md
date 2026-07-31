# Recommended GitHub Repository Folder Structure

Suggested layout for submitting this task as a GitHub repository:

```
shadowfox-matplotlib-seaborn-guide/
│
├── README.md
├── SUBMISSION_CHECKLIST.md
├── requirements.txt
├── .gitignore
│
├── report/
│   └── ShadowFox_Matplotlib_Seaborn_Report.docx
│
├── notebooks/
│   └── 01_matplotlib_seaborn_guide.ipynb
│
├── src/
│   └── visualization_guide.py
│
└── images/
    ├── mpl_line.png
    ├── mpl_scatter.png
    ├── mpl_bar.png
    ├── mpl_histogram.png
    ├── mpl_pie.png
    ├── mpl_box.png
    ├── mpl_violin.png
    ├── mpl_heatmap.png
    ├── mpl_countplot.png
    ├── mpl_pairplot.png
    ├── mpl_kde.png
    ├── sns_line.png
    ├── sns_scatter.png
    ├── sns_bar.png
    ├── sns_histogram.png
    ├── sns_pie.png
    ├── sns_box.png
    ├── sns_violin.png
    ├── sns_heatmap.png
    ├── sns_countplot.png
    ├── sns_pairplot.png
    └── sns_kde.png
```

## Folder Purpose

| Folder | Purpose |
|---|---|
| `report/` | Contains the main ~38-page Word documentation report. |
| `notebooks/` | Contains the interactive Jupyter Notebook version of all 22 charts. |
| `src/` | Contains the standalone, importable/runnable Python script. |
| `images/` | Contains pre-rendered PNG output for every chart, useful for embedding in the README or GitHub preview without re-running code. |

## Suggested `.gitignore`

```
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
venv/
output_images/
```

(`output_images/` is excluded because it is regenerated automatically by
`src/visualization_guide.py`; the curated, final copies live in `images/`.)
