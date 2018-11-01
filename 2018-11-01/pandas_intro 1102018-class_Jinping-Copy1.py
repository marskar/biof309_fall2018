
# coding: utf-8

# Pandas
# 
# "80% of a data scientists valuable time is spent simply finding, cleaning, and organizing data, leaving only 20% to actually perform analysis"  ----IBM Data Analytics
# 
# pandas 0.23.4 documentation 
# 
# 1. DataFrame - slice data by row and column - groupby
# 2. Creating data sets and data frames - Reading from CSV - Exporting to CSV - Finding maximums - Plotting data
# 3. Data cleanling -NAs missing values
# 

# In[12]:


#Import libraries pd np os matplotlib.pyplot
import pandas as pd

# 1. DataFrame and slice data by row and column

# In[15]:


# Our small data set as data 0,1,2,3,4,5,6,7,8,9
data = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe by pd.DataFrame
df = pd.DataFrame(data)
df


# In[16]:


# Lets change the name of the d.columns as 'Rev'
df.columns = ['Rev']


# In[29]:


# Lets add a column 'NewCol' = 5
df['NewCol']=5
df


# In[33]:


# Lets add and modify our new column +1 np.log10(data+1) single cell seq


# In[25]:


df['NewCol']


# In[60]:


# Lets add a couple of columns: 'test', 'col' = 'Rev'


# In[61]:


# Create group object  New, d.groupby()


# Apply sum function  sum()


# In[1]:


# Create group object New and test and Newtest d.groupby 

# Apply sum function sum()


# In[62]:


# Create group object  , and test and Newtest, Newtest d.groupby, as_index=False


# Apply sum function sum()


# Select dataframe

# In[64]:


# If we wanted, we could change the name of the index: i ='a','b','c','d','e','f','g','h','i','j'
# df.index


# In[12]:


#select dataframe by row names .loc ['':'']


# In[13]:


#select dataframe by row numbers .loc[]
df.loc[1:5]


# In[14]:


# df.iloc[inclusive:exclusive] 
# Note: .iloc is strictly integer position based.  


# In[15]:


#select data frame by column name. slice 'Rev' out as a list 
#['Rev']
 


# In[16]:


#select data frame by column name. slice 'Rev' out as a table with double brackets
#[['Rev']]


# In[17]:


#select data frame by column name   multi-selection [['Rev','col']] 


# In[20]:


#select data frame by row and column .iloc


# In[21]:


#transpose data.T
transpose = d.T
transpose


# 2.Creating data sets and data frames - Reading from CSV - Exporting to CSV - Finding maximums - Plotting data

# In[22]:


# Create Data name and birhts number 
#names  'Bob','Jessica','Mary','John','Mel'
#births  968, 155, 77, 578, 973


# In[24]:


# zip two list together
BabyDataSet = list(zip(names,births))
BabyDataSet


# In[26]:


# change the list to pd.ataFrame with data and columns names 
#pd.DataFrame(data = , columns=['', ''])


# Export data

# In[28]:


# write births1880.csv as a "df.to_csv" csv file. 
#df.to_csv('data', index = False, header False)


# Get data

# In[32]:


# how to know your working directory: os.getcwd()


# In[39]:


# set up working directory 
#with births1880.csv file name as loca 

#pd.read_csv


# In[41]:


# read loca again with header = None


# In[42]:


# read loca again with columns' name, names = ('Name', 'Births')


# Understand your Data

# In[43]:


#Check data type .dtype


# In[50]:


#Check columns type .dtype


# In[44]:


#Check data head .head()


# In[45]:


#Check data head first row of the df.head


# In[46]:


#Check the data tail .tail


# In[47]:


# number of the rows and the columns .shape


# In[48]:


#Get the column name .columns


# In[51]:


#Get the maximum value of column 'Birth' .max()


# In[ ]:


#let's add another column 'Alive'


# Present Data

# In[57]:


# Create graph df['',''].plot.box()  print("The most popular name")




# In[75]:


# Create a dataframe with dates as your index
States  = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL' ]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

#df1 DataFrame data and columns=['Revenue']
df = pd.DataFrame(States, data)
df
# In[76]:


# Create a second dataframe
#data2 10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6

# df2 DataFrame with data2 and columns=['Revenue']
df2 = pd.DataFrame([10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6], columns=['Revenue'])

# In[35]:


# Combine dataframes pd.concat ([dataset1, dataset2 ...])
pd.concat([df, df2], axis=1, ignore_index=True)

# In[ ]:


#Combine dataframes pd.concat ([dataset1, dataset2 ...], ignore_index = True)


# In[78]:


#sorted data by column as sortdata    data.sort_values(by =[column])


# In[79]:


#Get the unique values for a column by name    data[column].unique()


# In[80]:


#Get a count of the unique values of a column   len (data[column].unique())


# 4. Data wrangling- Data munging -Missing values:
# *standard types: NA, NaN, ""
# *non-standard types: n/a, na, "--"
# *unexpected types:   Joe, Mary, Bob, 12(?)
# *summarizing: df.isnull(),sum()
# *replacing: df.fillna()

# In[62]:


#import property : download data "property data.csv" into working directory
# pd.read_csv()

#.head()


# In[76]:


#change all other types of missing value to standard type of NA
#set up missing_value  missing_values "n/a", "na","--"


# In[77]:


#read_csv with na_values setting


# In[82]:


#summarize the missing values
df.isnull().sum()


# In[48]:


# create NAs 
#drop NAs
df.dropna()


# In[87]:


#fill na with 0
df = df.fillna(0)
df.isnull().sum()

