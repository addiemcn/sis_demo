# Streamlit in Snowflake Demo App - VERSION 2.0
import streamlit as st
import pandas as pd

st.set_page_config(page_title="SIS + Git Demo", page_icon="❄️", layout="wide")

st.title("❄️ Streamlit in Snowflake")
st.subheader("Version 2.0 - Now with Data!")

st.success("✅ This update was deployed from Git!")

# Show metrics in columns
col1, col2, col3 = st.columns(3)
col1.metric("Deployment", "Git Integration", "Automated")
col2.metric("Version", "2.0", "+1.0")
col3.metric("Status", "Live", "Updated")

# Sample data visualization
st.divider()
st.subheader("📊 Sample Data")

data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Users': [100, 150, 200, 280, 350]
})

st.bar_chart(data.set_index('Month'))

st.caption("Powered by Streamlit in Snowflake + Git 🚀")


