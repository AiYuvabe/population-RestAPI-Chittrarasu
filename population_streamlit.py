# import streamlit as st
# import requests

# BASE_URL = "http://127.0.0.1:8000"  # Update with your FastAPI server URL 

# st.title("World Population")

# # Fetch all continents
# response = requests.get(f"{BASE_URL}/continents/")
# if response.status_code == 200:
#     continents = response.json()["continents"]
# else:
#     st.error("Failed to fetch continents")
#     continents = []

# selected_continent = st.selectbox("Select a continent:", continents)

# if selected_continent:
#     stat = st.text_input("Enter a statistic to fetch (optional):")

#     url = f"{BASE_URL}/continents/{selected_continent}/"
#     if stat:
#         url += f"?stat={stat}"

#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         st.json(data)
#     else:
#         st.error("Failed to fetch data")

#DEEPSEEK

import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000"

# Streamlit app
# def main():
st.title("World Population Statistics")

    # Fetch all continents
response = requests.get(f"{FASTAPI_URL}/continents/")
if response.status_code == 200:
    continents = response.json()["continents"]
else:
    st.error("Failed to fetch continents")
    

    # Dropdown to select a continent
selected_continent = st.selectbox("Select a Continent", continents)

    # Fetch statistics for the selected continent
response = requests.get(f"{FASTAPI_URL}/continents/{selected_continent}/")
if response.status_code == 200:
    continent_stats = response.json()
else:
    st.error(f"Failed to fetch statistics for {selected_continent}")
        

    # Display the statistics
st.subheader(f"Statistics for {selected_continent}")
st.write(f"**Total Countries:** {continent_stats['Total_Countries']}")
st.write(f"**Total Population:** {continent_stats['Total_Population']}")
st.write(f"**Average Population:** {continent_stats['Average_Population']}")
st.write(f"**Total Area:** {continent_stats['Total_Area']}")
st.write(f"**Max Population:** {continent_stats['max_population']}")
st.write(f"**Min Population:** {continent_stats['min_population']}")
st.write(f"**Country with Max Population:** {continent_stats['Country_Max_Population']}")
st.write(f"**Country with Min Population:** {continent_stats['Country_Min_Population']}")
st.write(f"**Population Density:** {continent_stats['Population_Density']}")

    # Option to view a specific statistic
stat_options = list(continent_stats.keys())
selected_stat = st.selectbox("Select a specific statistic to view", stat_options)
st.write(f"**{selected_stat}:** {continent_stats[selected_stat]}")

# if __name__ == "__main__":
#     main()