import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# ---------------------------
# Load Data
# ---------------------------
data = {
    "Name": [
        "Harsh Atul Pardeshi", "Virag Nitin Borikar", "Rushikesh Sanjiv Awatare",
        "Suryawanshi Gauri Vijay", "Payal Narayan Wakle", "Durgesh Ramesh Hyalij",
        "Nayan Ganorkar", "Harsh Atul Pardeshi", "Virag Nitin Borikar"
    ],
    "Nickname": [
        "ThunderDetective33", "ThunderSkier07", "FrostAstronaut21",
        "WindPilot22", "StormAstronomer20", "ThunderAstronaut44",
        "GO-HV09P", "ThunderDetective34", "ThunderSkier08"
    ],
    "Observations": [2, 9, 5, 24, 6, 10, 16, 2, 6],
    "Matches": [1, 7, 4, 19, 6, 7, 9, 1, 2],
    "Observation Link": [
        "https://observer.globe.gov/myobservations/?userid=137464162",
        "https://observer.globe.gov/myobservations/?userid=137927592",
        "https://observer.globe.gov/myobservations/?userid=137464212",
        "https://observer.globe.gov/myobservations/?userid=137464180",
        "https://observer.globe.gov/myobservations/?userid=137464200",
        "https://observer.globe.gov/myobservations/?userid=137466631",
        "https://observer.globe.gov/myobservations/?userid=138844242",
        "https://observer.globe.gov/myobservations/?userid=137461895",
        "https://observer.globe.gov/myobservations/?userid=134855542"
    ],
    "Latitude": [20.333, 20.334, 20.336, 20.331, 20.330, 20.332, 20.338, 20.335, 20.337],
    "Longitude": [74.244, 74.243, 74.245, 74.241, 74.240, 74.246, 74.248, 74.247, 74.249]
}

df = pd.DataFrame(data)

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="GLOBE Observations Dashboard", layout="wide")

st.title("🌎 GLOBE Student Observations Dashboard")
st.subheader("By SE/TE Students | 2025")

# ---------------------------
# Sidebar Search
# ---------------------------
search_name = st.sidebar.text_input("🔍 Search by Name")

# Filter
filtered_df = df[df['Name'].str.contains(search_name, case=False)] if search_name else df

# ---------------------------
# Show Student Cards
# ---------------------------
st.header("👩‍🎓 Student Observations")

for idx, row in filtered_df.iterrows():
    with st.container():
        st.markdown(f"""
        ### {row['Name']} ({row['Nickname']})
        - **Observations:** {row['Observations']}
        - **NASA Satellite Matches:** {row['Matches']}
        - [🔗 View Observations]({row['Observation Link']})
        """)
        st.markdown("---")

# ---------------------------
# Graphs Section
# ---------------------------
st.header("📊 Graphs")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(filtered_df, x="Name", y="Observations", color="Observations",
                  title="Number of Observations", height=400)
    fig1.update_layout(xaxis={'categoryorder': 'total descending'}, showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(filtered_df, x="Name", y="Matches", color="Matches",
                  title="Number of Satellite Matches", height=400)
    fig2.update_layout(xaxis={'categoryorder': 'total descending'}, showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Map Section
# ---------------------------
st.header("🗺️ Observation Map")

m = folium.Map(location=[20.333, 74.244], zoom_start=12)

for idx, row in filtered_df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Name']}<br>Observations: {row['Observations']}"
    ).add_to(m)

st_data = st_folium(m, width=1200)

# ---------------------------
# Footer
# ---------------------------
st.write("---")
st.write("🚀 Developed with ❤️ by Durgesh Hyalij")
