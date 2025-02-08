import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000"

# Streamlit app
st.title("World Population Statistics")

# Fetch all continents
response = requests.get(f"{FASTAPI_URL}/continents/")
if response.status_code == 200:
    continents = response.json().get("continents", [])
else:
    st.error("Failed to fetch continents")
    continents = []

# Dropdown to select a continent
selected_continent = st.selectbox("Select a Continent", continents)

if selected_continent:
    # Fetch statistics for the selected continent
    response = requests.get(f"{FASTAPI_URL}/continents/{selected_continent}/")
    
    if response.status_code == 200:
        continent_data = response.json()
        st.subheader(f"Statistics for {selected_continent}")

        # Check if 'statistics' is in response
        statistics = continent_data.get("statistics", {})
        if statistics:
            st.write(f"**Total Countries:** {statistics.get('Total_Countries', 'N/A')}")
            st.write(f"**Total Population:** {statistics.get('Total_Population', 'N/A')}")
            st.write(f"**Average Population:** {statistics.get('Average_Population', 'N/A')}")
            st.write(f"**Total Area:** {statistics.get('Total_Area', 'N/A')}")
            st.write(f"**Max Population:** {statistics.get('max_population', 'N/A')}")
            st.write(f"**Min Population:** {statistics.get('min_population', 'N/A')}")
            st.write(f"**Country with Max Population:** {statistics.get('Country_Max_Population', 'N/A')}")
            st.write(f"**Country with Min Population:** {statistics.get('Country_Min_Population', 'N/A')}")
            st.write(f"**Population Density:** {statistics.get('Population_Density', 'N/A')}")
        else:
            st.error("No statistics found for this continent.")
    else:
        st.error(f"Failed to fetch statistics for {selected_continent}")

# Option to view a specific statistic
if statistics:
    stat_options = list(statistics.keys())
    selected_stat = st.selectbox("Select a specific statistic to view", stat_options)
    st.write(f"**{selected_stat}:** {statistics.get(selected_stat, 'N/A')}")
