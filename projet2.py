# pylint : disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st




con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with (st.sidebar):
    available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()

    theme = st.selectbox(
        "What would you like to review?",
        available_themes_df["theme"].unique(),
        index=None,
        placeholder="Select a theme...",
    )
    if theme:
        st.write("You selected:", theme)
        exercise = (
            con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
            .df()
            .sort_values("last_reviewed").
            reset_index()
        )
    else:
        exercise = (
            con.execute(f"SELECT * FROM memory_state")
            .df()
            .sort_values("last_reviewed").
            reset_index()
        )
    st.write(exercise)
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answer/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution_df"
        )



tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.write(answer)