import streamlit as st

# Balloons, for shit and giggles
st.balloons()

# Data file, from which we will read and write to
fname = "data_file.txt"

# Read the data file and show content
f = open(fname, "r")
data = f.readlines()
f.close()
st.write(data)

# Append a line to this data file
f = open(fname, "a")
f.write("This is a new line")
f.close()

# Read the data file again, and show content
f = open(fname, "r")
data = f.readlines()
f.close()
st.write(data)
