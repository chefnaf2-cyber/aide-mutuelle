import streamlit as st

# --- DESIGN DU TITRE ---
st.markdown("<h1 style='text-align: center; color: #FFD700; text-shadow: 2px 2px #000000;'>🤝 AIDE MUTUELLE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'><b>L'union fait la force - Niger</b></p>", unsafe_allow_html=True)

# --- MENU DE NAVIGATION ---
menu = st.sidebar.radio("Menu principal", ["Inscription & Parrainage", "Investir (Packs)", "Suivi de mon Cycle"])

if menu == "Inscription & Parrainage":
    st.subheader("📝 Créer mon compte")
    nom = st.text_input("Nom complet")
    tel = st.text_input("Numéro Airtel Money")
    code_p = st.text_input("Code de parrainage (Optionnel)")
    if st.button("S'inscrire"):
        if nom and tel:
            st.success(f"Félicitations {nom} ! Inscription réussie.")
        else:
            st.error("Veuillez remplir votre nom et votre numéro.")

elif menu == "Investir (Packs)":
    st.subheader("💎 Choisissez votre Pack d'investissement")
    pack = st.selectbox("Sélectionnez votre pack :", ["Bronze (5 000 FCFA)", "Argent (10 000 FCFA)", "Or (20 000 FCFA)"])
    
    # Calcul des gains selon le pack
    montant = 5000 if "Bronze" in pack else 10000 if "Argent" in pack else 20000
    gain_net = int(montant * 0.8) # 4000 pour 5000 après gaz
    
    st.info(f"Pack choisi : {pack}")
    st.write(f"✅ Vous recevrez **2 retraits de {gain_net} FCFA**.")
    st.write(f"⛽ Frais de gaz : {int(montant * 0.2)} FCFA par retrait.")
    
    st.warning(f"📲 Envoyez votre dépôt au numéro Airtel : **[TON NUMÉRO ICI]**")
    st.file_uploader("Envoyez la capture d'écran de votre transfert", type=["png", "jpg", "jpeg"])
    
    if st.button("Valider mon investissement"):
        st.success("Preuve envoyée ! Lulu va vérifier et vous coupler sous peu.")

elif menu == "Suivi de mon Cycle":
    st.subheader("📊 État du compte")
    st.info("Une fois couplé, vous verrez votre chrono de 14 jours ici.")