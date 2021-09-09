import pandas as pd                 
df = pd.read_csv("Week8Project/ClassData.csv")   
df.index += 1                       

from bokeh.plotting import figure, show      
from bokeh.models import ColumnDataSource                        

from bokeh.transform import factor_cmap                

colors = ["#78b98f", "#016876", "#3fc6f8",
          "#691b9e", "#bc74d8", "#514e72",
          "#ccbff5", "#9f0b64", "#f24bc7",
          "#3f16f9", "#2282f5", "#11e38c"]

grades = (df['Grade']).apply(str)                                
totals = df["Male"]                                          
source = ColumnDataSource(data=dict(grades=grades, totals=totals)) 

visual_colored = figure(title="Total Male Enrollment by Grade", x_range=grades, y_range=(0,25), 
                       x_axis_label = "Grade", y_axis_label = "Total Male Enrollment", 
                       plot_height=300, plot_width=900)

visual_colored.vbar(x='grades', top='totals', width=0.8, legend_field='grades', source=source, 
                    fill_color = factor_cmap('grades', palette=colors, factors=grades,nan_color='blue'))

visual_colored.xgrid.grid_line_color = None
visual_colored.legend.orientation = "horizontal"
visual_colored.legend.location = "top_right"

show(visual_colored)