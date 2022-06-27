import streamlit as st

def a_propos():
    
    st.title('À propos')
    col1, col2 = st.columns(2)
    with col1:
        st.title('Le projet')
        st.write('blabla')

    with col2:
        st.title('Vie privée')
        st.write('L\'application collecte des données personnelles dans le but d\'offrir un classement des différents utilisateurs.')
        st.write('Le fichier ZIP importé comprend différentes données personnelles. Les seules données personnelles stockées par l\'application sont : nom, prénom et somme des dépenses sur l\'année 2021.')
        st.write('Si vous avez fait le choix de participer au classement et que vous souhaitez ne plus y apparaître, vous pouvez contacter Lilou Roger ou Yann Vanden Broeck sur le Slack ESDESP.')
