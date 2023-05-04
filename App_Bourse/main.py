"""
Créer le 29/04/2023
Par: Carl Trépanier
Descritpion: Programme principal
Révisé le: 03/05/2023
"""

import matplotlib.pyplot as plt

from datetime import date, datetime, timedelta
from data_manager import get_and_manage_rates_data
from data_processing import *

# Initialisation de la date de début et de fin
date_start = date(2018, 1, 1)
#date_end = date(2023, 4, 30)
date_end = date.today() - timedelta(1) # Pour avoir la date d'hier

# Initialisation des actifs
assets = "ETH/USD"

# Récupération des données
rates = get_and_manage_rates_data(assets, date_start, date_end)
print("nb rates:", len(rates))

# Initialisation des moyennes mobiles. Calcul de la moyenne mobile sur 8 et 40 jours
ma_intervals = [8, 40]
ma_list = []

# Calcul des moyennes mobiles
for ma_interval in ma_intervals:
    ma = compute_moving_average_for_rates_data(rates, ma_interval)
    ma_list.append((ma, ma_interval))

# Calcul des points d'achat et de vente
buy_and_sell_points = compute_buy_and_sell_points_from_ma(ma_list[0][0], ma_list[1][0], 1)

# Calcul des gains avec un portefeuille de départ de 1000$
initial_wallet = 1000
final_wallet = compute_buy_and_sell_gains(initial_wallet, rates, buy_and_sell_points)

# Affichage des résultats
print("Date de début:", date_start, "avec un portefeuille de", str(round(initial_wallet, 2)) + "$.")
print("Date de fin:", date_end, "avec un portefeuille de", str(round(final_wallet, 2)) + "$.")

if final_wallet > initial_wallet:
    percent = (final_wallet - initial_wallet) * 100 / initial_wallet
    print("Soit un gain de", str(round(percent, 2)) + "%")
else:
    percent = (initial_wallet - final_wallet) * 100 / initial_wallet
    print("Soit une perte de", str(round(percent, 2)) + "%")

# Calcul des moyennes mobiles pour l'affichage. ma20 représente la moyenne mobile sur 20 jours et ma100 sur 100 jours
ma20 = compute_moving_average_for_rates_data(rates, 20)
ma100 = compute_moving_average_for_rates_data(rates, 100)

# Affichage du graphique
rates_dates = [datetime.strptime(rate["date"], "%Y-%m-%d") for rate in rates]
rates_values = [rate["value"] for rate in rates]

plt.ylabel(assets)
plt.plot(rates_dates, rates_values)

# Affichage des moyennes mobiles
for ma_item in ma_list:
    ma_values = [rate["value"] for rate in ma_item[0]]
    plt.plot(rates_dates, ma_values, label="MA" + str(ma_item[1]))

# Affichage des points d'achat et de vente
for point in buy_and_sell_points:
    date_obj = datetime.strptime(point[0], "%Y-%m-%d")
    plt.axvline(x=date_obj, color="red" if point[1] else "lightgreen")

plt.legend()
plt.show()
