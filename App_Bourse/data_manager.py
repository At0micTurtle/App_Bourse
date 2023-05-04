"""
Créer le 29/04/2023
Par: Carl Trépanier
Descritpion: Gestion des données
Révisé le: 03/05/2023
"""

import json

from datetime import date, datetime, timedelta
from api_service import api_get_exchange_filtered_rates_extended
from os import path

# À partir de la liste des données de taux de change, on crée une liste de dictionnaires
def convert_rates_to_date_value_format(rates_data):
    rates_date_value_format = []
    for rate in rates_data:
        rates_date_value_format.append({"date": rate["time_period_start"][:10], "value": rate["rate_close"]})
    return rates_date_value_format

# On sauvegarde les données de taux de change dans un fichier
def save_rates_data_to_file(filename, rates_data):
    json_data = json.dumps(rates_data)
    f = open(filename, "w")
    f.write(json_data)
    f.close()

# On charge les données de taux de change depuis un fichier
def load_json_data_from_file(filename):
    f = open(filename, "r")
    json_data = f.read()
    f.close()
    return json_data

# On récupère les données de taux de change depuis l'API CoinAPI et on les sauvegarde dans un fichier
def get_and_manage_rates_data(assets, date_start, date_end):
    data_filename = assets.replace("/", "_") + ".json"
    rates = []
    exclude_nb_days_start = 0
    exclude_nb_days_end = 0

    # Si le fichier existe, on charge les données de taux de change depuis le fichier
    if path.exists(data_filename):
        json_rates = load_json_data_from_file(data_filename)
        rates = json.loads(json_rates)

    # Si le fichier n'existe pas ou si les données de taux de change ne couvrent pas la période demandée, on récupère les données depuis l'API
    if len(rates) > 0:
        saved_data_date_start_str = rates[0]["date"]
        saved_data_date_end_str = rates[-1]["date"]
        print("Le fichier json existe")
        print("  Saved data date start:", saved_data_date_start_str)
        print("  Saved data date end:", saved_data_date_end_str)

        # Conversion des dates de début et de fin des données sauvegardées en string
        saved_data_date_start = datetime.strptime(saved_data_date_start_str, "%Y-%m-%d").date()
        saved_data_date_end = datetime.strptime(saved_data_date_end_str, "%Y-%m-%d").date()

        # Calcul du nombre de jours entre la date de début demandée et la date de début des données sauvegardées
        nb_days_start = (saved_data_date_start - date_start).days
        
        # Si la date de début demandée est antérieure à la date de début des données sauvegardées, on récupère les données manquantes
        if nb_days_start > 0:
            print("On rajoute les données à gauche: ", date_start, saved_data_date_start - timedelta(1))
            rates_start = api_get_exchange_filtered_rates_extended(assets, date_start, saved_data_date_start - timedelta(1))
            rates_start_date_value = convert_rates_to_date_value_format(rates_start)
            rates = rates_start_date_value + rates
        elif nb_days_start < 0:
            exclude_nb_days_start = -nb_days_start

        # Calcul du nombre de jours entre la date de fin demandée et la date de fin des données sauvegardées
        nb_days_end = (date_end - saved_data_date_end).days

        # Si la date de fin demandée est postérieure à la date de fin des données sauvegardées, on récupère les données manquantes
        if nb_days_end > 0:
            print("On rajoute les données à droite: ", saved_data_date_end + timedelta(1), date_end)
            rates_end = api_get_exchange_filtered_rates_extended(assets, saved_data_date_end + timedelta(1), date_end)
            rates_end_date_value = convert_rates_to_date_value_format(rates_end)
            rates += rates_end_date_value
        elif nb_days_end < 0:
            exclude_nb_days_end = -nb_days_end
        
        save_rates_data_to_file(data_filename, rates)
    else:
        rates_api = api_get_exchange_filtered_rates_extended(assets, date_start, date_end)
        rates = convert_rates_to_date_value_format(rates_api)    
        save_rates_data_to_file(data_filename, rates)

    if exclude_nb_days_start > 0:
        rates = rates[exclude_nb_days_start:]

    if exclude_nb_days_end > 0:
        rates = rates[:-exclude_nb_days_end]

    return rates