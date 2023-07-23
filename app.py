import numpy as np
import streamlit as st
from st_files_connection import FilesConnection

conn = st.experimental_connection('s3', type=FilesConnection)
filepath = 'amazon-reviews-pds/parquet/product_category=Software/'
filename = 'part-00000-495c48e6-96d6-4650-aa65-3c36a3516ddd.c000.snappy.parquet'
df = conn.read(f'{filepath}{filename}', input_format='parquet')
top20_most_reviewed_products = (
        df[['product_parent', 'review_id']]
        .groupby('product_parent')
        .count()
        .sort_values(by='review_id', ascending=False)
        .iloc[:20]
        .reset_index()
        .product_parent
        .unique()
)
df = df[df.product_parent.isin(top20_most_reviewed_products)]
product_parent = st.selectbox(label='Product', options=top20_most_reviewed_products)
df = df[df.product_parent==product_parent]
st.header(df.product_title.unique()[0])
star_rating = int(np.round(df[['star_rating']].mean().values[0], 0))
stars = ['⭑'] * star_rating
n_reviews = df['review_id'].count()
col0, col1 = st.columns(2)
with col0:
    st.title(''.join(stars))
with col1:
    st.text(f'{n_reviews} reviews')
st.dataframe(df[['star_rating', 'review_headline', 'review_body']], hide_index=True)
