import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
df = pd.read_csv('space_missions.csv')

# Step 2: Data Cleaning
# Check for missing values
print("Missing Values Count:\n", df.isnull().sum())

# Drop rows with missing values (assuming 'date' is the only column that might have them)
df.dropna(subset=['date'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort the dataframe by date
df.sort_values(by='date', inplace=True)

# Step 3: Exploratory Data Analysis (EDA)
# Descriptive Statistics
print("\nDescriptive Statistics:\n", df.describe())

# Distribution of Dates
df['date'].dt.year.value_counts().plot(kind='bar')
plt.title('Distribution of Space Missions Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Missions')
plt.show()

# Correlation Matrix (if relevant)
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()

# Step 4: Data Visualization
# Line Plot for Number of Missions Over Years
missions_per_year = df.groupby(df['date'].dt.year).size()
missions_per_year.plot(kind='line')
plt.title('Space Missions Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Missions')
plt.show()

# Bar Plot for Mission Types (Assuming 'mission_type' is a categorical column)
mission_types = df['mission_type'].value_counts()
mission_types.plot(kind='bar')
plt.title('Distribution of Mission Types')
plt.xlabel('Mission Type')
plt.ylabel('Count')
plt.show()
