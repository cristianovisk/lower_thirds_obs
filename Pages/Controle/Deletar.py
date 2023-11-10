import db
import streamlit as st

def Delete_Host():
    spk = db.Manager_Speakers()
    with st.form("include_host"):
        
        id_host = st.text_input("ID do Host:")
        st.form_submit_button("Deletar")
        spk.delete_Speaker(id=id_host)