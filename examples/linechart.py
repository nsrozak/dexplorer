### Set Up ###

# global imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dexplorer.visualizations import LineChart

# function arguments
x_column = 'time' 
y_column = 'feature_5' 
x_label = 'x feature'
y_label = 'y feature'
figsize = (8, 6)

### Main Program ###

# get data
data = pd.read_csv('data.csv')
data = data.head(50)
data['feature_1'] = (-4 * data['feature_1']) + data['feature_5']
data['feature_2'] = 4 * data['feature_2']
data['feature_8'] = (4 * data['feature_8']) + data['feature_5']
data['time'] = np.arange(data.shape[0])

# basic line chart
error_column = None 
error_high_column = None

line_chart = LineChart(data, x_column, y_column, x_label, y_label, 
                       error_column=error_column, 
                       error_high_column=error_high_column, 
                       figsize=figsize
                       )

line_chart_basic = line_chart.create_plot('Line Chart, Basic')
plt.savefig(os.path.join('plots', 'line_chart_basic.png'),
            bbox_inches='tight'
            )

# basic line chart colored by column
line_chart_basic = line_chart.create_plot('Line Chart, Basic', 
                                          color_column='feature_11'
                                          )
plt.savefig(os.path.join('plots', 'line_chart_categorical.png'),
            bbox_inches='tight'
            )

# centered error line chart
error_column = 'feature_2'

line_chart = LineChart(data, x_column, y_column, x_label, y_label, 
                       error_column=error_column, 
                       error_high_column=error_high_column, 
                       figsize=figsize
                       )

line_chart_centered_error = line_chart.create_plot('Line Chart, Centered Error')
plt.savefig(os.path.join('plots', 'line_chart_centered_error.png'),
            bbox_inches='tight'
            )

# off-centered error line chart
error_column = 'feature_1'
error_high_column = 'feature_8'

line_chart = LineChart(data, x_column, y_column, x_label, y_label, 
                       error_column=error_column, 
                       error_high_column=error_high_column, 
                       figsize=figsize
                       )

line_chart_offcentered_error = line_chart.create_plot('Line Chart, Off-Centered Error')
plt.savefig(os.path.join('plots', 'line_chart_offcentered_error.png'),
            bbox_inches='tight'
            )