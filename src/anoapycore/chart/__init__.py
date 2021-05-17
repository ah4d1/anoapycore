# chart

import matplotlib.pyplot as __plt
import seaborn as __sns
import multipledispatch as __dispatch

@__dispatch.dispatch(object,str)
def boxplot (a_data,a_column) :
    result = __sns.boxplot(x=a_data[a_column])

@__dispatch.dispatch(object,str,str)
def boxplot (a_data,a_column_x,a_column_y) :
    result = __sns.boxplot(data=a_data,x=a_column_x,y=a_column_y)
    
def histogram (a_data,a_column,a_bins='auto',a_color='#0504aa',a_alpha=0.7,a_grid_y=True) :
    __plt.hist(x=a_data[a_column],bins=a_bins,color=a_color,alpha=a_alpha)
    __plt.title(a_column)
    __plt.xlabel('Value')
    __plt.ylabel('Frequency')
    if a_grid_y == True :
        __plt.grid(axis='y',alpha=0.7)
    __plt.show()
    
def scatterplot (a_data,a_column_x,a_column_y,a_column_by="") :
    """
    Draw a scatterplot
    """
    __sns.set_theme() # apply the default theme
    if a_column_by == "" :
        loc_result = __sns.lmplot(data=a_data,x=a_column_x,y=a_column_y)
    else :
        loc_result = __sns.lmplot(data=a_data,x=a_column_x,y=a_column_y,col=a_column_by)
    result = loc_result
