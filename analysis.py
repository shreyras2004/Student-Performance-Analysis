import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student-mat.csv", header=None)

# Split columns
df = df[0].str.split(";", expand=True)

# Set column names
df.columns = df.iloc[0]

# Remove first row
df = df[1:]

# Reset index
df = df.reset_index(drop=True)

# Remove quotes from all data
df = df.replace('"', '', regex=True)

# Convert G3 and studytime to numeric
df["G3"] = pd.to_numeric(df["G3"])
df["studytime"] = pd.to_numeric(df["studytime"])

# -----------------------------
# DATA EXPLORATION
# -----------------------------

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# ANALYSIS
# -----------------------------

# Average final grade
average_grade = df["G3"].mean()

print("\nAverage Final Grade (G3):")
print(average_grade)

# Students scoring above 15
high_scorers = df[df["G3"] > 15]

print("\nStudents scoring above 15:")
print(len(high_scorers))

# Correlation
correlation = df["studytime"].corr(df["G3"])

print("\nCorrelation between study time and grades:")
print(correlation)

# Gender performance
gender_avg = df.groupby("sex")["G3"].mean()

print("\nAverage Score by Gender:")
print(gender_avg)

# -----------------------------
# VISUALIZATIONS
# -----------------------------

# Histogram
plt.figure(figsize=(8,5))

plt.hist(df["G3"], bins=10, edgecolor='black')

plt.title("Distribution of Final Grades")

plt.xlabel("Final Grade")

plt.ylabel("Number of Students")

plt.savefig("histogram.png")

plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))

sns.scatterplot(x=df["studytime"], y=df["G3"])

plt.title("Study Time vs Final Grade")

plt.xlabel("Study Time")

plt.ylabel("Final Grade")

plt.savefig("scatterplot.png")

plt.show()

# Bar Chart
plt.figure(figsize=(6,5))

sns.barplot(x=gender_avg.index, y=gender_avg.values)

plt.title("Average Score by Gender")

plt.xlabel("Gender")

plt.ylabel("Average G3 Score")

plt.savefig("barchart.png")

plt.show()
