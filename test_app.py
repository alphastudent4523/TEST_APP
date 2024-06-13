import streamlit as st
import pandas as pd
import plotly.express as px

# Layout configuration (adjust as needed)
st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide",
)


# Sample data: Trends in farming in India (replace this with actual data)
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Crop Production (in million tons)": [250, 260, 270, 280, 290, 300, 310, 320, 330]
}

df = pd.DataFrame(data)

# Create a line chart using Plotly
fig = px.line(df, x="Year", y="Crop Production (in million tons)",
              title="Trends in Farming in India")

# Display the graph at the top of the app
st.plotly_chart(fig)


# Title with potentially custom styling
st.markdown(
    "<h1 style='text-align: center; color: #3F51B5; font-size: 36px;'>My Financial WorkBook</h1>",
    unsafe_allow_html=True,
)

# Title with potentially custom styling
st.markdown(
    "<h1 style='text-align: center; color: #3F51B5; font-size: 36px;'>My Financial WorkBook</h1>",
    unsafe_allow_html=True,
)

# Metrics section (replace placeholders with actual data)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Investment", "$2,482,205,481")
col2.metric("Most Frequent", "$847,300")
col3.metric("Average", "$4,964,411")
col4.metric("Central Earnings", "$2,593,682")

# Filter section with dropdown menus (adjust options as needed)
number_label = "Enter a number (between 1 and 10):"
selected_number = st.number_input(number_label, min_value=1, max_value=10, value=5)
st.subheader('Please Filter')
nitrogen_select = st.selectbox('Select Region', ('Elist Midwest', 'Northeast'))
phosphorous_select = st.selectbox('Select Location', ('Farming', 'Office Bldg'))
pottasium_select = st.multiselect('Select Construction', ('Rebar', 'Masonry', 'Metal Clad'))

# Progress section with customization options (replace with actual progress value)
st.subheader('Progress')
progress_value = 0.7  # Replace with actual progress (0.0 to 1.0)
st.progress(progress_value)
st.write(f"Progress: {int(progress_value * 100)}%")  # Display percentage value

# Placeholder for charts section (replace with your charting library and data)
st.write('Charts Here!')

# Navigation section with potentially custom styling
st.sidebar.markdown(
    "<h3 style='text-align: center; color: #3F51B5; font-size: 24px;'>Main Menu</h3>",
    unsafe_allow_html=True,
)
st.sidebar.button("Home")
st.sidebar.button("State")
st.sidebar.button("Investment")
st.sidebar.button("Progress")
st.sidebar.button("Manage App")
st.sidebar.button("Search")

# Additional CSS customization (optional)
# You can include a separate CSS file or add custom styling within the Streamlit app
# For example, to change background color:
# st.write('<style>body { background-color: #F0F2F5; }</style>', unsafe_allow_html=True)
