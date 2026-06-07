import streamlit as st
import backend as bk
st.title("GENERATIVE AI PROJECT")
input= st.text_input("Type your query here")
button=st.button("Go")
if button:
    st.info("query submitted") 
    with st.spinner(" Searching... Please wait"):
        out=bk.get_text_output(input)
    st.write(out)
    st.success("successfully fetched the answer")

   
    

