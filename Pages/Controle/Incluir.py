import db
import streamlit as st

def Insert_Host():
    spk = db.Manager_Speakers()
    with st.form("include_host"):
        st.write("Dados do Host")
        name = st.text_input("Nome:")
        subtitle = st.text_input("Função:")
        if len(name) > 22:
            st.write('Campo nome grande de mais (max 22)')
        if len(subtitle) > 43:
            st.write('Campo subtitle grande de mais (max 43)')
        st.form_submit_button("Cadastrar")
        
        if name != "" and subtitle != "":
            spk.insert_Speaker(name=name, subtitle=subtitle)