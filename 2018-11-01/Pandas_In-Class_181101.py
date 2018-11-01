
# coding: utf-8

# <img src="files/img/pandas.png" alt="Operations Across Axes" />

# # [Pandas](http://pandas.pydata.org/) - Python Data Analysis Library
# ---
# 📢 But first the [news](https://pythonbytes.fm/episodes/show/101/nobel-prize-awarded-to-a-python-convert)!
# ---
# ## I shamelessly picked from these folks:
#  - [Daniel Chen - Pandas for Data Analysis](https://www.youtube.com/watch?v=oGzU688xCUs)
#  - [Jeff Delaney - 19 Essential Snippets in Pandas](https://jeffdelaney.me/blog/useful-snippets-in-pandas/)
#  - [Burke Squires - Intro to Data Analysis with Python](https://github.com/burkesquires/python_biologist/tree/master/05_python_data_analysis)
# 
# 
# ## General Outline:
# - What is Pandas all about?
# - Brief intro to Pandas objects and syntax
# - NumPy dataframe, show the basics
# - Import gapminder dataset, interactive

# ## [Jupyter Notebook Shortcuts](http://maxmelnick.com/2016/04/19/python-beginner-tips-and-tricks.html)
# - documentation:
# ```python
# type?
# ```
# - check function arguments using: shift + tab
# - run current cell/block: shift + enter 
# - insert cell above: esc + a
# - delete cell: esc (hold) + d + d (double tap)

# <img src="files/img/python-scientific-ecosystem.png" alt="Python Scientific Ecosystem" />
# 
# ## [Legend has it...](https://qz.com/1126615/the-story-of-the-most-important-tool-in-data-science/ )
# Pandas was develped by Wes McKinney (from Akron, Ohio!!!).  Math guy from MIT that went into finance, found that the problem with hedge fund management was dealing with the data (sourcing new data, merging it with the old, and cleaning it all up to optimize the input).  He got bummed out with Excel and R but was smitten with Python, though he realized there was no robust package for data analysis.  So he built Pandas in 2008 and released the project to the public in 2009.
# 
# Here's where it get's crazy, he left the world if finance to pursue a PhD in statistics at Duke, thus dropping Pandas development.  During that period he realized Python as a language could explode as a statistical computing language, it had the potential, but was still missing robust packages.  So he dropped out to push Pandas to become the a cornerstone of the Python scientific ecosystem.
# 
# And he put all his tips and tricks for Pandas into a book: [Python for Data Data Analysis](https://github.com/wesm/pydata-book)
# 
# ## What is Pandas?
# 
# "It enables people to analyze and work with data who are not expert computer scientists.  You still have to write code, but it's making the code intuitive and accessible.  It helps people move beyond just using Excel for data analysis." ~Wes
# 
# - The go-to data analysis library for Python
#     - Import and wrangle your raw data
#     - Manipulate and visualize
# - Allows for mixed data types in the same array
# 
# ### The DataFrame is your friend!
# - Two primary object types used in Pandas:
#     - DataFrames - like an Excel spreadsheet
#     - Series - like a single column in a spreadsheet
# - DataFrames are the primary object used in Pandas (it's like an Excel sheet)
# - Each DataFrame has:
#     - columns: the variables being measured
#     - rows: the observations being made
#     - index: maintains the order of the rows
# - Executing an action across an axis
#     - Axis 0 = default, 'index', perform action along index (performing in each column)
#     - Axis 1 = 'columns', perform action along columns (performing for each row)
#     - This is kinda wonky, but you can think of it like this:
#         - Axis 0 will give me mean of each column
#         - Axis 1 will give me the mean of each row
# 
# <img src="files/img/dataframe.jpg" alt="Pandas DataFrame" />

# # Getting Started
# ---
# You can import LOADS of different file types into Pandas as a DataFrame.  The most common that you may run into would be .csv and Excel files, but we're going to start by using a NumPy array as the input for our DataFrame.
# 
# ## Create A NumPy Array Of Test Data

# In[ ]:


# check numpy version


# In[ ]:


# create an object "array" that is a 4x100 numpy ndarray (use numpy.random.randint())
# be sure to set the seed to 0 if you want to replicate the results


# In[ ]:


# check the type of the array object


# ## Create A Pandas DataFrame

# In[ ]:


# import the pandas library


# In[ ]:


# checkout the documentation for a DataFrame (?)


# In[ ]:


# create a Pandas DataFrame object called "df" from the "array" object we made earlier


# ## Exploring A DataFrame

# In[ ]:


# check out what the "df" looks like


# In[ ]:


# check the "df" shape


# In[ ]:


# you can also use the len() function to get the number or rows/observations


# In[ ]:


# get a concise summary of the DataFrame with .info()


# In[ ]:


# view brief descriptive stats of the DataFrame


# In[ ]:


# view the top 5 rows
# you can input how many rows you want, default is 5
 


# In[ ]:


# view the bottom 5 rows


# In[ ]:


# take a sample of random rows/observations


# ## Manipulating DataFrame Columns (Variables)

# In[ ]:


# view current columns 


# In[ ]:


# send current column names to a list


# In[ ]:


# change column names
# create a list of new column names "a"-"d"
# must be same length the number of columns in the "df"

# set "df.columns" to the new list of names

# check the change by viewing the head of the dataframe


# In[ ]:


# select just column "a"


# In[ ]:


# check the type of column "a"
# notice that a single column is a "Series" object in Pandas


# In[ ]:


# insert a new column (called "new_column") and put a string in each cell


# In[ ]:


# shuffling column positions

# make a list of the current column order


# In[ ]:


# manipulate column names as a list object
# reverse column order with [::-1]


# In[ ]:


# move last column to first (hint: [-1:] + [:-1])


# In[ ]:


# set the column order (creates new dataframe) (hint: df = ...)


# In[ ]:


# drop/remove "new_column" from the dataframe


# In[ ]:


# check if the column is really gone


# In[ ]:


# write returned df to a new object


# In[ ]:


# we still have our original df


# In[ ]:


# Alternative to drop a column:
# use 'inplace=True' to overwrite existing dataframe


# ## Calculating Values from the DataFrame

# In[ ]:


# Pandas has basic arithmetic functions built-in


# ## Axis Key
# - 0 == Calculate statistic for each column (across rows)
# - 1 == Calculate statistic for each row (across columns)
#   
# <img src="files/img/python-operations-across-axes.svg" alt="Operations Across Axes" />
# 
# * The axis key is reversed when using the drop() function to remove columns/rows

# In[ ]:


# get the sum of each row by setting the axis to 1


# In[ ]:


# get the sum of columns ['a', 'b'] for each row


# In[ ]:


# add a new column called "sum" containing the sum of each row


# In[ ]:


# does the sum stay updated?
# insert a new row of random integers and see if values in "sum" change


# ---
# ## Exercise
# 1. Make an object titled "df3" that is a copy of "df"
# 2. Add a column to "df3" that expresses the [mean](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mean.html) of the values in columns a, b, c, and d across each row 
#     * What axis refers to calculations across a row?
# 3. Make an object titled "df4" that is a copy of "df3" and delete column "c" from df4 
#     * Do the values in the "mean" column change?

# In[ ]:


# Make an object titled "df3" that is a copy of "df"


# In[ ]:


# create a mean column in df3 that calculates the mean across each row
# be sure to exclue the sum value from the mean


# In[ ]:


# make a copy of df3 named df4, delete column "c"


# ---
# ## Combining DataFrames
# Before getting into the manipulation of DataFrame rows it helps to understand a bit more about index values and combined dataframes
# <img src="files/img/concat_axis0.png" alt="concat axis0" />

# In[ ]:


# create two new DataFrames from NumPy values


# In[ ]:


# Use pd.concat() to combine the two DataFrames by stacking vertically (hint: axis=0)


# In[ ]:


# check the index


# In[ ]:


# reset_index() will generate a column with the old index
# use this function when you want to reset the order of the index

# reset = cat_df.reset_index(drop=True) # use this to drop the new column with old index


# ## Manipulating DataFrame Rows (Observations)
# Two important functions to introduce here are loc() and iloc()
# - loc[ ] - accesses the index based on the value
# - iloc[ ] - accesses the index based on the position.  
# You may come across ix[ ] to select rows, but this function has depreciated 
# 
# Tips for specifying indexers:
# - series.loc[indexer]
# - dataframe.loc[row_indexer, column_indexer]

# In[ ]:


# We're going back to the concatenated Dataframe that was NOT reindexed
# select a row based on the index value using loc


# In[ ]:


# compare this with selecting a row using iloc


# In[ ]:


# changing all the values in a specific row (position 0)


# In[ ]:


# change a single value in a row using loc[] (hint: loc uses names)


# In[ ]:


# add a row using loc[] 
# (hint: use the length of cat_df to position the new row at end)


# In[ ]:


# delete the row that was just added using drop()


# ## Exporting A DataFrame
# If you want to save your work you can [pickle](https://ianlondon.github.io/blog/pickling-basics/) the DataFrame or you could export it as a file

# In[ ]:


# saving the "new" DataFrame as a .csv file, can export in multiple file types
# hint: seperator type by default is a comma


# ## Plots
# In general, the [Matplotlib](https://matplotlib.org/) library is the go-to for plots and figures, but Pandas has a plot() function that uses matplotlib to generate basic visualizaitons

# In[ ]:


# import matplotlib.pyplot


# In[ ]:


# you can use the Pandas plot() function to return a matplotlib.axes.AxesSubplot object


# In[ ]:


# you can alter that object using matplotlib commands/functions
# save generated plot as "ax" and add labels (hint: use set_xlabel())


# In[ ]:


# save the figure by using get_figure() to extract the plot as 
# a matplotlib.figure.Figure object
# (hint: save ax object as "fig", then use savefig())


# ## Exercise
# - For reproducability, set your RandomState seed to 2000
# - Create a dataframe with 10000 observations (can use NumPy)
#     - Variable "a": randomly assign a value of 0 or 1
#     - Variable "b": randomly assign a value from a normal distribution (center of 0 and a standard deviation of 1)
# - make a histogram of the distrubution of variable "b"
# - filter dataframe down to the 90th percentile of variable "b" and plot histogram for "b"

# In[ ]:


# solution


# In[ ]:


# threshhold for 90th percentile of "b"


# In[ ]:


# select values above threshhold for "b"


# # Working With Heterogeneous Data
# ---
# ## Import a .csv as a Pandas DataFrame

# In[ ]:


# import a .csv file to a DataFrame


# In[ ]:


# strip-down column names


# ## Take A Glance At The DataFrame

# In[ ]:


# shape, columns, values


# ## Techniques To Filter Data

# In[ ]:


# Sorting
# Why not sort the df by year in ascending order (hint: use sort_values())


# In[ ]:


# Unique Values
# Get a list of the countries represented using unique()


# In[ ]:


# What about continents?


# In[ ]:


# Using the groupby() function:


# In[ ]:


# How would I get a list of the countries that fall within "Oceania"?


# In[ ]:


# nunique()
# How many countries are represented by each continent?


# In[ ]:


# What about a dictionary containing all the countries for each continent?
# hint: create a groupby object and use the todict() function


# In[ ]:


# use dictionary to get number of countries in Africa


# In[ ]:


# Filter Using Conditional Logic
# What if we just want a DataFrame of all the African countries?


# In[ ]:


# reset the index


# In[ ]:


# explore the new africa df


# In[ ]:


# create a new series with the mean gdp per cap for each country in africa


# In[ ]:


# create a boxplot


# In[ ]:


# view gdp changes over time for each country using pivot
# hint: index='year', columns='country', values='gdp_per_cap'


# In[ ]:


# what are the countries that peak out over 10,000 gdp-per-cap units?


# # Misc.
# ---
# ## Create a Pandas DataFrame from a dictionary

# In[ ]:


# create a dictionary object
my_dict = {'a':['cheese', 'dog', 'goat', '4h'], 'b':['lush','planet', '2017', 'la trance'] }

# create a pandas DataFrame from a dictionary
df = pd.DataFrame(my_dict)
df


# In[ ]:


# create a new dataframe from groupby() using .reset_index()
df = pd.read_csv('data/gapminder.tsv', sep='\t')
group = df.groupby('continent')['country'].unique().reset_index() # reseting the index is key
group


# In[ ]:


# column containing list of values, count those values as value for new column
group['num_countries'] = group['country'].str.len()
group


# In[ ]:


# clean-up column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')

