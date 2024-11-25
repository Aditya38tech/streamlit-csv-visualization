import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("CSV Data Visualization")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show the data
    st.subheader("Data Preview")
    st.write(df.head())

    # Basic Statistics
    st.subheader("Data Summary")
    st.write(df.describe())

    # Select plot type
    plot_type = st.selectbox("Choose a plot type", ["Line Chart", "Bar Chart", "Histogram"])

    if plot_type == "Line Chart":
        # Line chart
        st.subheader("Line Chart")
        selected_columns = st.multiselect("Select columns for the line chart", df.columns)
        if len(selected_columns) > 0:
            st.line_chart(df[selected_columns])

    elif plot_type == "Bar Chart":
        # Bar chart
        st.subheader("Bar Chart")
        selected_columns = st.multiselect("Select columns for the bar chart", df.columns)
        if len(selected_columns) > 0:
            st.bar_chart(df[selected_columns])

    elif plot_type == "Histogram":
        # Histogram
        st.subheader("Histogram")
        selected_column = st.selectbox("Select column for the histogram", df.columns)
        if selected_column:
            st.write(df[selected_column].hist(bins=20))
            plt.show()
            st.pyplot()
