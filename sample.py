# %%writefile sample.py
import pandas as pd
import numpy as np
import streamlit as st
# import matplotlib.pyplot as plt  # Uncomment this line

# Read the CSV file
df = pd.read_csv('sales.csv')

# Title
st.title("AJPK Super Market")

# import Image from pillow to open images
from PIL import Image
img = Image.open("asset/istockphoto-1412353022-2048x2048.jpg")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=800)

# Header
st.header("Super Market Sales Report")

st.write("DataFrame")
st.write(df.describe())


