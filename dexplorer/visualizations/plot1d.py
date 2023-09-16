### Set Up ###

# global imports
import pandas as pd
import matplotlib.pyplot as plt

from dexplorer.visualizations.plot import Plot
from typing import Tuple, Any
from scipy.stats import gaussian_kde

### Classes ###

class Histogram(Plot):
    def __init__(self, data: pd.DataFrame, x_column: str, x_label: str, y_label: str, 
                 num_bins:int, density: bool=False, figsize: Tuple=(8, 6)):
        # initialize super class
        super(Histogram, self).__init__(data, x_column, 
                                        x_label, y_label, 
                                        y_column=None,
                                        figsize=figsize
                                        )
        
        # set member variables
        self.num_bins = num_bins
        self.density = density
        self.alpha = 0.4 if self.density == True else 1

    def _get_distribution_density(self, x: pd.Series):
        density = gaussian_kde(x)
        density.covariance_factor = lambda : .25
        density._compute_covariance()
        return density

    def _add_plot_data(self, fig: Any, data: pd.DataFrame, color: str=None):
        # create plot
        x = data[self.x_column]
        plt.hist(x, bins=self.num_bins, color=color, density=self.density, alpha=self.alpha)

        # add density
        if self.density == True:
            density = self._get_distribution_density(x)
            plt.plot(x, density(x), color=color)

        # return figure
        return fig

    def create_plot(self, title: str, color_column: str=None, 
                    x_ticks_width: int=None, y_ticks_width: int=None):
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
    