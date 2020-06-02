import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column,String,Integer,Float
import pandas as pd
from database import Products

# connect to database
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

# data base code ends

st.title("Welcome to Product inventory adder")
name = st.text_input('product name')
price = st.number_input('product price')
brand = st.text_input('product brand')

if st.button("save") and name and price and brand:
    with st.spinner("saving..."):
        product = Products(name=name, price=price, brand=brand)
        sess.add(product)
        sess.commit()
        st.success("saved to database")
else:
    st.error("error")

op = st.checkbox("show products from database")
if op:
    df = pd.read_sql('products',engine)
    st.write(df)



