import streamlit as st
from zipfile import ZipFile, Path
import pandas as pd
from datetime import datetime


def bonjour(uploaded_zip):

    with ZipFile(uploaded_zip) as myzip:
            data = myzip.open("Uber Data/Account and Profile/profile_data.csv")
        
    data = pd.read_csv(data)

    data_Firstname = data['First Name'].to_string(index=False)
    data_Lastname = data['Last Name'].to_string(index=False)
    bjr = 'Bonjour' + ' ' + data_Firstname + ' ' + data_Lastname + ' ' + '! 👋 '
    #st.title(bjr)

    return bjr, data_Firstname, data_Lastname

def scoring(name, last_name, depense):

    score = pd.read_csv('classement.csv', sep=",")

    nom = name + ' ' + last_name

    result1 = score.isin([nom]).any().any()
    result2 = score.isin([depense]).any().any()
    
    
    if not (result1 and result2):
        score = score.append({'Nom': nom, 'Dépense': depense}, ignore_index=True).sort_values(by='Dépense', ascending=False)
        pd.DataFrame(score).to_csv('classement.csv', index=False)

def depense(uploaded_zip):
        
        with ZipFile(uploaded_zip) as myzip:
            data = myzip.open("Uber Data/Eats/eats_order_details.csv")
            data2 = myzip.open("Uber Data/Eats/eats_order_details.csv")

        data_Global = pd.read_csv(data)
        data_2021 = pd.read_csv(data2)

        list_date = data_2021['Order Time'].tolist()
        list_date = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z %Z') for date in list_date ]
        data_2021['Order Time']= list_date
        data_2021['Order Time'] = data_2021['Order Time'].dt.strftime('%Y')
        data_2021 = data_2021.rename(columns={"Order Time": "Order_Time"})

        data_2021 = data_2021.query('Order_Time=="2021"')

        #Au global dépense + répartition frais / nourriture 
        unique_data_TTC = data_Global[["Order ID","Order Price"]].drop_duplicates(subset=['Order ID'])
        unique_data_TTC = unique_data_TTC[["Order ID","Order Price"]].dropna(subset=['Order Price'])

        dépense_TTC = round(sum(unique_data_TTC["Order Price"]),2)
        dépense_HT = round(sum(data_Global["Item Price"]),2)
        moyenne_price = round(unique_data_TTC["Order Price"].mean(),2)
        nb_commande = unique_data_TTC["Order ID"].count()
        frais = round(dépense_TTC - dépense_HT)

        #st.write("AU GLOBAL")
        #st.write("total dépense =", dépense_TTC,"€")
        #st.write("dont", frais, "€ de frais")
        #st.write("pour", nb_commande, "commandes")
        #st.write("avec une moyenne par commande de", moyenne_price,"€")


        #Sur l'année 2021 dépense + répartition frais / nourriture 
        data_2021_TTC = data_2021[["Order ID","Order Price"]].drop_duplicates(subset=['Order ID'])

        dépense_TTC_2021 = round(sum(data_2021_TTC["Order Price"]),2)
        dépense_HT_2021 = round(sum(data_2021["Item Price"]),2)
        moyenne_price_2021 = round(data_2021_TTC["Order Price"].mean(),2)
        nb_commande_2021 = data_2021_TTC["Order ID"].count()
        frais_2021 = round(dépense_TTC_2021 - dépense_HT_2021)

        #st.write('------------')
        #st.write("SUR 2021")
        #st.write("total dépense =", dépense_TTC_2021,"€")
        #st.write("dont", frais_2021, "€ de frais")
        #st.write("pour", nb_commande_2021, "commandes")
        #st.write("avec une moyenne par commande de", moyenne_price_2021,"€")

        return dépense_TTC, moyenne_price, nb_commande, frais, dépense_TTC_2021, moyenne_price_2021, nb_commande_2021, frais_2021

def top5(zipzip):
    with ZipFile(zipzip) as myzip:
        data = myzip.open("Uber Data/Eats/eats_order_details.csv")
        data2 = myzip.open("Uber Data/Eats/eats_restaurant_names.csv")
    orders = pd.read_csv(data)
    restaurant = pd.read_csv(data2)
    orders['Times ordered'] = 1
    orders2 = orders
    
    list_date = orders2['Order Time'].tolist()
    list_date = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z %Z') for date in list_date ]
    orders2['Order Time']= list_date
    orders2['Order Time'] = orders['Order Time'].dt.strftime('%Y')
    orders2 = orders2.rename(columns={"Order Time": "Order_Time"})
    orders_2021 = orders2.query('Order_Time=="2021"')
    
    #dataset commandes dédupliquées
    orders_restaurant = orders.drop_duplicates(subset=['Order ID']) 
    orders_restaurant_2021 = orders_2021.drop_duplicates(subset=['Order ID'])
    #dataset products
    orders_product = orders
    orders_product_2021 = orders_2021
    
    restaurant = restaurant.drop_duplicates(subset={'Restaurant ID'})
    
    #top 5 restaurant global
    
    top_5_restau = orders_restaurant[['Restaurant ID','Times ordered']].groupby('Restaurant ID').sum().sort_values(by='Times ordered', ascending=False)
    top_5_restau.reset_index(inplace=True)
    
    correspondance = dict(zip(restaurant['Restaurant ID'], restaurant['Restaurant Name']))
    top_5_restau['Restaurant Name'] = top_5_restau['Restaurant ID'].map(correspondance)
    
    #top 5 restaurant 2021
    
    top_5_restau_2021 = orders_restaurant_2021[['Restaurant ID','Times ordered']].groupby('Restaurant ID').sum().sort_values(by='Times ordered', ascending=False)
    top_5_restau_2021.reset_index(inplace=True)
    top_5_restau_2021['Restaurant Name'] = top_5_restau_2021['Restaurant ID'].map(correspondance)
    
    #top 5 produit
    
    top_5_prod = orders_product[['Item Name','Times ordered']].groupby('Item Name').sum().sort_values(by="Times ordered", ascending=False)
    top_5_prod.reset_index(inplace=True)
    
    
    #top 5 produits 2021
    
    top_5_prod_2021 = orders_product_2021[['Item Name','Times ordered']].groupby('Item Name').sum().sort_values(by="Times ordered", ascending=False)
    top_5_prod_2021.reset_index(inplace=True)
    #supprimer Restaurant ID
    top_5_restau = top_5_restau.drop(["Restaurant ID"], axis=1)
    top_5_restau_2021 = top_5_restau_2021.drop(["Restaurant ID"], axis=1)
    #change column order
    top_5_restau = top_5_restau.iloc[:, [1,0]]
    top_5_restau_2021 = top_5_restau_2021.iloc[:, [1,0]]
    #rename columns
    top_5_restau.rename(columns = {'Restaurant Name':'Restaurant', 'Times ordered':'Nombre de commandes'}, inplace = True)
    top_5_restau_2021.rename(columns = {'Restaurant Name':'Restaurant', 'Times ordered':'Nombre de commandes'}, inplace = True)
    top_5_prod.rename(columns = {'Item Name':'Produit', 'Times ordered':'Nombre de commandes'}, inplace = True)
    top_5_prod_2021.rename(columns = {'Item Name':'Produit', 'Times ordered':'Nombre de commandes'}, inplace = True)
    

    return top_5_restau, top_5_restau_2021, top_5_prod, top_5_prod_2021