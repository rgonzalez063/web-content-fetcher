import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlit app title
st.title("Web Content Fetcher")

# Input for URL
url = st.text_input("Enter a URL to fetch its content:")

if url:
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main content (e.g., body text)
        main_content = soup.get_text()

        # Display the content
        st.subheader("Content:")
        st.text_area("Fetched Content", main_content, height=400)
    except Exception as e:
        st.error(f"An error occurred: {e}")