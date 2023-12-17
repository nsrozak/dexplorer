### Set Up ###

# global imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from typing import Tuple, Any

### Classes ###

class Heatmap():
    def __init__(self, data: pd.DataFrame, x_label: str, y_label: str, diverging: bool=False, 
                 figsize: Tuple=(8, 6)):
        # set member variables
        self.data = data
        self.x_label = x_label
        self.y_label = y_label
        self.figsize = figsize

        # set color scheme
        if diverging == True:
            self.cmap = 'RdYlGn'
            self.norm = mcolors.TwoSlopeNorm(vmin=self.data.values.min(), 
                                             vmax=self.data.values.max(), 
                                             vcenter=0
                                            )
        
        else:
            self.cmap = 'YlOrRd'
            self.norm = None
            
    def _get_plot_axes(self, title: str, x_ticks_labels: str=None, y_ticks_labels: str=None):
        # add axes
        fig = plt.figure(figsize=self.figsize)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(title, weight='bold')

        # adjust axes labels
        if x_ticks_labels is not None:
            x = np.arange(len(x_ticks_labels))
            plt.xticks(x, x_ticks_labels, rotation=90)

        if y_ticks_labels is not None:
            y = np.arange(len(y_ticks_labels))
            plt.yticks(y, y_ticks_labels)

        # return figure
        return fig
    
    def _add_plot_data(self, fig: Any, add_text: bool=False):
        # add data
        plt.imshow(self.data, cmap=self.cmap, norm=self.norm)

        # add text to graph
        if add_text == True:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    text = plt.text(j, i, str(self.data.values[i, j])[:6],
                                    ha='center', 
                                    va='center', 
                                    fontsize=11
                                    )
                    
        # return figure
        return fig
    
    def create_plot(self, title: str, x_ticks_labels: list, y_ticks_labels: list,
                    add_text: bool=False):
        # get plot axes
        fig = self._get_plot_axes(title, 
                                  x_ticks_labels=x_ticks_labels, 
                                  y_ticks_labels=y_ticks_labels
                                  )

        # add data to the plot
        fig = self._add_plot_data(fig, add_text=add_text)

        # return figure
        return fig
    