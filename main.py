
import streamlit as st
import pandas as pd
import time


st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Streamlit Interactive Demo")
 
st.write(
    "This application demonstrates different Streamlit "
    "functions and interactive widgets."
)

st.header("1️⃣ Text and Headings")

st.subheader("Streamlit Functions")

st.write("This is created using **st.write().**")

st.text("This is created using **st.text().**")

st.caption("This is created using st.caption().")

st.markdown("**This is Markdown text.**")

st.divider()


st.header("2️⃣ Input Widgets")

# Text Input
name = st.text_input("Enter your name", placeholder="Type your name here...")

# Text Area
message = st.text_area("Enter your feedback", placeholder="Type your message here...")

# Number Input
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=1,
    step=5
)

# Radio Button
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

# Selectbox
city = st.selectbox(
    "Select City",
    ["Mumbai", "Delhi", "Pune", "Bangalore"]
)

# Multiselect
skills = st.multiselect(
    "Select your skills",
    ["Python", "SQL", "Excel", "Power BI",
     "Machine Learning", "Deep Learning"]
)

# Slider
experience = st.slider(
    "Years of Experience",
    0,
    20,
    1
)

# Checkbox
is_student = st.checkbox("Are you a student?")
# multi_checkbox=st.multiselect(
#     st.checkbox("Select your hobbies"),
#     ["Reading", "Traveling", "Gaming", "Cooking", "Sports"]
# )

# Date Input
dob = st.date_input("Select your date of birth")

# Time Input
meeting_time = st.time_input("Select meeting time")

# Color Picker
color = st.color_picker("Choose a color", "#00f900")

# File Uploader
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

# Camera Input
# picture = st.camera_input("Take a picture")

# Audio Input
audio = st.audio_input("Record your audio")

# Feedback
feedback = st.feedback("stars")

st.divider()

st.header("3️⃣ Button")

if st.button("Submit Information"):

    st.subheader("Your Submitted Information")

    st.write("Name:", name)
    st.write("Feedback:", message)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Experience:", experience)
    st.write("Are you a student?:", is_student)
    st.write("Date of Birth:", dob)
    st.write("Meeting Time:", meeting_time)
    st.write("Selected Color:", color)
    st.write("Feedback Rating:", feedback)

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded CSV Data:")
        st.dataframe(df)

    # if picture is not None:
    #     st.image(picture)

    # if audio is not None:
    #     st.audio(audio)

    st.success("Information submitted successfully!")

st.divider()

st.header("4️⃣ File Uploader Preview")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.write("Preview of uploaded data:")

    st.dataframe(df)

st.divider()

st.header("5️⃣ Columns and Metrics")

df=pd.read_csv("Covid19.csv")
st.write(df.head())
col1, col2, col3, col4,col5,col6,col7 = st.columns(7)

with col1:
    st.metric("Total Students", 100)

with col2:
    st.metric("Average Age", 25)

with col3:
    st.metric("Pass Percentage", "92%")

with col4:
    st.metric("Fail Percentage", "35")
with col5:
    st.metric("Total Courses", 10)
with col6:
    st.metric("Total Results", 100)
with col7:
    st.metric("Total Teachers", 10)
    
    
st.divider()

st.header("6️⃣ Tabs")

tab1, tab2, tab3 = st.tabs(
    ["Student", "Course", "Result"]
)

with tab1:
    st.write("Student Information")
    st.write(df.head())

with tab2:
    st.write("Course Information")
    st.write(df.tail())
with tab3:
    st.write("Result Information")
    st.write(df.sample(5))
    
st.divider()

st.header("7️⃣ Expander")

with st.expander("Click here to see more information"):

    st.write(
        "This content is hidden inside an expander. This is made using streamlit."
    )

st.divider()

st.header("8️⃣ Status Messages")

st.success("Success message")

st.info("Information message")

st.warning("Warning message")

st.error("Error message")

if st.button("Show Exception"):

    st.balloons()
st.divider()

st.header("9️⃣ Spinner")

if st.button("Start Processing"):

    with st.spinner("Processing..."):
        time.sleep(5)

    st.success("Processing completed!")

st.divider()

st.header("🔟 Display Image")

st.image(
    "BFly.jpeg",
    caption="Sample Image",
    # width=800
)

st.write("You can display images using st.image().")

st.divider()

st.header("1️⃣1️⃣ Colored Text")

st.markdown(
    "This text is normal, but this is :red[colored red]!"
)

st.write(
    "You can also make text :blue[blue] "
    "by wrapping it."
)

st.header(
    "Rainbow headings look like this: "
    ":rainbow[My Rainbow Title]"
)

st.markdown(
    "Status: :green-badge[Completed] "
    "or :orange-badge[In Progress]"
)

st.divider()

st.header("🎉 End of Demonstration")

st.success(
    "This application demonstrates the major "
    "Streamlit widgets and functions."
)


st.sidebar.header("THis is about the side bar")

st.sidebar.selectbox("Show Sidebar", ['Bar Chart', 'Column Chart', 'Line Chart', 'Area Chart', 'Pie Chart', 'Scatter Plot', 'Histogram', 'Heatmap', 'Box Plot'])