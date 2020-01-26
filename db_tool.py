import pandas as pd
import matplotlib.pyplot as plt

# I am trying to code in the filtering object we keep using.
df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')


def genre_pie(console):
    # Generating explode for pie chart readability
    explode = list()
    g_list = set()
    x = 0.5
    for each in df['Genre']:
        g_list.add(each)
        if len(explode) < len(g_list):
            explode.append("%.1f" % x)
            x -= 0.1

    explode = [float(i) for i in explode]

    for i in range(explode.index(0.0), len(explode)):
        explode[i] = 0.0
    explode.pop(-1)

    # Simplified aggregation using Data Frame methods
    g_count = df[df['Platform'] == console] \
        .groupby(['Genre']) \
        .size() \
        .sort_values()

    # Plotting the pie chart chart:
    fig1, ax1 = plt.subplots()
    plt.suptitle(f"{console}'s percentage of titles in each Genre")
    ax1.pie(g_count.values, explode=explode, labels=g_count.keys(),
            autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()

    # I can't figure out why this isn't working for me. It was basically a copy and paste.
    # A .png gets added to the folder but it's blank when I try to look at it.
    plt.savefig(f'images/{console}_genre_percentages.png')

# Now you can pass in a console to automate the pie chart.
genre_pie('X360')