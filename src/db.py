import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_db_config():
    # Essaye d'abord secrets.toml
    try:
        if "SERVER_NAME" in st.secrets:
            return st.secrets
    except Exception:
        pass

    # Sinon .env
    return {
        "SERVER_NAME": os.getenv("SERVER_NAME"),
        "DATA_NAME": os.getenv("DATA_NAME"),
        "UID": os.getenv("UID"),
        "PASSWORD": os.getenv("PASSWORD"),
        "PORT": os.getenv("PORT", "1433")
    }

def connect():
    config = get_db_config()

    username = config["UID"]
    password = config["PASSWORD"]
    server = config["SERVER_NAME"]
    port = config["PORT"]
    database = config["DATA_NAME"]

    connection_url = (
        f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    return create_engine(connection_url)
