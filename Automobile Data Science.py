#!/usr/bin/env python
# coding: utf-8

# # The Relationship between the Cylinder count and Quarter mile time for auto mobiles.

# #### Adam Levere, 100864665

# ## Introduction:

# * **My question:** To explore and compare the relationships between cylinder count and quarter mile time. Which in itself has many independent variables affecting its dependent counterparts.

# * **Why my question:** The correlation between cylinder count and quarter-mile time is a fascinatingly different perspective in the world of auto engineering. Not only is this information extremely interesting for those in the tuning and performance world, but also shows the correlations related to daily driving and factors important to climate preservation and understanding transportation. Namely because, understanding factors that improve performance, can be good areas for subjectivity when considering how to improve performance and reduce resources to improve areas of life.

# * **My data:** Sourced and collected from an online git repository of 32 cars and their respective features. This includes valuable information, such as name, cylinder count, weight, quarter-mile time, horsepower, forward gears, and more.
# 

# * **Why my question with the given data:** ‘Speed’ or more specifically acceleration is something fascinated and loved by most, the idea that I'm comparing cylinder count to quarter-mile time, is something that isn't typically looked at. So for that reason, and the idea that companies now are reducing the number of cylinders in newer cars, piqued my interest in this topic. Especially because we are now moving away from typical combustion engines and I think it's important we talk about them more.
# 

# **Names and part functions as background information for the assessment:** MPG refers to the amount of gas that is used by the engine, per mile (Which is changed to litres used per 100kms). CYL refers to the number of cylinders in the engine or the primary source of power (either 4,6 or 8). HP refers to the gross horsepower of the engine at the crank (before it goes to the wheels, which does reduce it). The most important factor in improving quarter-mile time is the power to weight. Which is gross horsepower divided by the weight of the car. With weight being constant, and not easily manipulated, we focus on horsepower. Which includes for the most part cylinder count and displacement.
# 

# ### To Restate:

# **Considering that in a quarter-mile time, the largest factor that affects the time would be the power-to-weight ratio (Horsepower/Weight), we see that if weight is constant, more cylinders is linked to more displacement or horsepower. Which directly impacts the quarter-mile time.**
# 
# Exploring an interesting problem involving more unconventional methods of comparing cars, I chose to compare two features of cars that don't usually correlate themselves in the world of cars. That, there is no single value or variable that outweighs all other factors, I chose to first compare a value that relies on other variables in the data set. This includes the correlation between the number of cylinders and the displacement of the engine. Displacement in itself doesn't necessarily correlate to faster quarter-mile time but is an important factor, as is cylinder count.

# ## Data Locating
# * Printing the first 5 values to show values

# In[29]:


import pandas as pd
cars = pd.read_csv('https://gist.githubusercontent.com/noamross/e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv')
print(cars.head()) # print out the first 5 values of the data set


# ## Cleaning the data and improving readability.

# * Dropping any values needed, rounding to two decimal places and changing the column names.

# In[30]:


cars = cars.dropna(axis = 0)#Remove any none values

pd.set_option('display.precision', 2) #Set all data values to 2 decimals

cars.columns = ["Name","MPG","cyl","Disp","Gross hp","Rear axel ratio",
                "Weight","1/4 mile time","Engine shape (0-V,1-Straight)",
                "Transmission (0-auto, 1-manual)","# of forward gears","# of carberators"]

print(cars.head())


# ### More cleaning and converting values, to useable information.

# * Replacing 0 and 1, with V(V-style) and In(Inline)
# * Changing the Displacement values from cubic inches to cubic centimeters
# * Changing the weight value (multiplying by 1000)
# * Converted MPG to Litres per 100kms
# * Replaced the Transmission values

# In[31]:


cars['MPG'] = 235.214583 / cars['MPG']
cars = cars.rename(columns={'MPG':'L/100kms'})
cars = cars.replace({'Engine shape (0-V,1-Straight)': {0:'V',1:'In'}} ) #replacing 0 with V and 1 with IN - inline
cars = cars.replace({'Transmission (0-auto, 1-manual)':{0:'Auto',1:'Manual'}})
cars = cars.rename(columns={'Transmission (0-auto, 1-manual)':'Transmission'})
cars['Disp'] = (cars['Disp'] * 16.387).round() #to convert cubic inches to cubic centimetres and round to whole num
cars['Weight'] = cars['Weight'] * 1000
print(cars.head())


# * There are many factors that affect quarter-mile time estimation: 
# #1 **number of cylinders**, 2 **displacement**, 3 **gross hp** and 4 **weight**. Everything else makes a small much smaller diffrence ie transmission, engine shape and forward gears.

# ## Showing cylinder number relationships - looking at values with an impact on 1/4 mile times

# #### Describing the cylinder count in a graph format.
# 
# * The number of cylinders does two things when considering quarter-mile time. Since horsepower is a large factor in quarter-mile time, the number of cylinders is just as important. 
#     * More cylinders improve power smoothness, power delivery and increase the amount of force the engine can produce.

# #### Bar graph description:
# * Shows a larger number of 75% of 8 cylinder vehicles or below, 50% of 6 cylinder vehicles or below and 25% of 4 cylinder vehicles or below. 
# * Graph shows correlations of values centred around 4, 6 and 8 cylinders
# * No values in between

# #### Describe functionality:
# * A total number of 32 cars with this 'cyl' value.
# * Minimum at 4 and Maximum at 8.
# * Mean of 6.19, showing the average across the data set.

# In[32]:


print(cars['cyl'].describe())

cars_plot_cyl = cars.cyl.hist(bins=12,color = 'magenta',edgecolor = 'black')# To create a bar graph using .hist


# ## Showing quarter-mile time relationships

# #### Describing the quarter-mile times in a graph
# * Total count of 32 quarter-mile times 
# * Mean of 17.85, which is a relatively standard quarter-mile time
#   * This is represented in the graph, with values centred around 17-18 seconds
# * 25% of the values in the data set are 16.89 seconds or below 
# * 50% of the values are 17.71 or below
# * 75% of the values are 18.90 or below
# * Some values are below 16 and some higher then 22

# In[33]:


#Now to compare quarter-mile times
print(cars['1/4 mile time'].describe())

import seaborn as sns #using a seaborn graph 

cars_plot_miletime = sns.histplot(data = cars, x = '1/4 mile time')


# # Showing the displacment relationships

# #### To compare the values in displacement:
# * Total count of 32 data set values with 'Disp'
# * Mean around 3780cc of about 3.7L for engine size
# * Min at 1165cc and Max at 7735cc
# * Std deviation at 2031cc's
# * Shows alot more values towards 1000cc and 2000cc
#     * Shows a dip in the graph around 3500cc to 4500cc, and indicates that there arent very many values with that displacement

# In[34]:


#To show value distribution for displacement
print(cars['Disp'].describe())

cars_plot_disp = sns.histplot(data = cars, x = 'Disp', color = 'green')


# ## Comparing Displacement and Cylinder count
# 
# * As previously mentioned, power to weight is vital when looking at quarter-mile time, which is based on Horsepower with weight being constant. Horsepower is heavily influenced on displacement and cylinder count. So comparing displacement and clyinder count is valuable in coming to a conclusion that more cylinders directly affects quarter-mile time.
#     * As shown in this scatterplot, It is apparent that higher displacement in cars is linked to more cylinders. 
#     * As displacement increases, so does cylinder count. These values have a linear relationship.
#     * It is visually appearant that the lowest 8 cylinder displacement is much higher then the highest 4 cylinder displacement.
#         * This provides a strong correlation between the displacement and cylinder count.

# In[35]:


#Comparing data
cars_cyl_disp = sns.scatterplot(x = 'cyl', y = 'Disp', data = cars)
#There is a strong corrilation between engine size (displacement) and the number of cylinders in a engine.


# ## Scatter plot to compare displacement and quarter-mile time

# * Now to corrilate the higher displacement and cylinders to horse power - which affects 1/4 mile time.
# * This scatter plot, shows the higher displacements centre around lower quarter-mile times.

# In[36]:


cars_hp = sns.scatterplot(x = 'Disp', y = '1/4 mile time', data = cars)


# ## Linear regression line for scatter plot

# * To show the relationship between displacement and quarter-mile time.
#   * Making it obvious that as displacement increases, so does quarter-mile time.
#   * Since displacement and cylinder count are shown to directly be affected by eachother in a linear fashion, we see that so is quarter-mile time and displacement.
#   * As the displacement of the vehicle increases, so does the quarter-mile time.

# In[37]:


cars_hp_reg = sns.regplot(x = 'Disp', y = '1/4 mile time', data = cars)


# ## Regression line for cylinder count and quarter-mile time - final plot analysis

#  * Since displacement was earlier shown to be directly correlated from cylinder count. We can approach the relationship between cylinder count and quarter-mile time and conclude that there is an inverse relationship. Meaning as quarter-mile time decreases, the amound of cylinders increase. Proving the original hypothesis of this project.

# In[38]:


cars_qtime_cyl = sns.regplot(x = 'cyl', y = '1/4 mile time', data = cars)


# # Conclusion:
# * Proven by the scatter plots and bar graphs, we see that there is a direct relationship between the number of cylinders in a car, and the quarter-mile time it has. Not only because of the smoothened and improved power delivery, but because higher cylinder counts are corrilated to larger displacements.

# ### Sources of data and refrences
# 
# * https://gist.github.com/noamross/e5d3e859aa0c794be10b for repository
# * https://gist.githubusercontent.com/noamross/e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv for the raw data csv file
