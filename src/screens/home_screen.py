import streamlit as st
from pathlib import Path

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    teacher_img = Path("assets") / "Teacher.jpeg"
    student_img = Path("assets") / "Student.jpeg"

    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm Student")
        if student_img.exists():
            st.image(str(student_img), width=120)
        else:
            st.error("Student image not found!")

        if st.button("Student Portal",type="primary", icon=':material/arrow_outward:',icon_position='right'):
            st.session_state["login_type"] = "student"
            st.rerun()
            


    with col2:
        st.header("I'm Teacher")
        if teacher_img.exists():
            st.image(str(teacher_img), width=145)
        else:
            st.error("Teacher image not found!")

        if st.button("Teacher Portal",type="primary", icon=':material/arrow_outward:',icon_position='right'):
            st.session_state["login_type"] = "teacher"
            st.rerun()
    
    footer_home()    