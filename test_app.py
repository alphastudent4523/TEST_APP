import streamlit as st
import project_test
        

def predict(N,P,K,temperature,humidity,ph,rainfall):
    return project_test.calc_main(N,P,K,temperature,humidity,ph,rainfall)

st.set_page_config(
    page_title="CROP RECOMMENDATION SYSTEM",
    layout="wide",
)


# Title with potentially custom styling
st.markdown(
    "<h1 style='text-align: center; color: #3F51B5; font-size: 36px;'>CROP RECOMMENDATION SYSTEM</h1>",
    unsafe_allow_html=True,
)

# Metrics section (replace placeholders with actual data)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Investment", "$2,482,205,481")
col2.metric("Most Frequent", "$847,300")
col3.metric("Average", "$4,964,411")
col4.metric("Central Earnings", "$2,593,682")

# Filter section with dropdown menus (adjust options as needed)
st.subheader('Enter The Details')
nitrogen_select = st.number_input('Nitrogen Level', step=0.1)
phosphorous_select = st.number_input('Phosphorous Level', step=0.1)
pottasium_select = st.number_input('Pottasium Level', step=0.1)
temperature_select=st.number_input("Temperature", step=0.1)
humidity_select=st.number_input("humidity", step=0.1)
pH_select=st.number_input("pH", step=0.1)
Rainfall_select=st.number_input("Rainfall", step=0.1)

if st.button('Confirm'):
    prediction=str(predict(nitrogen_select,phosphorous_select,pottasium_select,temperature_select,humidity_select,pH_select,Rainfall_select))
    # Progress section with customization options (replace with actual progress value)
    st.subheader('The Suitable Crop')
    # Placeholder for charts section (replace with your charting library and data)
    st.markdown(f'<img src="https://cdn.icon-icons.com/icons2/2930/PNG/512/sprout_leaf_plant_agriculture_ground_icon_183627.png" width="48" height="48"> {prediction}',unsafe_allow_html=True)


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

