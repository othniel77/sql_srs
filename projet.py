import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to be review?",
        ("Join","Group By","Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )

    st.write('You selected:', option)

data = {"a": [1, 2, 3], "b":[4, 5, 6]}
lait = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["cat", "dog", "owl"])

with tab1:
    sql_query = st.text_area(label="entrez votre input")
    result = duckdb.query(sql_query).df()
    st.write(f"Vous avez entré la query suivante: {sql_query}")
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)