### Set Up ###

# global imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dexplorer.visualizations import Histogram

# function arguments
x_column = 'feature_0' 
x_label = 'x feature'
y_label = 'y feature'
num_bins = 15
figsize = (8, 6)

### Main Program ###

# get data
data = pd.read_csv('data.csv')

# basic histogram
density = False
histogram = Histogram(data, x_column, x_label, y_label, 
                      num_bins, 
                      density=density, 
                      figsize=figsize
                      )

histogram_basic = histogram.create_plot('Histogram, Basic')
plt.savefig(os.path.join('plots', 'histogram_basic.png'),
            bbox_inches='tight'
            )

# basic histogram colored by column
histogram_categorical = histogram.create_plot('Histogram, Categorical', 
                                              color_column='feature_11'
                                              )
plt.savefig(os.path.join('plots', 'histogram_categorical.png'),
            bbox_inches='tight'
            )

# basic density
density = True
histogram = Histogram(data, x_column, x_label, y_label, 
                      num_bins, 
                      density=density, 
                      figsize=figsize
                      )

density_basic = histogram.create_plot('Density, Basic')
plt.savefig(os.path.join('plots', 'density_basic.png'),
            bbox_inches='tight'
            )

# basic density colored by column
density_categorical = histogram.create_plot('Density, Categorical', 
                                            color_column='feature_11'
                                            )
plt.savefig(os.path.join('plots', 'density_categorical.png'),
            bbox_inches='tight'
            )