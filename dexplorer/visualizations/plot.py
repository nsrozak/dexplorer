### Set Up ###

# gloabl imports 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, Any, Optional

### Classes ###

class Plot():
    def __init__(self, data: pd.DataFrame, x_column: str, x_label: str, y_label: str, 
                 y_column: Optional[str]=None, figsize: Tuple=(8, 6)):
        # set member variables
        self.data = data
        self.x_column = x_column
        self.y_column = y_column
        self.x_label = x_label
        self.y_label = y_label
        self.figsize = figsize

        # get data min and max
        self.x_min = self.data[self.x_column].min()
        self.x_max = self.data[self.x_column].max()
        self.y_min = self.data[self.y_column].min() if self.y_column != None else None
        self.y_max = self.data[self.y_column].max() if self.y_column != None else None

        # predefined member variables
        self.categorical_colors = ['lightskyblue', 'orange', 'forestgreen', 
                                   'gold', 'orangered', 'royalblue',
                                   'navajowhite', 'yellowgreen'
                                   ]

    def _get_plot_axes(self, title: str, x_ticks_width: int=None, y_ticks_width: int=None,
                       x_ticks_labels: str=None):
        # add axes
        fig = plt.figure(figsize=self.figsize)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(title, weight='bold')

        # adjust axes scales
        if x_ticks_width != None:
            plt.xticks([i for i in range(self.x_min, self.x_max + x_ticks_width, x_ticks_width)])
        if y_ticks_width != None:
            plt.yticks([i for i in range(self.y_min, self.y_max + y_ticks_width, y_ticks_width)])

        # adjust axes labels
        if x_ticks_labels is not None:
            x = np.arange(len(x_ticks_labels))
            plt.xticks(x, x_ticks_labels, rotation='90')

        # return figure
        return fig

    def _add_categorical_plot_data(self, fig: Any, color_column: str, _add_plot_data: Any):
        # add legend
        categories = self.data[color_column].unique()

        for i, category in enumerate(categories):
            # add data to the figure
            color = self.categorical_colors[i]
            data_category = self.data[self.data[color_column] == category].copy()
            fig = _add_plot_data(fig, data_category, color=color)

        # add legend
        plt.legend(categories, bbox_to_anchor=(1.01, 1), loc='upper left', ncol=1)

        # return figure
        return fig