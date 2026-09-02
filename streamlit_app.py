import streamlit as st

st.balloons()

fname = "data_file.txt"
f = open(fname, "r")
data = f.readlines()
f.close()

st.write(data)
