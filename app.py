#deploy to cloud

import streamlit as st

# demo plot graph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a simple dataframe
data = {
    'x': np.arange(1, 101),
    'y': np.random.randn(100)
}
df = pd.DataFrame(data)

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'])

# Customize the plot with some labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('A Simple Scatterplot')

# Add a bad line to test code quality tool
undefined_variable = this_variable_does_not_exist

# Display the plot
st.pyplot(fig)