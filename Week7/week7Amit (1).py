#!/usr/bin/env python
# coding: utf-8

# ## <font color=green> Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products. </font>
# 
# ## <font color=green> 1. Add 12 Records. Take input from user.</font>

# In[1]:


import csv


# In[2]:


with open ("C:\\22bca02\\product.csv",'w') as f:
    data=csv.writer(f)
    header=["Prod_no","Prod_name","Jan","Feb","Mar","Apr","May","Jun"]
    data.writerow(header)
    for i in range(12):
        prod_no=int(input("Enter product no:"))
        prod_name=input("Enter product name:")
        jan=int(input("Enter product selling of jan:"))
        feb=int(input("Enter product selling of feb:"))
        mar=int(input("Enter product selling of mar:"))
        apr=int(input("Enter product selling of apr:"))
        may=int(input("Enter product selling of may:"))
        jun=int(input("Enter product selling of jun:"))
        record=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        data.writerow(record)


# In[134]:


with open ("C:\\22bca02\\product.csv",'r') as f:
    data=csv.reader(f)
    for i in data:
        print(i)


# ## <font color=green> 2.Create dataframe.</font>

# In[135]:


import pandas as pd


# In[136]:


df=pd.read_csv("C:\\22bca02\\product.csv",sep=",")
df


# ## <font color=green>3. Change Column Name Product No, Product Name, January, February, March, April, May, June.</font>

# In[137]:


df.columns=["Product_no","Product_name","January","February","March","April","May","June"]


# In[138]:


df


# ## <font color=green> 4.Add column "Total Sell" to count total of all month and "Average Sell"</font>

# In[139]:


df["Total sell"]=df["January"]+df["February"]+df["March"]+df["April"]+df["May"]+df["June"]


# In[140]:


df


# In[141]:


df["Average sell"]=df["Total sell"]/6


# In[142]:


df


# ## <font color=green> 5. Add 2 row at the end.</font>

# In[143]:


df.loc[12],df.loc[13]=[113,"Htmi",8000,10000,6000,7000,9000,12000,52000,8666.666],[114,"Camera",4000,5600,4780,8974,5051,5647,34052,5675.3333333333]
df


# In[144]:


df


#  ## <font color=green> 6. Add 2 row after 3rd row. </font>

# In[145]:


df.loc[3.5]= [115,"Ram",5000,2540,2650,2658,2564,2589,18001,3000.16666666] # Append list at the bottom
df = df.sort_index().reset_index(drop = True)  # Reorder DataFrame
df 


# In[146]:


df.loc[4.5]= [116,"Router",5880,2140,1150,9858,2164,1589,22781,3796.83333333] # Append list at the bottom
df = df.sort_index().reset_index(drop = True)  # Reorder DataFrame
df 


# ## <font color=green> 7.Print first 5 row.</font>

# In[147]:


df.head()


# ## <font color=green> 8.Print Last 5 row.</font>

# In[148]:


df.tail()


# ## <font color=green> 9.Print row 6 to 10.</font>

# In[150]:


df.iloc[6:11]


# ## <font color=green> 10.Print only product name.</font>

# In[151]:


df["Product_name"]


# In[152]:


df


# ## <font color=green> 11.Print sell of January month with product id and product name.</font>

# In[153]:


df[["January","Product_no","Product_name"]]


# ## <font color=green> 12.Print only those product id , product name where january sell is > 5000 and February sell is >8000 .</font>

# In[128]:


df[(df["January"] > 5000) & (df["February"] > 8000)]
print("January > 5000 and February > 8000:")
df[["Product_no", "Product_name"]]


# ## <font color=green> 13.Print record in sorting order of Product name.</font>

# In[129]:


df.sort_values(by="Product_name")


# ## <font color=green> 14. Display only odd index number column record.</font>

# In[130]:


df.iloc[1::2]


# ## <font color=green> 15.Display alternate row.</font>

# In[157]:


df.iloc[::2]


# In[ ]:




