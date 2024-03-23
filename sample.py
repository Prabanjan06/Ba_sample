# %%writefile sample.py
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# import matplotlib.pyplot as plt

# pip install matplotlib

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

# sns.heatmap(data.corr(),annot=True)
# plt.show()

def plot_gender_pie_chart(data):
    # Count the number of men and women
    gender_counts = data['Gender'].value_counts()

    # Plotting the pie chart
    st.write('### Gender Distribution')
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

def main():
    st.title('Gender Distribution Analysis')
    plot_gender_pie_chart(df)

if __name__ == "__main__":
    main()


# Subheader
# st.subheader("")

# Text
# st.text("Welcome you ALL!!!")


# Markdown
# st.markdown("### This is a markdown")

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


# df['Branch'].plot(kind='hist', bins=20, title='Branch')
# plt.gca().spines[['top', 'right',]].set_visible(False)
