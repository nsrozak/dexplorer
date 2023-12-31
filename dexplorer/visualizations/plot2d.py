### Set Up ###

# global imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from dexplorer.visualizations.plot import Plot
from typing import Tuple, Any
from scipy.stats import gaussian_kde

### Classes ###
        
class LineChart(Plot):
    def __init__(self, data: pd.DataFrame, x_column: str, y_column: str, 
                 x_label: str, y_label: str, error_column: str=None, 
                 error_high_column: str=None, figsize: Tuple=(8, 6)):        
        # initialize super class
        super(LineChart, self).__init__(data, x_column,  
                                        x_label, y_label, 
                                        y_column=y_column,
                                        figsize=figsize
                                       )
        
        # set member variables
        self.error_column = error_column
        self.error_high_column = error_high_column
        
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

    def _add_plot_data(self, fig: Any, data: pd.DataFrame, color: str=None):
        # get color
        color = self.categorical_colors[0] if color is None else color
        
        # create plot
        x = data[self.x_column]
        y = data[self.y_column]
        plt.plot(x, y, color=color)

        # add errors
        if self.error_column != None:
            error_low, error_high = self._get_error(data)
            plt.fill_between(x, error_low, error_high, color=color, alpha=0.3)

        # return figure
        return fig
    
    def create_plot(self, title: str, color_column: str=None, x_ticks_width: int=None, 
                    y_ticks_width: int=None):
        # get plot axes
        fig = self._get_plot_axes(title, 
                                  x_ticks_width=x_ticks_width, 
                                  y_ticks_width=y_ticks_width,
                                  x_ticks_labels=None
                                  )

        # add data to the plot
        if color_column == None:
            fig = self._add_plot_data(fig, self.data, color=None)
            
        else:
           fig = self._add_categorical_plot_data(fig, color_column, self._add_plot_data)

        # return figure
        return fig
    

class Scatterplot(Plot):
    def __init__(self, data: pd.DataFrame, x_column: str, y_column: str, 
                 x_label: str, y_label: str, figsize: Tuple=(8, 6)):
        # initialize super class
        super(Scatterplot, self).__init__(data, x_column, 
                                          x_label, y_label, 
                                          y_column=y_column,
                                          figsize=figsize
                                          )
        
        # set member variables
        self.diverging_cmap = 'RdYlGn'
        self.sequential_cmap = 'YlOrRd'

    def _get_color_density(self, x: pd.Series, y: pd.Series):
        xy = np.vstack([x,y])
        z = gaussian_kde(xy)(xy)
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]
        return x, y, z

    def _add_plot_data(self, fig: Any, data: pd.DataFrame, color: Any=None, 
                       diverging: bool=False, norm: mcolors.TwoSlopeNorm=None):
        # get color
        color = self.categorical_colors[0] if color is None else color
        # get color map
        cmap = self.diverging_cmap if diverging == True else self.sequential_cmap

        # create plot
        x = data[self.x_column]
        y = data[self.y_column]
        plt.scatter(x, y, c=color, cmap=cmap, norm=norm)

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
    
    def _add_continuous_plot_data(self, fig: Any, color_column: str, color_type: str):
        # get coloring
        color = self.data[color_column]

        if color_type == 'diverging':
            diverging = True
            norm = mcolors.TwoSlopeNorm(vmin=color.min(), vmax=color.max(), vcenter=0)
        else:
            diverging = False
            norm = None

        # add plot data
        fig = self._add_plot_data(fig, self.data, 
                                  color=color, 
                                  diverging=diverging, 
                                  norm=norm
                                 )

        # return figure
        return fig
    
    def create_plot(self, title: str, color_type: str='categorical', color_column: str=None, 
                    x_ticks_width: int=None, y_ticks_width: int=None):

        # get plot axes
        fig = self._get_plot_axes(title, 
                                  x_ticks_width=x_ticks_width, 
                                  y_ticks_width=y_ticks_width,
                                  x_ticks_labels=None
                                  )

        # add data to the plot
        if (color_type == 'categorical') and (color_column == None):
            fig = self._add_plot_data(fig, self.data, color=None)
            
        elif color_type == 'categorical':
           fig = self._add_categorical_plot_data(fig, color_column, self._add_plot_data)

        elif color_type == 'density':
            fig = self._add_density_plot_data(fig)

        elif (color_type == 'diverging') or (color_type == 'sequential'):
            fig = self._add_continuous_plot_data(fig, color_column, color_type)

        # return figure
        return fig
    