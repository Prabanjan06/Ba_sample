# %%writefile sample.py
import streamlit as st

# Title
st.title("Guide for Streamlit !!!")
# Header
st.header("Certificate course on Business Analytics With Python")
# Subheader
st.subheader("offered by Dept of AMCS, TCE, Madurai")
# Text
st.text("Welcome you ALL!!!")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
# display the text if the checkbox returns True value
st.text("Showing the widget")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
