### Set Up ###

# global imports
import os
import pandas as pd
import matplotlib.pyplot as plt
from dexplorer.visualizations import Scatterplot

# function arguments
x_column = 'feature_0'
y_column = 'feature_1'
x_label = 'x feature'
y_label = 'y_feature'
figsize = (8, 6)

### Main Program ###

# get data
data = pd.read_csv('data.csv')

# create scatterplot object
scatterplot = Scatterplot(data, x_column, y_column, 
                          x_label, y_label, 
                          figsize=figsize
                          )

# create basic scatterplot
scatterplot_basic = scatterplot.create_plot('Scatterplot, Basic')
plt.savefig(os.path.join('plots', 'scatterplot_basic.png'),
            bbox_inches='tight'
            )

# create categorical scatterplot
scatterplot_categorical = scatterplot.create_plot('Scatterplot, Categorical',
                                                  color_type='categorical', 
                                                  color_column='feature_11'
                                                  )
plt.savefig(os.path.join('plots', 'scatterplot_categorical.png'),
            bbox_inches='tight'
            )

# create density scatterplot
scatterplot_density = scatterplot.create_plot('Scatterplot, Density',
                                              color_type='density'
                                              )
plt.savefig(os.path.join('plots', 'scatterplot_density.png'),
            bbox_inches='tight'
            )

print(data)

print(data['feature_9'].unique())
