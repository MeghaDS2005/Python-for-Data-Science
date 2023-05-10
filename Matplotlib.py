#!/usr/bin/env python
# coding: utf-8

# # MatplotLib 
# 
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.
# 
# Some of the major Pros of Matplotlib are:
# 
# Generally easy to get started for simple plots
# Support for custom labels and texts
# Great control of every element in a figure
# High-quality output in many formats
# Very customizable in general
# 

# In[1]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


## Simple Examples

x=np.arange(0,10)
y=np.arange(11,21)


# In[3]:


##plotting using matplotlib 

##plt scatter

plt.scatter(x,y,c='g')


# In[5]:


plt.scatter(x,y,c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')


# In[7]:


plt.scatter(x,y,c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
plt.savefig('Test.png')


# In[8]:


y=x*x
## plt plot

plt.plot(x,y,'r*',linestyle='dashed',linewidth=2, markersize=12)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('2d Diagram')


# In[11]:


x = [1, 2, 3]
z=np.multiply(x,x)
y = np.array([[1, 2], [3, 4], [5, 6]])
plt.plot(z, y)


# In[12]:


## Creating Subplots

plt.subplot(2,2,1)
plt.plot(x,y,'r--')


# In[17]:


plt.subplot(2,2,1)
plt.plot(x,y,'r--')


# In[16]:


plt.subplot(2,2,2)
plt.plot(x,y,'g*--')


# In[14]:


plt.subplot(2,2,3)
plt.plot(x,y,'bo')


# In[13]:


plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[18]:


plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[19]:


x = np.arange(1,11) 
y = 3 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()


# In[20]:


np.pi


# In[21]:


# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 4 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 


# In[22]:


#Subplot()
# Compute the x and y coordinates for points on sine and cosine curves 
x = np.arange(0, 5 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   
# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)
   
# Make the first plot 
plt.plot(x, y_sin,'r--') 
plt.title('Sine')  
   
# Set the second subplot as active, and make the second plot. 
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos,'g--') 
plt.title('Cosine')  
   
# Show the figure. 
plt.show()


# In[26]:


## Bar plot

x = [2,8,10] 
y = [11,16,9]  

x2 = [3,9,11] 
y2 = [6,15,7] 
plt.bar(x, y) 
plt.bar(x2, y2, color = 'g') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()



# In[27]:


a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
# The x-axis will have the value of array a and the y-axis will have the value of density. The bins show the density.
# By default, the value of bins will be 10 but if we want to change, we can also change the size of the bins.

plt.hist(a) 
plt.title("histogram") 
plt.show()


# In[39]:


data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# A lower value is 0, a higher value is up to the standard deviation, and step count is 100.
# This box plot is used to generate percentiles.
# The standard deviation will loop from 1 to 4. In the first step it will be between 0 to 1 then 100 steps, 2nd step 0 to 2 and in 3rd 0-3.

# rectangular box plot
type(plt.boxplot(data,vert=True,patch_artist=True)); 
# Here, vert basically provides the percentiles to be represented as vertically and horizontally. True-> vertically and false-> horizontally.
# Patch_artist provides colour. False no colour and true means coloured representation.


# In[35]:


type(data)


# In[37]:


data


# In[38]:


# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.4, 0, 0, 0)  # explode 1st slice
# explode means the how far the slice will go from the pie chart
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False)
# autopact =1.1f means representation od percentage in floating point form. Shows means shadow of slices.
plt.axis('equal')
plt.show()


# In[40]:


type(labels)


# In[41]:


type(sizes)


# In[42]:


type(colors)


# In[43]:


type(explode)


# In[ ]:




