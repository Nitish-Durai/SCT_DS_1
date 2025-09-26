import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data/API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_1039409.csv"
df = pd.read_csv(file_path, skiprows=4)

year = "2024"
age_data = df[["Country Name", year]].dropna()

# Now I'm plotting histogram of age distribution (% of population aged 15–64)
plt.figure(figsize=(10,6))
sns.histplot(age_data[year], bins=20, kde=True, color="skyblue", edgecolor="black")

plt.title(f"Distribution of Population Aged 15–64 (% of Total) in {year}")
plt.xlabel("Percentage of Population (15–64 years)")
plt.ylabel("Number of Countries")
plt.show()
