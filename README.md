# vg-charts
This program is for manipulating video game stats

## [Bar Chart of Console Releases by Year (2010+)](./recent_console_releases_by_year.py)
<a href='./recent_console_releases_by_year.py'>![](./images/recent_console_releases_by_year.png)</a>


## [Pie Chart of Percentage of each Genre for Xbox One Games]
<a href='./xbox_genre_percentages.py'>![](./images/xbox_genre_percentages.png)</a>


## [Pie Chart of Percentage of Square Enix Games by Platform]
<a href='./vg_chart_generator/vg_chart_generator/__init__.py'>![](./images/square_enix_games_by_platform.png)</a>
> vg-chart-generator --filtercol Publisher --filterval "Square Enix" --groupby Platform --chart --outfile square_enix_games_by_platform.png

## [Pie Chart of Percentage of Fighting Games by Platform]
<a href='./vg_chart_generator/vg_chart_generator/__init__.py'>![](./images/fighting_by_platform.png)</a>
> vg-chart-generator --filtercol Genre --filterval Fighting --groupby Platform --chart --outfile fighting_by_platform.png