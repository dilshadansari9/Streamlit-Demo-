import streamlit as st
import pandas as pd

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

name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=25
)

gender = st.radio(
    "Select Gender",
    ["Male", "Female"]
)

city = st.selectbox(
    "Select City",
    ["Mumbai", "Delhi", "Pune", "Bangalore"]
)

skills = st.multiselect(
    "Select your skills",
    ["Python", "SQL", "Machine Learning", "Deep Learning"]
)

experience = st.slider(
    "Years of Experience",
    0,
    20,
    1
)

is_student = st.checkbox("Are you a student?")


st.header("3️⃣ Button")

if st.button("Dilshad"):
    st.success("Information submitted successfully!")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Experience:", experience)

st.divider()

st.header("4️⃣ File Uploader")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.write("Preview of uploaded data:")

    st.dataframe(df)

st.divider()

st.header("5️⃣ Columns")

col1, col2, col3, value = st.columns(4)

with col1:
    st.metric("Total Students", 100)

with col2:
    st.metric("Average Age", 25)

with col3:
    st.metric("Pass Percentage", "92%")
with value:
    st.metric("Fail Percentage", "35%")


st.divider()

st.header("6️⃣ Tabs")

tab1, tab2, tab3 = st.tabs(
    ["Student", "Course", "Result"]
)

with tab1:
    st.write("Student Information")

with tab2:
    st.write("Course Information")

with tab3:
    st.write("Result Information")

st.divider()

st.header("7️⃣ Expander")

with st.expander("Click here to see more information"):
    st.write(
        "This content is hidden inside an expander."
    )

st.divider()

st.header("8️⃣ Status Messages")

st.success("Success message")

st.info("Information message")

st.warning("Warning message")

st.error("Error message")


st.divider()

st.header("🔟 Spinner")

with st.spinner("Processing..."):
    import time
    time.sleep(2)

st.success("Processing completed!")

st.divider()

st.header("1️⃣1️⃣ Display Image")

st.image('BFly.jpeg')
st.write(
    "You can display images using st.image()."
)

st.divider()


st.markdown("This text is normal, but this is :red[colored red]!")
st.write("You can also make text :blue[bold and blue] by wrapping it.")
st.header("Rainbow headings look like this: :rainbow[My Rainbow Title]")


st.markdown("Status: :green-badge[Completed] or :orange-badge[In Progress]")

st.header("🎉 End of Demonstration")

st.success(
    "This application demonstrates the major Streamlit widgets and functions."
)

