from matplotlib import pyplot as plt
import streamlit as st
from src.queries import get_full_schema

st.title("📋 Structure de la base de données")

schema_df = get_full_schema()
st.dataframe(schema_df, use_container_width=True)

