# ***Data Analysis Module***

# Import the necessary libaries

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset using the currect path

df = pd.read_csv(r"dataset\sp500_companies.csv")

# Space to make it easier to read in the terminal
print()

#------ Convert "Marketcap" and "Revenuegrowth" to numeric for easier calculations ------

df["Marketcap"] = pd.to_numeric(df["Marketcap"])
df["Revenuegrowth"] = pd.to_numeric(df["Revenuegrowth"])

# Drop rows with missing values in key columns

df = df.dropna(subset=["Marketcap", "Revenuegrowth"])

#------ Question 1: Which company has the highest revenue growth rate? ------

top_growth_company = df.loc[df["Revenuegrowth"].idxmax(), ["Shortname", "Revenuegrowth"]]

# Print the statement

print(f" The company with the highest revenue growth rate is --{top_growth_company['Shortname']}-- with a growth rate of {top_growth_company['Revenuegrowth']:.2%}! ")
print()

#------ Question 2: Which sector has the highest average market capitalization? ------

sector_avg_marketcap = df.groupby("Sector")["Marketcap"].mean().sort_values(ascending=False)
top_sector = sector_avg_marketcap.idxmax()
top_sector_avg = sector_avg_marketcap.max()

# Print the statement

print(f" The sector with the highest average market capitalization is --{top_sector}-- with an average market cap of ${top_sector_avg:,.2f}! ")
print()

#------ Question 3: What are the top 5 countries with the most company headquarters? ------

country_counts = df['Country'].value_counts().head(5)

# Print the statement

print("\nTop 5 countries with the most company headquarters:")
print(country_counts)
print()

#------ Bar graph of top countries with HQ's ------ 

country_counts.plot(kind='bar', color='skyblue')
plt.title("Top 5 Countries by Company Headquarters")
plt.xlabel("Country")
plt.ylabel("Number of Companies")
plt.tight_layout()

# Add number labels above each bar
for index, value in enumerate(country_counts):
    plt.text(index, value + 1, str(value), ha='center')

# Show graph
plt.show()


#------ Question 4: What are the top 5 most common sectors and how many are there of the same kind? ------

sector_counts = df['Sector'].value_counts().head(5)

# Print the statement

print("\nTop 5 most common sectors and how many companies are in each:")
print(sector_counts)
print()

# Bar graph of top sectors

sector_counts.plot(kind='bar', color='blue')
plt.title("Top 5 Most Common Sectors")
plt.xlabel("Sector")
plt.ylabel("Number of Companies")
plt.xticks(rotation=45)
plt.tight_layout()

# Add number labels above each bar
for index, value in enumerate(sector_counts):
    plt.text(index, value + 1, str(value), ha='center')

# Show graph
plt.show()

#------ OPTIONAL Question and graph: What are the average market cap by sectors? ------

#                   Draw a chart for average market cap by sector

#           I chose to use a bar chart to show this data by using matplotlib

plt.figure(figsize=(12, 6))
sector_avg_marketcap.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Market Capitalization by Sector", fontsize=16)
plt.xlabel("Sector", fontsize=10)
plt.ylabel("Average Market Cap (Trillions)", fontsize=10)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the graph

plt.show()
