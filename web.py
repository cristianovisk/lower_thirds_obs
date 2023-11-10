import streamlit as st
import db
from Pages.Controle.Dash import Control_Panel
from Pages.Controle.Incluir import Insert_Host as PageIncluirHost
from Pages.Controle.Deletar import Delete_Host as PageDeleteHost
from Pages.Controle.Consultar import List_Hosts as PageConsultarHosts

spk = db.Manager_Speakers()

# st.title('OWASP Fortaleza')
st.image(image="https://owasp.org/www-chapter-fortaleza/assets/images/Logo_OWASP_Fortaleza.png")
st.sidebar.title("Hosts")
option = st.sidebar.selectbox("Ação", ["Controle", "Consultar", "Incluir", "Deletar"])

if option == "Incluir":
    PageIncluirHost()
elif option == "Consultar":
    PageConsultarHosts()
elif option == "Deletar":
    PageDeleteHost()
elif option == "Controle":
    Control_Panel()