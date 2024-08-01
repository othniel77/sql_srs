import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")


option = st.selectbox(
    "What would you like to be review?",
    ("Join","Group By","Windows Functions"),
    index=None,
    placeholder="Select a theme...",
)

st.write('You selected:', option)
tab1, tab2, tab3 = st.tabs(["cat", "dog", "owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
