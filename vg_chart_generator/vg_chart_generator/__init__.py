import pandas as pd
import matplotlib.pyplot as plt
import argparse
import pkg_resources


class VgChartGenerator():

    # the init method is the constructor for an instance
    def __init__(self):
        self.df = pd.read_csv(
            pkg_resources.resource_filename('vg_chart_generator', 'Video_Games_Sales_as_at_22_Dec_2016.csv'))

    def columns(self):
        return self.df.columns.to_list()

    def values(self, column):
        return sorted([str(v) for v in self.df[column].unique()], key=str.casefold)

    # Return aggregated data frame filtered to one platform and grouped
    def aggregate_data(self, filtercol, filterval, groupby):
        return self.df[self.df[filtercol] == filterval] \
            .groupby([groupby]) \
            .size() \
            .sort_values()

    # Generate the plot and write it out
    def generate_plot(self, aggregate, title, filename):
        plt.suptitle(title)
        explode = (0.4, 0.3, 0.2) + tuple([0] * (len(aggregate.values) - 3))
        plt.pie(aggregate.values,
                explode=explode,
                labels=aggregate.keys(),
                autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.axis('equal')
        # Save the graph as an image
        plt.savefig(filename)


def main(args=None):
    parser = argparse.ArgumentParser(description='Create Video Game Charts')
    parser.add_argument('--columns', help='List the available columns', action='store_true')
    parser.add_argument('--filtercol', help='The column to use for filtering')
    parser.add_argument('--filterval', help='The value of filtercol to use for filtering')
    parser.add_argument('--values', help='List the values for provided filter column', action='store_true')
    parser.add_argument('--groupby', help='The column to use for grouping the filtered data')
    parser.add_argument('--chart', help='Save the filtered and grouped data as a chart', action='store_true')
    parser.add_argument('--outfile', help='The output file name for the generated chart')
    args = parser.parse_args(args)
    generator = VgChartGenerator()
    if args.columns:
        print('\n'.join(generator.columns()))
    elif args.filtercol:
        if args.values:
            print('\n'.join(generator.values(args.filtercol)))
        elif args.filterval:
            aggregate = generator.aggregate_data(args.filtercol, args.filterval, args.groupby)
            if args.chart:
                filename = args.outfile if args.outfile else '%s_%s.png' % (args.filterval, args.groupby)
                title = "%s's percentage of titles in each %s" % (args.filterval, args.groupby)
                generator.generate_plot(aggregate, title, filename)
            else:
                print(aggregate)


if __name__ == '__main__':
    main()
