import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Part 1: Quarterly Performance Analysis
# Data provided in the business case
quarterly_data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Score': [-1.61, 6.31, 8.5, 4.14]
}

df_quarterly = pd.DataFrame(quarterly_data)

# Calculate Average
average_score = df_quarterly['Score'].mean()
print(f"Calculated Average Score: {average_score}")

# Benchmark
benchmark_target = 4.5

# Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_quarterly, x='Quarter', y='Score', marker='o', label='Satisfaction Score', linewidth=2.5)
plt.axhline(y=benchmark_target, color='r', linestyle='--', label=f'Industry Target ({benchmark_target})')
plt.axhline(y=average_score, color='g', linestyle=':', label=f'2024 Average ({average_score:.2f})')

plt.title('Patient Satisfaction Score Trend - 2024')
plt.xlabel('Quarter')
plt.ylabel('Satisfaction Score')
plt.legend()
plt.grid(True)
plt.savefig('satisfaction_trend.png')
print("Visualization saved as 'satisfaction_trend.png'")

# Part 2: Qualitative Analysis from hospital_rantings.csv
# This helps understand the "Why" behind the scores (assuming the CSV reflects general sentiment)
try:
    df_reviews = pd.read_csv('hospital_rantings.csv')
    print("\n--- Qualitative Analysis ---")
    print(f"Total Reviews: {len(df_reviews)}")
    print(f"Average Rating in CSV: {df_reviews['Ratings'].mean():.2f}")

    # Keyword analysis for "Wait times" and "Service Quality"
    keywords = {
        'wait': 0,
        'time': 0,
        'staff': 0,
        'rude': 0,
        'billing': 0,
        'money': 0,
        'care': 0
    }

    for feedback in df_reviews['Feedback'].dropna():
        feedback_lower = feedback.lower()
        for key in keywords:
            if key in feedback_lower:
                keywords[key] += 1

    print("\nKeyword Frequency in Feedback:")
    for key, value in keywords.items():
        print(f"{key}: {value}")

except FileNotFoundError:
    print("hospital_rantings.csv not found.")
