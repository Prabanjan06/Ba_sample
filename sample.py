%%writefile sample.py
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

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("/content/sample_data/logo (2).png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

	# display the text if the checkbox returns True value
	st.text("Showing the widget")


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")



st.sidebar.title("This text written in the sidebar");
st. sidebar.button("click me")
st. sidebar.radio("Pick ur gender",["male","female"])

