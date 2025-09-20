import streamlit as st 
from views import about_me, fraud_detection, analysis

# Set Streamlit page configuration (Title, favicon, layout)
st.set_page_config(page_title="Healthcare Claims Fraud Detection App", page_icon="💼", layout="wide")


# --- PAGE SETUP ---
PAGES = {
    "Health Claims Fraud Detection": fraud_detection,
  "Data Analysis": analysis,
    "About Me": about_me
}

# Sidebar Section for Navigation first
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to", list(PAGES.keys()))

    st.title("Contact Me")
    st.write("📧 Email: [atif738738@gmail.com](mailto:atif738738@gmail.com)")

    st.write("🔗 LinkedIn: [Atif](https://www.linkedin.com/in/atif-raja-570853275?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    
# Load the selected page function
page = PAGES[selection]
page.app()  # Call the app function from the selected module 

