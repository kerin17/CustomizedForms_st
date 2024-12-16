import streamlit as st
import time

# caching to save time and in case of large data import
@st.cache_data(ttl=60)  # Cache this data for 60 seconds
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3)  # Delays to mimic an API call
    return {"data": "This is cached data!"} #returning immutable data

st.write("Fetching data...")
data = fetch_data()
st.write(data)


##############



file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    # Open the file in append mode, which creates the file if it doesn't exist
    file = open(file_path, "a+")
    return file

# Use the cached file handler
file_handler = get_file_handler()

# Write to the file using the cached handler
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush()  # Ensure the content is written immediately
    st.success("Wrote a new line to the file!")

# Read and display the file contents
if st.button("Read File"):
    file_handler.seek(0)  # Move to the beginning of the file
    content = file_handler.read()
    st.text(content)
