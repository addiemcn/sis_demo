# Streamlit in Snowflake Demo App
import streamlit as st

st.set_page_config(page_title="SIS + Git Demo", page_icon="❄️")

st.title("❄️ Streamlit in Snowflake")
st.subheader("Version 1.0")

st.write("This app was deployed from GitHub!")

st.metric(label="Deployment Method", value="Git Integration")

