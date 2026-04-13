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

# Mémoire du robot
if 'membres' not in st.session_state:
    st.session_state.membres = {}
if 'file_attente' not in st.session_state:
    st.session_state.file_attente = []
if 'alertes_retrait' not in st.session_state:
    st.session_state.alertes_retrait = []

st.markdown("<div class='title'>MUTUELLE NIGER</div>", unsafe_allow_html=True)

# Menu sur le côté
choix_menu = st.sidebar.radio("Navigation", ["Inscription", "Mon Espace Personnel", "Espace de Validation 🔐"])

# --- PARTIE INSCRIPTION ---
if choix_menu == "Inscription":
    st.info("💸 Faites votre dépôt Airtel Money au : **+227 89 06 28 06**")
    with st.form("formulaire_inscription"):
        nom_complet = st.text_input("Nom et Prénom")
        numero_tel = st.text_input("Numéro Airtel Money")
        mot_de_passe = st.text_input("Créez votre mot de passe", type="password")
        preuve_photo = st.file_uploader("Capture d'écran du transfert", type=["jpg", "png"])
        
        bouton_valider = st.form_submit_button("VALIDER MON INSCRIPTION")
        
        if bouton_valider:
            if nom_complet and numero_tel and mot_de_passe and preuve_photo:
                st.session_state.membres[numero_tel] = {
                    "nom": nom_complet, "mdp": mot_de_passe, "statut": "En attente", 
                    "date_inscription": datetime.now(), "nombre_retraits": 0
                }
                if len(st.session_state.file_attente) > 0:
                    partenaire = st.session_state.file_attente.pop(0)
                    st.session_state.membres[numero_tel]["statut"] = "Couplé"
                    st.session_state.membres[partenaire]["statut"] = "Couplé"
                    st.balloons()
                    st.success("Couplage réussi ! Bienvenue.")
                else:
                    st.session_state.file_attente.append(numero_tel)
                    st.info("Dépôt reçu. Le robot vous couplera bientôt.")
            else:
                st.error("Veuillez remplir toutes les cases.")

# --- PARTIE MON ESPACE ---
elif choix_menu == "Mon Espace Personnel":
    entrer_tel = st.text_input("Votre Numéro Airtel")
    entrer_mdp = st.text_input("Votre Mot de Passe", type="password")
    
    if entrer_tel in st.session_state.membres and st.session_state.membres[entrer_tel]["mdp"] == entrer_mdp:
        utilisateur = st.session_state.membres[entrer_tel]
        st.write(f"### Bonjour {utilisateur['nom']}")
        st.write(f"État du compte : **{utilisateur['statut']}**")
        
        # Calcul des 14 jours
        date_retrait = utilisateur["date_inscription"] + timedelta(days=14)
        
        if datetime.now() >= date_retrait and utilisateur["statut"] == "Couplé" and utilisateur["nombre_retraits"] < 2:
            st.success("💰 Votre gain de 4 000 FCFA est prêt !")
            if st.button("DEMANDER MON RETRAIT MAINTENANT"):
                st.session_state.alertes_retrait.append({"nom": utilisateur["nom"], "tel": entrer_tel})
                st.info("Demande envoyée au système.")
        else:
            if utilisateur["nombre_retraits"] >= 2:
                st.warning("Cycle terminé. Veuillez réinvestir.")
            else:
                st.write(f"Retrait disponible le : {date_retrait.strftime('%d/%m/%Y')}")

# --- PARTIE VALIDATION ---
elif choix_menu == "Espace de Validation 🔐":
    code_admin = st.text_input("Entrez votre code secret", type="password")
    if code_admin == "Ch1987":
        st.write("### Retraits en attente")
        if st.session_state.alertes_retrait:
            for index, alerte in enumerate(st.session_state.alertes_retrait):
                st.write(f"⚠️ **{alerte['nom']}** ({alerte['tel']})")
                if st.button(f"Confirmer le paiement pour {alerte['nom']}", key=index):
                    st.session_state.membres[alerte['tel']]["nombre_retraits"] += 1
                    st.session_state.alertes_retrait.pop(index)
                    st.success("Paiement validé !")
        else:
            st.write("Rien à valider pour le moment.")o
u