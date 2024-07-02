

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'US_Accidents_Dec20_Updated.csv'
df = pd.read_csv(file_path)

# Display the first few lines of the CSV file
print(df.head())

# Analyze patterns related to road conditions, weather, and time of day
# Convert Start_Time to datetime with error handling
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')

# Extract hour of the day
df['Hour'] = df['Start_Time'].dt.hour

# Extract day of the week
df['DayOfWeek'] = df['Start_Time'].dt.day_name()

# Extract month
df['Month'] = df['Start_Time'].dt.month_name()

# Visualize accident hotspots using geographical distribution
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Start_Lng', y='Start_Lat', data=df, alpha=0.1)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Visualize contributing factors
# Road conditions
plt.figure(figsize=(10, 6))
sns.countplot(y='Weather_Condition', data=df, order=df['Weather_Condition'].value_counts().iloc[:10].index)
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.show()

# Time of day
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')
plt.show()

# Day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='DayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.show()

# Month
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=df, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Accidents by Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()

