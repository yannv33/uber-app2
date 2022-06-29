import streamlit as st

def a_propos():
    
    st.title('À propos')
    col1, col2 = st.columns(2)
    with col1:
        st.title('Le projet')
        st.write(' ')
        st.write('Le projet naît d’une simple interrogation lors d’un cours à l’ESD entre deux étudiants, Yann Vanden Broeck et Lilou Roger : combien ai-je dépensé cette année sur Uber Eats ? C’est alors que nous nous sommes lancé le défi de trouver cette information ! ')
        st.write('Malheureusement sur l’application elle n’est pas accessible facilement. Pour cela nous avons utilisé les données Uber, accessibles grâce au droit d’accès offert par le RGPD et après quelques sueurs froides à la vue des montants astronomiques que nous avions dépensé, nous avons pris la décision de partager cette découverte à notre classe.')
        st.write('Le but de ce site codé avec Streamlit et Python est de rendre l’expérience accessible, afin que chaque personne puisse accéder et comprendre ses données de manière simple et concise. Ainsi cette expérience pourra mettre en garde notre classe et plus largement les étudiants de l’ESD face aux dangers des plateformes utilisant des modèles économiques basés sur des systèmes de micro-paiement. On espère une prise de conscience qui leur fera faire réduire leur consommation et leurs dépenses sur ce type d’application. Le fond est moralisateur mais volontairement emprunt de fun grâce au classement et au concours.')
        st.write('Qui sommes-nous pour vous juger ? 😜')
    with col2:
        st.title('Vie privée')
        st.write(' ')
        st.write('L\'application collecte des données personnelles dans le but d\'offrir un classement des différents utilisateurs.')
        st.write('Le fichier ZIP importé comprend différentes données personnelles. Les seules données personnelles stockées par l\'application sont : nom, prénom et somme des dépenses sur l\'année 2021.')
        st.write('Si vous avez fait le choix de participer au classement et que vous souhaitez ne plus y apparaître, vous pouvez contacter Lilou Roger ou Yann Vanden Broeck sur le Slack ESDESP.')
