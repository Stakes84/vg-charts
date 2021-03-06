import pandas as pd
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# Simplified aggregation using Data Frame methods
g_count = df[df['Platform'] == 'XOne'] \
  .groupby(['Genre']) \
  .size() \
  .sort_values()

# Plotting the chart:
fig1, ax1 = plt.subplots()
plt.suptitle("Xbox One's percentage of titles in each Genre")
ax1.pie(g_count.values, explode=(0.4, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0, 0), labels=g_count.keys(),
        autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
plt.savefig('images/xbox_genre_percentages.png')
