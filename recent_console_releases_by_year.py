import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load the Video Game Sales data as a DataFrame
stats = 'Video_Games_Sales_as_at_22_Dec_2016.csv'
df = pd.read_csv(stats)

# Make a list of consoles we care about
consoles = [
  'PS2',
  'PS3',
  'PS4',
  'Wii',
  'WiiU',
  'X360',
  'XOne'
]

# Chain a series of methods on the DataFrame
# Each method can have its own line because of the continuation character: \
# - Filter the DataFrame to just the consoles
# - Query for just the games released on or after 2010
# - Group first by year, then platform
# - Get the size of each group
# - "Unstack" the group sizes into separate values (for plotting)
# - Plot the values as a stacked bar chart
df[df['Platform'].isin(consoles)] \
  .query('Year_of_Release>=2010') \
  .groupby(['Year_of_Release', 'Platform']) \
  .size() \
  .unstack() \
  .plot(kind='bar', stacked=True)

# Show the graph
plt.show()