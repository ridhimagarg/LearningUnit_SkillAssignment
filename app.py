from unittest import result
import streamlit as st
from predict import *

st.title("Skill Assignment!")


st.subheader("Model")
selectbox = st.selectbox(
    "Select Model1 or Model2",
    ["Model1", "Model2"]
)
st.write(f"You selected {selectbox}")



st.subheader("Input")
desc = st.text_input('Learning Unit Description', 'Life of Brian')
st.write('The description is-: ', desc)

if st.button("Predict"):
    st.write("Skills assigned to this learning unit")
    if selectbox == "Model1":
        st.write("Model1 Running..")
        result = predictor1(desc)
        st.success('The output is {}'.format(result))
    elif selectbox =="Model2":
        st.write("Model2 running..")
        result = predictor2(desc)
        st.success('The output is {}'.format(result))


