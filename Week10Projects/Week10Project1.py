from bokeh.plotting import figure, show    # Import modules
from bokeh.io import output_notebook       
from bokeh.models import ColumnDataSource  
from bokeh.models import FactorRange
from bokeh.transform import factor_cmap

import pandas as pd                 # Tell Python we will be using the Pandas set of tools, and nickname it to pd so we can type it quicker
df = pd.read_csv("Week10Projects/ClassData.csv")   # Create a DataFrame, call it df, and set its value to the content of our CSV data
df.index += 1                       # Tells the DataFrame to start index labels at 1

grouped_df = df.groupby(['School'])  # Groups the data in dataframe by the 'School' column           
schools = {}                         # Create an empty dictionary              
for group in grouped_df.groups:      # For every group within the grouped_df (Which are the 3 schools),
    schools[group] = grouped_df.get_group(group) # get data on each group and put it into the dictionary (3 keys made up of all the data from dataframe with specific school type)             


school_names = ["Elementary", "Middle", "High"] # Establish an array of school names
males = []                                      # Establish an array of males and females
females = []
for school in school_names:                     
    males.append(schools[school]['Male'].sum()) # Calculate the sum of the male students within each specific school in the schools dictionary (Look at # of males throughout elementary and add it up)
    females.append(schools[school]['Female'].sum()) # Same ^

data = dict(school_names=school_names, males=males, females=females) # Create a dict to store data

categories = ['m', 'f'] # Establish categories for male and female     
colors = ["#718dbf", "#e84d60"]                                         
x = [(school, category) for school in schools for category in categories] # For every school 
y = sum(zip(data['males'], data['females']), ())                       

data = dict(x=x, y=y)
source = ColumnDataSource(data=data)

grouped_visual = figure(title="Total Male vs. Female Enrollment by Grade", x_range=FactorRange(*x), y_range=(0,80),
                        x_axis_label='Grade', y_axis_label="Enrollment", plot_height=400, plot_width=800)

grouped_visual.vbar(x='x', top='y', width=0.7, source=source, fill_color=factor_cmap('x', palette=colors, factors=categories, start=1, end=2))

grouped_visual.xgrid.grid_line_color = None
show(grouped_visual)