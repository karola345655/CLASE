import streamlit as st

st.title("titulo")

col1,col2,col3= st.columns([4,4,2])

if col1.button("columna1"):
  st.write("columna1")

if col2.button("columna2"):
  st. write("worales")

if col3.button("columna3"):
  st.write("que chido wuju")
