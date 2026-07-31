# ============================================
# SHADOWFOX INTERMEDIATE LEVEL PROJECT
# Delhi Air Quality Index (AQI) Analysis
# Author : Tushar Aastik
# ============================================

# ========== Import Libraries ==========

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Graph Style
plt.style.use("ggplot")
sns.set_style("whitegrid")

# ============================================
# Load Dataset
# ============================================

print("="*60)
print("Loading Dataset...")
print("="*60)

df = pd.read_csv("delhiaqi.csv")

print("\nDataset Loaded Successfully!\n")

# ============================================
# Display First Records
# ============================================

print("="*60)
print("First 5 Rows")
print("="*60)

print(df.head())

# ============================================
# Last Records
# ============================================

print("="*60)
print("Last 5 Rows")
print("="*60)

print(df.tail())

# ============================================
# Dataset Shape
# ============================================

print("="*60)
print("Dataset Shape")
print("="*60)

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

# ============================================
# Column Names
# ============================================

print("="*60)
print("Column Names")
print("="*60)

print(df.columns)

# ============================================
# Dataset Information
# ============================================

print("="*60)
print("Dataset Information")
print("="*60)

print(df.info())

# ============================================
# Missing Values
# ============================================

print("="*60)
print("Missing Values")
print("="*60)

print(df.isnull().sum())

# ============================================
# Duplicate Values
# ============================================

print("="*60)
print("Duplicate Values")
print("="*60)

print("Duplicate Rows :", df.duplicated().sum())

# ============================================
# Remove Duplicate Rows
# ============================================

df = df.drop_duplicates()

print("Duplicate rows removed successfully.")

# ============================================
# Statistical Summary
# ============================================

print("="*60)
print("Statistical Summary")
print("="*60)

print(df.describe())

# ============================================
# Convert Date Column
# ============================================

df["date"] = pd.to_datetime(df["date"])

# ============================================
# Create New Columns
# ============================================

df["Year"] = df["date"].dt.year
df["Month"] = df["date"].dt.month
df["Day"] = df["date"].dt.day
df["Hour"] = df["date"].dt.hour
df["Month_Name"] = df["date"].dt.month_name()

print("\nNew Date Columns Created Successfully.\n")

# ============================================
# Data Types
# ============================================

print("="*60)
print("Data Types")
print("="*60)

print(df.dtypes)

# ============================================
# Save Clean Dataset
# ============================================

df.to_csv("clean_delhiaqi.csv", index=False)

print("\nClean Dataset Saved Successfully.")

print("="*60)
print("PART 1 COMPLETED SUCCESSFULLY")
print("="*60)


# ======================================================
# PART 2 : EXPLORATORY DATA ANALYSIS (EDA)
# ======================================================

print("\n" + "="*60)
print("EXPLORATORY DATA ANALYSIS")
print("="*60)

# -----------------------------
# Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Fill Missing Values
# -----------------------------
df.fillna(df.mean(numeric_only=True), inplace=True)

# -----------------------------
# Statistical Summary
# -----------------------------
print("\nStatistical Summary")
print(df.describe())

# -----------------------------
# Correlation Matrix
# -----------------------------
print("\nCorrelation Matrix")
correlation = df.corr(numeric_only=True)
print(correlation)

# ======================================================
# VISUALIZATION 1
# PM2.5 Trend
# ======================================================

plt.figure(figsize=(15,6))
plt.plot(df["date"], df["pm2_5"], color="red")
plt.title("PM2.5 Trend Over Time")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ======================================================
# VISUALIZATION 2
# PM10 Trend
# ======================================================

plt.figure(figsize=(15,6))
plt.plot(df["date"], df["pm10"], color="blue")
plt.title("PM10 Trend Over Time")
plt.xlabel("Date")
plt.ylabel("PM10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ======================================================
# VISUALIZATION 3
# Histogram
# ======================================================

plt.figure(figsize=(8,5))
sns.histplot(df["pm2_5"], bins=30, kde=True)
plt.title("Distribution of PM2.5")
plt.show()

# ======================================================
# VISUALIZATION 4
# Box Plot
# ======================================================

plt.figure(figsize=(7,5))
sns.boxplot(y=df["pm2_5"])
plt.title("Boxplot of PM2.5")
plt.show()

# ======================================================
# VISUALIZATION 5
# Scatter Plot
# ======================================================

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="pm2_5", y="pm10")
plt.title("PM2.5 vs PM10")
plt.show()

# ======================================================
# VISUALIZATION 6
# Heatmap
# ======================================================

plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ======================================================
# Monthly Average PM2.5
# ======================================================

monthly_pm25 = df.groupby("Month_Name")["pm2_5"].mean()

plt.figure(figsize=(12,6))
monthly_pm25.plot(kind="bar")
plt.title("Average Monthly PM2.5")
plt.ylabel("PM2.5")
plt.show()

# ======================================================
# Average Pollutants
# ======================================================

pollutants = ["co","no","no2","o3","so2","pm2_5","pm10","nh3"]

avg = df[pollutants].mean()

plt.figure(figsize=(10,6))
avg.plot(kind="bar")
plt.title("Average Pollutant Levels")
plt.ylabel("Concentration")
plt.show()

# ======================================================
# Maximum Pollutant Values
# ======================================================

maximum = df[pollutants].max()

plt.figure(figsize=(10,6))
maximum.plot(kind="bar", color="orange")
plt.title("Maximum Pollutant Levels")
plt.ylabel("Value")
plt.show()

# ======================================================
# Minimum Pollutant Values
# ======================================================

minimum = df[pollutants].min()

plt.figure(figsize=(10,6))
minimum.plot(kind="bar", color="green")
plt.title("Minimum Pollutant Levels")
plt.ylabel("Value")
plt.show()

print("\nPART 2 COMPLETED SUCCESSFULLY")


# ======================================================
# PART 3 : ADVANCED VISUALIZATIONS
# ======================================================

print("\n" + "="*60)
print("ADVANCED DATA VISUALIZATION")
print("="*60)

# ------------------------------------------------------
# Create Season Column
# ------------------------------------------------------

def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Summer"
    elif month in [6,7,8,9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df["Season"] = df["Month"].apply(get_season)

# ======================================================
# Graph 11
# Season Wise PM2.5
# ======================================================

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="Season",y="pm2_5")
plt.title("Season Wise Average PM2.5")
plt.show()

# ======================================================
# Graph 12
# Season Wise PM10
# ======================================================

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="Season",y="pm10")
plt.title("Season Wise Average PM10")
plt.show()

# ======================================================
# Graph 13
# Violin Plot
# ======================================================

plt.figure(figsize=(8,5))
sns.violinplot(y=df["pm2_5"])
plt.title("PM2.5 Distribution")
plt.show()

# ======================================================
# Graph 14
# KDE Plot
# ======================================================

plt.figure(figsize=(8,5))
sns.kdeplot(df["pm2_5"],fill=True)
plt.title("Density Curve of PM2.5")
plt.show()

# ======================================================
# Graph 15
# Pair Plot
# ======================================================

sns.pairplot(df[["pm2_5","pm10","co","no2","so2"]])
plt.show()

# ======================================================
# Graph 16
# Average Pollutants
# ======================================================

pollutants=["co","no","no2","o3","so2","pm2_5","pm10","nh3"]

plt.figure(figsize=(12,6))

df[pollutants].mean().sort_values().plot(kind="barh")

plt.title("Average Pollutant Concentration")
plt.show()

# ======================================================
# Graph 17
# Highest Pollution Day
# ======================================================

top=df.sort_values("pm2_5",ascending=False).head(10)

plt.figure(figsize=(12,6))

sns.barplot(data=top,x="pm2_5",y="date")

plt.title("Top 10 Highest PM2.5 Days")

plt.show()

# ======================================================
# Graph 18
# Boxplot All Pollutants
# ======================================================

plt.figure(figsize=(12,6))

sns.boxplot(data=df[pollutants])

plt.xticks(rotation=45)

plt.title("Outlier Detection")

plt.show()

# ======================================================
# Graph 19
# Monthly Pollutant Trend
# ======================================================

monthly=df.groupby("Month")[pollutants].mean()

monthly.plot(figsize=(12,6))

plt.title("Monthly Pollutant Trend")

plt.show()

# ======================================================
# Graph 20
# Correlation with PM2.5
# ======================================================

corr=df.corr(numeric_only=True)

corr["pm2_5"].sort_values().plot(kind="barh",figsize=(8,6))

plt.title("Correlation with PM2.5")

plt.show()

# ======================================================
# Top Pollutant
# ======================================================

average=df[pollutants].mean()

print("\nAverage Pollutant Levels")

print(average)

highest=average.idxmax()

print("\nHighest Pollutant =",highest)

# ======================================================
# AQI Observation
# ======================================================

print("\nObservations")

print("1. Winter months generally have higher PM2.5 values.")

print("2. PM2.5 and PM10 show strong positive correlation.")

print("3. Seasonal variation affects pollution levels.")

print("4. Boxplots indicate presence of outliers.")

print("5. Heatmap shows relationships among pollutants.")

print("\nPART 3 COMPLETED SUCCESSFULLY")



# ======================================================
# PART 4 : FINAL INSIGHTS & REPORT
# ======================================================

print("\n" + "="*70)
print("FINAL ANALYSIS REPORT")
print("="*70)

# ======================================================
# Research Question 1
# ======================================================

pollutants=["co","no","no2","o3","so2","pm2_5","pm10","nh3"]

avg_pollutant=df[pollutants].mean()

print("\nResearch Question 1")
print("------------------------------")
print("Which pollutant has the highest average concentration?")

print(avg_pollutant)

print("\nHighest Pollutant : ",avg_pollutant.idxmax())
print("Average Value :",avg_pollutant.max())

# ======================================================
# Research Question 2
# ======================================================

print("\nResearch Question 2")
print("------------------------------")
print("Season Wise PM2.5")

season_pm=df.groupby("Season")["pm2_5"].mean()

print(season_pm)

# ======================================================
# Research Question 3
# ======================================================

print("\nResearch Question 3")
print("------------------------------")
print("Monthly Average PM2.5")

monthly=df.groupby("Month_Name")["pm2_5"].mean()

print(monthly)

# ======================================================
# Research Question 4
# ======================================================

print("\nResearch Question 4")
print("------------------------------")
print("Average Pollutants")

print(df[pollutants].mean())

# ======================================================
# Research Question 5
# ======================================================

print("\nResearch Question 5")
print("------------------------------")
print("Correlation of PM2.5")

print(df.corr(numeric_only=True)["pm2_5"])

# ======================================================
# Save Final Dataset
# ======================================================

df.to_csv("Final_Delhi_AQI.csv",index=False)

print("\nFinal Dataset Saved Successfully")

# ======================================================
# Save Correlation Matrix
# ======================================================

corr=df.corr(numeric_only=True)

corr.to_csv("Correlation_Matrix.csv")

print("Correlation Matrix Saved Successfully")

# ======================================================
# Final Summary
# ======================================================

print("\n")
print("="*70)
print("PROJECT SUMMARY")
print("="*70)

print("""
1. Dataset Loaded Successfully

2. Missing Values Checked

3. Duplicate Rows Removed

4. Date Converted

5. New Features Created

6. Statistical Analysis Completed

7. Correlation Analysis Completed

8. More than 20 Graphs Generated

9. Seasonal Analysis Completed

10. Pollutant Comparison Completed

11. Outlier Detection Completed

12. Monthly Trend Analysis Completed

13. Final Insights Generated

""")

# ======================================================
# Conclusion
# ======================================================

print("="*70)
print("CONCLUSION")
print("="*70)

print("""

• PM2.5 is one of the major contributors to poor air quality.

• PM10 also contributes significantly.

• Winter season generally records higher pollution.

• Strong positive correlation exists between PM2.5 and PM10.

• Air pollution varies across months.

• Seasonal weather conditions influence AQI.

• Continuous monitoring is essential.

""")

# ======================================================
# Recommendations
# ======================================================

print("="*70)
print("RECOMMENDATIONS")
print("="*70)

recommendations=[

"Increase public transport usage.",

"Reduce industrial emissions.",

"Control construction dust.",

"Promote electric vehicles.",

"Increase plantation.",

"Monitor AQI regularly.",

"Create public awareness programs.",

"Strengthen pollution control policies."

]

for i,r in enumerate(recommendations,1):

    print(f"{i}. {r}")

# ======================================================
# THANK YOU
# ======================================================

print("\n")
print("="*70)
print("SHADOWFOX INTERMEDIATE LEVEL PROJECT COMPLETED")
print("="*70)

print("Author : Tushar Aastik")

print("Project : Delhi AQI Analysis")

print("Status : Successfully Completed")

print("="*70)