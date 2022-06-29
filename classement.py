import streamlit as st
from zipfile import ZipFile, Path
import pandas as pd
from datetime import datetime
from fonctions import depense
from fonctions import bonjour
from fonctions import top5
from fonctions import scoring

def classement():
    st.title('Classement')
    st.write("Le classement est basé sur le montant dépensé en 2021 sur l'application Uber Eats.")

    #get necessary data for scoring function
    #bjr, data_Firstname, data_Lastname = bonjour(st.session_state.zip)
    #dépense_TTC, moyenne_price, nb_commande, frais, dépense_TTC_2021, moyenne_price_2021, nb_commande_2021, frais_2021 = depense(st.session_state.zip)
    #classement = scoring(data_Firstname, data_Lastname, dépense_TTC_2021)

    classement = pd.read_csv('classement.csv', sep=",")
    classement.index += 1

    st.table(classement)

    st.stop()