import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="COVID-19 Data Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 COVID-19 Data Visualization Dashboard")
st.write("Explore different types of charts using the COVID-19 dataset.")

df = pd.read_csv("Covid19.csv")

st.sidebar.header("Chart Selection")

graphs_list = [
    "Bar Chart",
    "Column Chart",
    "Line Chart",
    "Area Chart",
    "Pie Chart",
    "Scatter Plot",
    "Histogram",
    "Heatmap",
    "Box Plot"
]

user_choice = st.sidebar.selectbox(
    "Select a chart",
    graphs_list
)

if user_choice == "Bar Chart":

    st.header("📊 Age Distribution - Bar Chart")
    st.write("Comparison of the number of people belonging to different age groups.")

    age_count = df["Age"].value_counts().sort_index()

    st.bar_chart(
        age_count,
        color="#4CAF50"
    )

elif user_choice == "Column Chart":

    st.header("📊 COVID-19 Result Comparison")

    result_count = df["Covid_Result"].value_counts()

    st.bar_chart(
        result_count,
        color="#2196F3"
    )

elif user_choice == "Line Chart":

    st.header("📈 Age-wise COVID-19 Cases")

    age_count = df["Age"].value_counts().sort_index()

    st.line_chart(
        age_count,
        color="#FF5722"
    )

elif user_choice == "Area Chart":

    st.header("📈 Age-wise COVID-19 Distribution")

    age_count = df["Age"].value_counts().sort_index()

    st.area_chart(
        age_count,
        color="#9C27B0"
    )

elif user_choice == "Pie Chart":

    st.header("🥧 COVID-19 Result Distribution")

    result_count = df["Covid_Result"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        result_count,
        labels=result_count.index,
        autopct="%1.1f%%",
        colors=["#4CAF50", "#F44336"],
        startangle=90
    )

    ax.set_title(
        "COVID-19 Result Distribution",
        fontsize=14
    )

    st.pyplot(fig)

elif user_choice == "Scatter Plot":

    st.header("🔵 Age vs COVID-19 Result")

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="Age",
        y="Covid_Result",
        color="#E91E63",
        s=80,
        ax=ax
    )

    ax.set_title(
        "Relationship Between Age and COVID-19 Result",
        fontsize=14
    )

    st.pyplot(fig)

elif user_choice == "Histogram":

    st.header("📊 Age Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        data=df,
        x="Age",
        bins=10,
        kde=True,
        color="#00BCD4",
        ax=ax
    )

    ax.set_title(
        "Distribution of Age",
        fontsize=14
    )

    st.pyplot(fig)

elif user_choice == "Heatmap":

    st.header("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include="number")

    correlation = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(
        "Correlation Between Numerical Variables",
        fontsize=14
    )

    st.pyplot(fig)

elif user_choice == "Box Plot":

    st.header("📦 Age Distribution - Box Plot")

    fig, ax = plt.subplots()

    sns.boxplot(
        data=df,
        x="Age",
        color="#673AB7",
        ax=ax
    )

    ax.set_title(
        "Distribution and Spread of Age",
        fontsize=14
    )

    st.pyplot(fig)




