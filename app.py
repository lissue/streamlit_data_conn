import streamlit as st
from st_files_connection import FilesConnection

conn = st.experimental_connection('s3', type=FilesConnection)
#data = conn.read('amazon-reviews-pds/tsv/index.txt', input_format='text')
data = conn.read('amazon-reviews-pds/parquet/product_category=Software/part-00000-495c48e6-96d6-4650-aa65-3c36a3516ddd.c000.snappy.parquet', input_format='parquet')
st.write(data)
