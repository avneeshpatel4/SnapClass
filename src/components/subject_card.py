import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):

    html = f"""
<div style="background:white;border-left:8px solid #EB459E;padding:25px;border-radius:20px;border:1px solid #D1D5DB;margin-bottom:20px;box-shadow:0 2px 6px rgba(0,0,0,.08);">

<h3 style="margin:0;color:#1E293B;font-size:1.5rem;">
{name}
</h3>

<p style="color:black;margin:10px 0 18px 0;font-size:16px;">
Code
<span style="background:#E0E3FF;color:#5865F2;padding:2px 8px;border-radius:5px;font-weight:600;">
{code} 
</span>  
<b style="color: black;"> | Section: {section}</b>
</p>
"""

    if stats:
        html += '<div style="display:flex;gap:8px;flex-wrap:wrap;">'

        for icon, label, value in stats:
            html += f"""
<div style="background:#EB459E1;color: black;padding:6px 12px;border-radius:12px;font-size:.9rem;">
{icon} <b>{value}</b> {label}
</div>
"""

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()