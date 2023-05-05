"""
Créer le 03/05/2023
Par: Carl Trépanier
Descritpion: Programme principal du dashboard streamlit
Révisé le: 04/05/2023
"""


import streamlit as st
import matplotlib.pyplot as plt

from datetime import date, datetime, timedelta
from data_manager import get_and_manage_rates_data
from data_processing import *

st.title("Dashboard")

st.write("## Initialisation des variables")

# Initialisation de la date de début et de fin
date_start = st.date_input("Date de début", value=date(2018, 1, 1))
date_end = st.date_input("Date de fin", value=date.today() - timedelta(1))

# Initialisation des actifs
dropdown_assets = st.selectbox("Symbole boursier", ["BTC/USD", "LTC/USD", "ETH/USD", "XRP/USD", "TSLA/USD", "MSFT/USD", "FB/USD", "AAPL/USD", "AMZN/USD", "GOOGL/USD"])
assets = dropdown_assets

st.write("## Récupération des données")

# Récupération des données
rates = get_and_manage_rates_data(assets, date_start, date_end)
st.write("Nombre de données:", len(rates))

# Initialisation des moyennes mobiles
ma_intervals = [8, 40]
ma_list = []

# Calcul des moyennes mobiles
for ma_interval in ma_intervals:
    ma = calculate_mobile_average_for_rates_data(rates, ma_interval)
    ma_list.append((ma, ma_interval))

# Calcul des points d'achat et de vente
buy_and_sell_points = calculate_buy_and_sell_points_from_ma(ma_list[0][0], ma_list[1][0], 1)

st.write("## Calcul des gains et des pertes")

# Calcul des gains
initial_wallet = 1000

try:
    final_wallet = calculate_buy_and_sell_gains(initial_wallet, rates, buy_and_sell_points)
except Exception:
    st.error("Erreur: Division par zéro lors du calcul des gains et des pertes")

# Affichage du graphique
rates_dates = [datetime.strptime(rate["date"], "%Y-%m-%d") for rate in rates]
rates_values = [rate["value"] for rate in rates]

st.write("Date de début:", date_start)
st.write("Date de fin:", date_end)
st.write("Portefeuille de début:", f"{str(round(initial_wallet, 2))}$")
st.write("Portefeuille de fin:", f"{str(round(final_wallet, 2))}$")

if final_wallet > initial_wallet:
    percent = (final_wallet - initial_wallet) * 100 / initial_wallet
    st.write("Soit un gain de", f"{str(round(percent, 2))}%")
else:
    percent = (initial_wallet - final_wallet) * 100 / initial_wallet
    st.write("Soit une perte de", f"{str(round(percent, 2))}%")

st.write("## Affichage du graphique")

# Affichage du graphique
fig, ax = plt.subplots()
ax.set_ylabel(assets)
ax.plot(rates_dates, rates_values)

ax.legend()
st.pyplot(fig)
