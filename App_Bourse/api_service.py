"""
Créer le 29/04/2023
Par: Carl Trépanier
Descritpion: Prise de données de l'API
Révisé le: 04/05/2023
"""

import requests
import json

from datetime import timedelta
from api_config import API_KEY, BASE_URL

headers = {"X-CoinAPI-Key" : API_KEY}

# On crée une liste de périodes de dates de longueur maximale max_days
def get_dates_intervals(date_start, date_end, max_days):
    diff = date_end - date_start
    diff_days = diff.days
    dates_intervals = []
    interval_start_date = date_start
    while diff_days > 0:
        nb_days_to_add = max_days - 1
        if diff_days < max_days - 1:
            nb_days_to_add = diff_days
        interval_end_date = interval_start_date + timedelta(nb_days_to_add)
        dates_intervals.append((interval_start_date, interval_end_date))
        diff_days -= nb_days_to_add + 1
        interval_start_date = interval_end_date + timedelta(1)
    return dates_intervals

# On récupère les taux de change entre deux dates, incluant la date de fin
def api_get_exchange_rates(assets, start_date, end_date):
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = (end_date + timedelta(1)).strftime("%Y-%m-%d")

    url = f"{BASE_URL}v1/exchangerate/{assets}/history?period_id=1DAY&time_start={start_date_str}T00:00:00&time_end={end_date_str}T00:00:00"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        print("Quota restant:", response.headers["X-RateLimit-remaining"]) # Affiche le nombre de requêtes restantes
        print()
        return data
    else:
        print(f"Error with status code: {response.status_code}")
        return None

# Les dates de début et de fin peuvent être séparées de plus de 100 jours
def api_get_exchange_rates_extended(assets, start_date, end_date):
    rates = []
    dates_intervals = get_dates_intervals(start_date, end_date, 100)
    
    if len(dates_intervals) > 0:
        for i in dates_intervals:
            rates += api_get_exchange_rates(assets, i[0], i[1])
    return rates

# Vérifier la cohérence des données
def rate_is_inconsistente(rate):
    value = rate["rate_open"]
    vmin = value / 10
    vmax = value * 10
    if not vmin <= rate["rate_close"] <= vmax:
        return True
    return (
        not vmin <= rate["rate_low"] <= vmax
        if vmin <= rate["rate_high"] <= vmax
        else True
    )

# Filtrage des données inconsistantes
def filter_inconsistent_rate_values(input_rates):
    if len(input_rates) < 2:
        return input_rates
    filtered_rates = []
    for i in range(len(input_rates)):
        rate = input_rates[i]
        if rate_is_inconsistente(rate):
            reference_rate = None
            reference_rate = input_rates[i - 1] if i > 0 else input_rates[i + 1]
            patched_rate = rate
            patched_rate["rate_open"] = reference_rate["rate_open"]
            patched_rate["rate_close"] = reference_rate["rate_close"]
            patched_rate["rate_high"] = reference_rate["rate_high"]
            patched_rate["rate_low"] = reference_rate["rate_low"]
        filtered_rates.append(rate)
    return filtered_rates

# Retourne les données filtrées
def api_get_exchange_filtered_rates_extended(assets, start_date, end_date):
    rates = api_get_exchange_rates_extended(assets, start_date, end_date)
    return filter_inconsistent_rate_values(rates)