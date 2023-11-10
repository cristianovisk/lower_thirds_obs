import db
import streamlit as st
from control_obs import unhide_LowerThird, hide_LowerThird

def Control_Panel():
    spk = db.Manager_Speakers()
    ids = []
    for speaker in spk.get_Speakers():
        ids.append(f"{speaker.get('id')} - {speaker.get('name')}")
    
    try:
        option = st.selectbox("IDs", ids).split('-', 1)[0]
        data_speaker = spk.get_Speaker_by_ID(option)
        st.table(data_speaker)

        with st.form("Display"):
            if st.form_submit_button("Mostrar"):
                unhide_LowerThird(name=data_speaker[0].get('name'), subtitle=data_speaker[0].get('subtitle'))
            if st.form_submit_button("Ocultar"):
                hide_LowerThird(name=data_speaker[0].get('name'), subtitle=data_speaker[0].get('subtitle'))
    except:
        st.error('DATABASE EMPTY')
        
    