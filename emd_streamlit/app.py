# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:38:35 2021

@author: mcapel
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# st.set_page_config(layout = 'wide')
st.title('Test')
st.markdown(' ## ** Test ** * app * to see if streamlit works')
st.radio(label = 'Does the app work?', options = ['Yes','No'])
st.sidebar.selectbox('App Navigation', options = ['Option 1','Option 2','Option 3'])

test_data = pd.DataFrame.from_dict({'BRL':[6.45, 6.47, 6.52, 6.34, 6.39, 6.24, 6.34, 6.33,6.32,6.29]})

fig = px.line(test_data.reset_index(), x = 'index', y = 'BRL', template = 'plotly_white')

st.plotly_chart(fig, use_container_width = True)