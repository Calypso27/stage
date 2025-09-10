import streamlit as st
from src.queries import get_table_names, get_table_data

st.set_page_config(page_title="Dashboard SQL", layout="wide")
st.title("Tableau de bord")

try:
    tables = get_table_names()
    table_names = tables['TABLE_NAME'].tolist()

    selected_table = st.selectbox("Choisir une table", table_names)
    df = get_table_data(selected_table, limit=1000)

    st.dataframe(df)

except Exception as e:
    st.error(f"Erreur de connexion : {e}")
