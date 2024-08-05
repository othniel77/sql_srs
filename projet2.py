# pylint : disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st


con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

#solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_stat WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

