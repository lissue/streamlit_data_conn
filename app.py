import os
import glob
import pandas as pd
import streamlit as st
from datetime import date
from datarobot_connection.connection import DataRobotConnection

conn = st.experimental_connection(
    'datarobot',
    type=DataRobotConnection,
)
col0, col1 = st.columns(2)
with col0:
    options = ['datasets', 'projects', 'deployments']
    query = st.selectbox('Asset type', options)
    df_query = conn.query(query).set_index('ID')
with col1:
    files = glob.glob(f'./records/{query}_*.csv')
    if len(files) > 0:
        select_record = st.selectbox('Record', files)
        df_record = pd.read_csv(select_record).set_index('ID')
        df = df_query.join(df_record[['Organization']]).reset_index()
    else:
        df = df_query.reset_index()
        df['Organization'] = None
edited_df = st.data_editor(df)
if st.button('Save'):
    edited_df.to_csv(f'./records/{query}_{date.today()}.csv')
