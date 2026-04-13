import streamlit as st
from datetime import datetime, timedelta

# Configuration du site
st.set_page_config(page_title="Mutuelle Niger", page_icon="🤝")

# Style Jaune Niger
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 15px; background-color: #FFD700; color: black; font-weight: bold; }
    .title { text-align: center; color: #FFD700; font-size: 35px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title'>MUTUELLE NIGER</div>", unsafe_allow_html=True)

# Mémoire de l'application
if 'membres' not in st.session_state: st.session_state.membres = {}
if 'file_attente' not in st.session_state: st.session_state.file_attente = []

# Menu de navigation
choix_menu = st.sidebar.radio("Navigation", ["Inscription", "Mon Espace Personnel", "Validation"])

if choix_menu == "Inscription":
    st.info("💸 Faites votre dépôt Airtel Money au : **+227 89 06 28 06**")
    with st.form("inscription"):
        nom = st.text_input("Nom et Prénom")
        tel = st.text_input("Numéro Airtel Money")
        mdp = st.text_input("Créez votre mot de passe", type="password")
        valider = st.form_submit_button("VALIDER MON INSCRIPTION")
        
        if valider:
            if nom and tel and mdp:
                st.session_state.membres[tel] = {"nom": nom, "mdp": mdp, "date": datetime.now(), "statut": "En attente"}
                if len(st.session_state.file_attente) > 0:
                    partenaire = st.session_state.file_attente.pop(0)
                    st.session_state.membres[tel]["statut"] = "Couplé"
                    st.session_state.membres[partenaire]["statut"] = "Couplé"
                    st.success("Couplage réussi ! Bienvenue dans la mutuelle.")
                else:
                    st.session_state.file_attente.append(tel)
                    st.info("Dépôt reçu. Le système vous couplera bientôt.")
            else:
                st.error("Veuillez remplir toutes les cases.")

elif choix_menu == "Mon Espace Personnel":
    tel_log = st.text_input("Votre Numéro Airtel")
    mdp_log = st.text_input("Votre Mot de passe", type="password")
    if tel_log in st.session_state.membres and st.session_state.membres[tel_log]["mdp"] == mdp_log:
        user = st.session_state.membres[tel_log]
        st.write(f"### Bonjour {user['nom']} !")
        st.write(f"État de votre compte : **{user['statut']}**")
        date_r = user["date"] + timedelta(days=14)
        if datetime.now() >= date_r and user["statut"] == "Couplé":
            st.success("💰 Votre gain de 4 000 FCFA est prêt !")
            if st.button("DEMANDER MON RETRAIT MAINTENANT"):
                st.info("Demande de retrait envoyée avec succès.")
        else:
            st.write(f"Prochain retrait disponible le : {date_r.strftime('%d/%m/%Y')}")

elif choix_menu == "Validation":
    st.title("Espace Administration")
    st.write("Section réservée à la validation des nouveaux membres.")