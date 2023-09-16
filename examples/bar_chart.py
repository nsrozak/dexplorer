### Set Up ###

# global imports
import os
import pandas as pd
import matplotlib.pyplot as plt
from dexplorer.visualizations import BarChart

# function arguments
x_column = 'feature_2' 
x_label = ''
y_label = 'Sum'
labels_column = 'feature_11'
figsize = (8, 6)

### Main Program ###

# get data
data = pd.read_csv('data.csv')

# basic bar chart
basic_data = data.groupby([labels_column])\
    .agg({x_column: 'sum'})\
    .reset_index()\
    .sort_values(by=x_column)
labels = basic_data[labels_column].tolist()

width = 0.8
bar_chart = BarChart(basic_data, x_column, 
                     labels_column, labels, 
                     x_label, y_label, 
                     width, 
                     figsize=figsize
                    )

bar_chart_basic = bar_chart.create_plot('Bar Chart, Basic')
plt.savefig(os.path.join('plots', 'bar_chart_basic.png'),
            bbox_inches='tight'
            )

# basic histogram colored by column
categorical_data = data.groupby([labels_column, 'feature_9'])\
    .agg({x_column: 'sum'})\
    .reset_index()\
    .sort_values(by=x_column)

width = 0.3
bar_chart = BarChart(categorical_data, x_column, 
                     labels_column, labels, 
                     x_label, y_label, 
                     width, 
                     figsize=figsize
                    )
bar_chart_categorical = bar_chart.create_plot('Bar Chart, Categorical', 
                                              color_column='feature_9'
                                              )
plt.savefig(os.path.join('plots', 'bar_chart_categorical.png'),
            bbox_inches='tight'
            )
