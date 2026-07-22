import streamlit as st

def footer_home():
    st.markdown(f"""
                <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
                <h3>Created With ♥️ Avneesh Patel</h3>
                </div>
                """,unsafe_allow_html=True)
    