import os
import streamlit as st
from datarobot_connection.connection import DataRobotConnection

conn = st.experimental_connection(
    'datarobot',
    type=DataRobotConnection,
)
options = ['datasets', 'projects', 'deployments']
query = st.selectbox('Asset type', options)
st.dataframe(conn.query(query))
