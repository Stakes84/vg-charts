import pandas as pd
import matplotlib.pyplot as plt

# Reading the file
df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
# Making a list of Xbox One index locations
console = {'XOne': []}
# Counting XBox One Titles by genre
genre = []

for i in range(len(df)):
    if df['Platform'][i] == 'XOne':
        console['XOne'].append(i)
        genre.append(df['Genre'][i])
g_count = {}

for each in set(genre):
    g_count.update({each: genre.count(each)})

g_count = {k: v for k, v in sorted(g_count.items(), key=lambda item: item[1])}


def make_autopct(values):
    def my_autopct(pct):
        total = sum(g_count.values())
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


# Plotting the chart... For more info on number values replace autopct with make_autopct(g_count.values())
#   or else use '%1.1f%%'
fig1, ax1 = plt.subplots()
plt.suptitle("Xbox One's percentage of titles in each Genre")
ax1.pie(g_count.values(), explode=(0.4, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0, 0), labels=g_count.keys(),
        autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
