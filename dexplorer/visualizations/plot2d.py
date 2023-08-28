### Set Up ###

# global imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, Any
from scipy.stats import gaussian_kde

### Classes ###

class Plot2D():
    def __init__(self, data: pd.DataFrame, x_column: str, y_column: str, 
                 x_label: str, y_label: str, error_column: str=None, 
                 error_high_column: str=None, figsize: Tuple=(8, 6)):
        # set member variables
        self.data = data
        self.x_column = x_column
        self.y_column = y_column
        self.x_label = x_label
        self.y_label = y_label
        self.error_column = error_column
        self.error_high_column = error_high_column
        self.figsize = figsize

        # get data min and max
        self.x_min = self.data[self.x_column].min()
        self.x_max = self.data[self.x_column].max()
        self.y_min = self.data[self.y_column].min()
        self.y_max = self.data[self.y_column].max()

        # predefined member variables
        self.categorical_colors = ['lightskyblue', 'orange', 'forestgreen', 
                                   'gold', 'orangered', 'royalblue',
                                   'navajowhite', 'yellowgreen'
                                   ]
    
    def _get_error(self, data: pd.DataFrame):
        # get errors if different widths for high and low
        if self.error_high_column != None:
            error_low = data[self.error_column]
            error_high = data[self.error_high_column]

        # get errors if same width for high and low
        else:
            error_low = data[self.y_column] - data[self.error_column]
            error_high = data[self.y_column] + data[self.error_column]

        # return errors
        return error_low, error_high
    
    def _get_color_density(self, x: pd.Series, y: pd.Series):
        xy = np.vstack([x,y])
        z = gaussian_kde(xy)(xy)
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]
        return x, y, z
        
    def _get_plot_axes(self, title: str, x_ticks_width: int=None, y_ticks_width: int=None):
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

        # return figure
        return fig

    def _add_categorical_plot_data(self, fig: Any, color_column: str, _add_plot_data: function):
        # add legend
        categories = self.data[color_column].unique()
        plt.legend(categories, bbox_to_anchor=(1.01, 1), loc='upper left', ncol=1)

        for i, category in enumerate(categories):
            # add data to the figure
            color = self.categorical_colors[i]
            data_category = self.data[self.data[color_column] == category].copy()
            fig = _add_plot_data(fig, data_category, color=color)

        # return figure
        return fig
    

class Scatterplot(Plot2D):
    def __init__(self, data: pd.DataFrame, x_column: str, y_column: str, 
                 x_label: str, y_label: str, figsize: Tuple=(8, 6)):
        # initialize super class
        super(Scatterplot, self).__init__(data, x_column, y_column, 
                                          x_label, y_label, 
                                          error_column=None, 
                                          error_high_column=None, 
                                          figsize=figsize
                                          )
        
        # set member variables
        self.diverging_cmap = 'RdYlGn'
        self.sequential_cmap = 'YlOrRd'

    def _add_plot_data(self, fig: Any, data: pd.DataFrame, color: Any=None, 
                       diverging: bool=False):
        # get color
        color = self.categorical_colors[0] if color == None else color
        # get color map
        cmap = self.diverging_cmap if diverging == True else self.sequential_cmap

        # create plot
        x = data[self.x_column]
        y = data[self.y_column]
        plt.scatter(x, y, color=color, cmap=cmap)

        # return figure
        return fig
    
    def _add_density_plot_data(self, fig: Any):
        # get coloring
        x = self.data[self.x_column]
        y = self.data[self.y_column]
        x, y, z = self._get_color_density(x, y)

        # add plot data
        fig = self._add_plot_data(fig, self.data, color=z)

        # return figure
        return fig
    
    def create_plot(self, title: str, color_type: str='categorical', color_column: str=None, 
                    x_ticks_width: int=None, y_ticks_width: int=None):

        # get plot axes
        fig = self._get_plot_axes(title, x_ticks_width=x_ticks_width, y_ticks_width=y_ticks_width)

        # add data to the plot
        if (color_type == 'categorical') and (color_column == None):
            fig = self._add_plot_data(fig, self.data, color=None)
            
        elif color_type == 'categorical':
           fig = self._add_categorical_plot_data(fig, color_column, self._add_plot_data)

        elif color_type == 'density':
            fig = self._add_density_plot_data(fig)

        elif (color_type == 'diverging') or (color_type == 'continuous'):
            to_do = True

        # return figure
        return fig
    

class LineChart(Plot2D):
    def __init__(self, data: pd.DataFrame, x_column: str, y_column: str, 
                 x_label: str, y_label: str, error_column: str=None, 
                 error_high_column: str=None, figsize: Tuple=(8, 6)):        
        # initialize super class
        super(Scatterplot, self).__init__(data, x_column, y_column, 
                                          x_label, y_label, 
                                          error_column=error_column, 
                                          error_high_column=error_high_column, 
                                          figsize=figsize
                                          )

    def _add_plot_data(self, fig: Any, data: pd.DataFrame, color: str=None):
        # create plot
        x = data[self.x_column]
        y = data[self.y_column]
        plt.plot(x, y, color=color)

        if self.error_column != None:
            error_low, error_high = self._get_error(data)
            plt.fill_between(x, error_low, error_high, color=color, alpha=0.3)

        # return figure
        return fig
    
    def create_plot(self, title: str, color_column: str=None, x_ticks_width: int=None, 
                    y_ticks_width: int=None):
        # get plot axes
        fig = self._get_plot_axes(title, x_ticks_width=x_ticks_width, y_ticks_width=y_ticks_width)

        # add data to the plot
        if color_column == None:
            fig = self._add_plot_data(fig, self.data, color=None)
            
        else:
           fig = self._add_categorical_plot_data(fig, color_column, self._add_plot_data)

        # return figure
        return fig
    