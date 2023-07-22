import streamlit as st
from st_files_connection import FilesConnection

conn = st.experimental_connection('s3', type=FilesConnection)
data = conn.read('amazon-reviews-pds/tsv/index.txt', input_format='text')
st.write(data)
