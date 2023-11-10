import db
import streamlit as st

def List_Hosts():
    spk = db.Manager_Speakers()
    st.table(spk.get_Speakers())