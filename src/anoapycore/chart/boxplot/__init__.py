# chart.boxplot

import matplotlib.pyplot as __plt
import seaborn as __sns
import multipledispatch as __dispatch

@__dispatch.dispatch(object,str)
def show (a_data,a_column) :
    result = __sns.boxplot(x=a_data[a_column])

@__dispatch.dispatch(object,str,str)
def show (a_data,a_column_x,a_column_y) :
    result = __sns.boxplot(data=a_data,x=a_column_x,y=a_column_y)
    
