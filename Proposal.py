#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import seaborn as sns 
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff


# In[3]:


# Expand the web app across the whole screen
st.set_page_config(layout="wide")


# In[19]:


# Image
image=Image.open("/Users/user/Desktop/Proposal/Ineq.jpeg")
new_image2 = image.resize((1300, 400))
st.image(new_image2,use_column_width=False)


# In[13]:


# Create containers horizontally
header = st.container()
data = st.container()
features = st.container()
Interactive_visu = st.container()
Interactive_visu_2 = st.container()
Interactive_visu_3 = st.container()


# In[18]:


with header:
    st.markdown("<h1 style='text-align: center; color: black;'> #Equality of Tomorrow </h1>", unsafe_allow_html=True)
    col1,col2,col3=st.columns([1,6,1])
    col2.text("""
    Imagine we live in a data-abundant world and yet we are still searching for means to prove inequality. 
    Imagine that we live on the same planet, under the same umbrella yet living conditions are vastly unequal 
    between different places all over the world. 
    Imagine that for a child born today in one of the poorest regions such as Africa, getting a healthy, secured, 
    productive life requires overcoming hurdle after hurdle. 
    The inequality of today is the consequences of unequal progress of yesterday. 
    Every person should have an equal opportunity to lead a prosper, healthy and productive life. 
    It is true that we do not have control over the place where we are born, 
    but for sure this shouldn’t determine our chance or right 
    for a prosper and good life.
    There is no reason to believe that what was possible for countries in North America and Europe 
    should not be possible for the rest of the world. 
    Our generation has a lot of opportunities and responsibilities to allow every part of the world to develop 
    into a place where health, security, access to education, and prosperity are a reality.  
    We should even the odds and provide everyone – no matter their nationality – the chance of a good life.
    
    """)


# In[10]:
with data:
    data = pd.read_csv("/Users/user/Desktop/Proposal/World_indicators.csv")
    if st.checkbox("Preview a Sample of our Dataset"):
        st.text("""
                 The dataset we will be using to launch our organization’s activities and mission is “World Development Indicators dataset”. 
                 This dataset contains a total of 338,000 rows and a a lot of indicators that will help us study the status of development
                 of all countries over the world in different fields from 1960 until 2021.
                 """)
        number = st.slider("Select No of Rows", 1, data.shape[0])
        st.write(data.head(number))
    


# In[7]:


with Interactive_visu:
    Our_Mission = st.checkbox("Our Mission")
    if Our_Mission:
        col,img =st.columns([3,1])
        col.text("""
                As Anthony Atkinson said: “if we are concerned about equality of opportunity tomorrow, 
                we need to be concerned about inequality of outcome today”. 
                Therefore, in one of our milestones we will be taking closer look at the layers of inequality 
                and we will examine them globally.  
                In 2018, the United Nations published a diagram that shaped 
                the complexity of inequality and showed five overlapping categories, 
                where each of which can be divided into serval subcategories. 
                Our mission will focus on socio-economics, demographics and shocks and fragility dimensions.
                """)
    
        image1=Image.open("/Users/user/Desktop/Proposal/UN.png")
        new_image = image1.resize((800, 600))
        img.image(new_image,width=None, caption= "Layers of Inequality")
       


# In[8]:


with Interactive_visu_2:
    Our_Vision = st.checkbox("Our Vision")
    if Our_Vision:
        st.text("""
        Many campaigns and NGOs worked to improve and raise awareness on global inequality. 
        A lot of their efforts covered a wide variety of inequalities,
        However, our organization will focus “on data and research” to make progress against global inequalities. 
        Once we know what is happening over the globe, study patterns of improvements and strategies implemented, 
        discover unequal places, then we can surely work closely with concerned parties sush as governments,
        world bank, volunteers, and donors to take actions and increase the chances for a good life.
         """)
        


# In[15]:


with Interactive_visu_3:
    Donate = st.checkbox("Donate")
    if Donate:
        col1,img1 =st.columns(2)
        col1.markdown("<h1 style='text-align: center; color: black;'>                 </h1>", unsafe_allow_html=True)
        col1.markdown("<h2 style='text-align: center; color: black;'> Alone we can do so little </h2>", unsafe_allow_html=True)
        col1.markdown("<h3 style='text-align: center; color: black;'> Together we can do so much </h3>", unsafe_allow_html=True)
        
        image2=Image.open("/Users/user/Desktop/Proposal/Donate.png")
        new_image1 = image2.resize((550, 300))
        img1.image(new_image1,width=None, caption= " Giving is the greatest act of grace")
       

