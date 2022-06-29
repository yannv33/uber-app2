import streamlit as st
from zipfile import ZipFile, Path
import pandas as pd
from datetime import datetime
from fonctions import depense
from fonctions import bonjour
from fonctions import top5
from fonctions import scoring

def mes_analyses():
    # CSS to inject contained in a string
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    # Corps du site

    st.title("Découvre tes données Uber Eats !")

    data_lilou = {}

    uploaded_zip = st.file_uploader('Upload ton fichier ZIP dans l\'encadré en dessous !', type="zip")

    if (uploaded_zip is not None):
        #ok
        bjr, data_Firstname, data_Lastname = bonjour(uploaded_zip)
        st.title(bjr)
        st.write("Voici un résumé de tes données Uber Eats au global et sur l'année 2021 !")
        st.write(" ")
        st.write("Si tu souhaites participer au classement, clique le bouton ci-dessous :")

        dépense_TTC, moyenne_price, nb_commande, frais, dépense_TTC_2021, moyenne_price_2021, nb_commande_2021, frais_2021 = depense(uploaded_zip)
        top_5_restau, top_5_restau_2021, top_5_prod, top_5_prod_2021 = top5(uploaded_zip)

        if st.button('Participer au classement'):
            scoring(data_Firstname, data_Lastname, dépense_TTC_2021)
            st.write('Participation prise en compte !')
        else:
            None

        col1, col2 = st.columns(2)
        with col1:
            st.title('Global')
            st.write("Total dépense =", dépense_TTC,"€,")
            st.write("dont", frais, "€ de frais,")
            st.write("pour", nb_commande, "commandes,")
            st.write("avec une moyenne par commande de", moyenne_price,"€.")
            st.write('------------------------------------------')
            st.subheader('Top 5 des restaurants les + commandés')
            st.table(top_5_restau.head())
            st.write('------------------------------------------')
            st.subheader('Top 5 des produits les + commandés')
            st.table(top_5_prod.head())

        with col2:
            st.title('2021')
            st.write("Total dépense =", dépense_TTC_2021,"€,")
            st.write("dont", frais_2021, "€ de frais,")
            st.write("pour", nb_commande_2021, "commandes,")
            st.write("avec une moyenne par commande de", moyenne_price_2021,"€.")
            st.write('------------------------------------------')
            st.subheader('Top 5 des restaurants les + commandés en 2021')
            st.table(top_5_restau_2021.head())
            st.write('------------------------------------------')
            st.subheader('Top 5 des produits les + commandés en 2021')
            st.table(top_5_prod_2021.head())

    else:
       st.info(
          f"""
                👆 Pour pouvoir accéder à l'analyse de tes données Uber Eats il faut au préalable les télécharger sur leur site.
                ⚠️ Il y a un délai de minimum 24h pour les récupérer : [Faire la demande](https://auth.uber.com/login/?breeze_local_zone=dca1&next_url=https%3A%2F%2Fmyprivacy.uber.com%2Fprivacy%2Fexploreyourdata%2Fdownload%3F_ga%3D2.66157422.1551093104.1654689943-719198744.1652267294&state=1sYn0ZT-glUCeVIUaR0cUyziL8MvPBH4ab9tCMQKtX0%3D)
                """
        )

    if 'zip' not in st.session_state:
        st.session_state['zip'] = uploaded_zip

    st.stop()
            