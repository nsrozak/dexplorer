### Set Up ###

# global imports
import os
import pandas as pd
import matplotlib.pyplot as plt
from dexplorer.visualizations import Heatmap

# function arguments
x_label = ''
y_label = ''
figsize = (9, 9)

### Main Program ###

# get data
data = pd.read_csv('data.csv')
data.drop(columns=['feature_9', 'feature_10', 'feature_11', 'y'], 
          inplace=True
          )
data = data.corr()

# create heatmap object
diverging = True
heatmap = Heatmap(data, x_label, y_label, 
                  diverging, 
                  figsize=figsize
                  )

# create diverging heatmap
title = 'Heatmap, Diverging'
x_ticks_labels = data.columns.tolist()
y_ticks_labels = x_ticks_labels
add_text = True

heatmap_diverging = heatmap.create_plot(title, x_ticks_labels, y_ticks_labels,
                                        add_text=add_text
                                        )
plt.savefig(os.path.join('plots', 'heatmap_diverging.png'),
            bbox_inches='tight'
            )

# create heatmap object
diverging = False
heatmap = Heatmap(data, x_label, y_label, 
                  diverging, 
                  figsize=figsize
                  )

# create sequential heatmap
title = 'Heatmap, Sequential'
x_ticks_labels = data.columns.tolist()
y_ticks_labels = x_ticks_labels
add_text = True

heatmap_diverging = heatmap.create_plot(title, x_ticks_labels, y_ticks_labels,
                                        add_text=add_text
                                        )
plt.savefig(os.path.join('plots', 'heatmap_sequential.png'),
            bbox_inches='tight'
            )