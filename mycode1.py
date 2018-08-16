
# coding: utf-8

# In[ ]:

name = "superman"

NewAge = 100


# In[ ]:


newage = 50


# In[ ]:


newage = age - 50


# In[ ]:


sequence = "CTAGCTAG"


# In[1]:


print(sequence)


# In[2]:


sequence = "CTAGCTAG"


# In[3]:


print(sequence)


# In[4]:


print(sequence[3])


# In[5]:


print ("my fourth letter is", sequence [3])


# In[6]:


len(sequence)


# In[10]:


print ("the length of the squence"),len(sequence)


# In[11]:


len(sequence)


# In[12]:


COX1 = "CTAG"


# In[13]:


sequence[0]


# In[14]:


sequence[1]


# In[15]:


sequence[0:3]


# In[16]:


COX2 = "TACG"


# In[17]:


COX1 = "CTAG"


# In[18]:


COX1 + COX2


# In[19]:


COX1 + " " + COX2


# In[20]:


age


# In[21]:


age = 99


# In[22]:


age


# In[23]:


len(age
)


# In[24]:


name + age


# In[25]:


5**2


# In[26]:


5***2


# In[27]:


5*2


# In[28]:


5**2


# In[29]:


print(5**2)


# In[30]:


print("5 square is", 5**2)


# In[31]:


print ("the length of the squence",len(sequence))


# In[32]:


5%2


# In[33]:


7%2


# In[34]:


# this is a comment


# In[35]:


# add these two genes were the same. So they were added


# In[36]:


max (23,2,5)


# In[37]:


round (3.14232)


# In[38]:


round (3.1423253145, 2)


# In[39]:


min (2,3,43,8)


# In[40]:


help (min)


# In[41]:


max (21, 32, 45) + min (21, 32, 45)


# In[42]:


hundred_C = "c" * 100


# In[49]:


print (hundred_C)


# In[50]:


hundred_C + COX1


# In[51]:


len (hundred_C + COX1)


# In[52]:


import math


# In[53]:


math.sin(3.14)


# In[54]:


print("the cos of 180 is", math.cos(180))


# In[55]:


math.sin(math.pi)


# In[56]:


math.cos(math.pi)


# In[57]:


help(math)


# In[58]:


import math as m


# In[59]:


from math import cos


# In[60]:


cos (180)


# In[61]:


import math


# In[62]:


print("sin(pi/2)")


# In[63]:


print("sin(pi/2) =",sin(pi/2))


# In[64]:


print("sin(pi/2) =",math.sin(math.pi/2))


# In[66]:


import pandas


# In[ ]:


pandas.read_csv


# In[68]:


"data/data/gapminder_gdp_oceania.csv"


# In[69]:


pandas.read_csv("data/data/gapminder_gdp_oceania.csv")


# In[70]:


pandas.read_csv("data/data/gapminder_gdp_americas.csv")


# In[71]:


data = pandas.read_csv("data/data/gapminder_gdp_oceania.csv")


# In[75]:


print (data)


# In[74]:


data = pandas.read_csv("data/data/gapminder_gdp_oceania.csv", index_col="country")


# In[76]:


data.info ()


# In[80]:


america = pandas.read_csv("data/data/gapminder_gdp_americas.csv", index_col="country")


# In[81]:


print(america)


# In[83]:


america.describe ()


# In[84]:


print(america)


# In[85]:


america.T.describe ()


# In[87]:


print (america.T)


# In[88]:


america.columns


# In[89]:


data


# In[91]:


data.iloc[0,0]


# In[93]:


data.iloc[:,0]


# In[95]:


data.iloc[0, 0:3]


# In[98]:


subset=data.iloc[:, 0:3]


# In[99]:


print(subset > 11000)


# In[100]:


subset [subset >11000]


# In[110]:


europe = pandas.read_csv("data/data/gapminder_gdp_europe.csv",index_col="country")


# In[111]:


print (europe)


# In[115]:


europe.iloc ["Serbia",:]


# In[113]:


europe.iloc ["Serbia",:]


# In[114]:


europe.iloc["Serbia",:]


# In[116]:


print (europe)


# In[118]:


europe.iloc[2:4,"Italy":"Norway"]


# In[127]:


europe.loc["Albania",:]


# In[ ]:


"Italy":"Norway"

