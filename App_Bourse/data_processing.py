# Calcul du taux de change moyen sur une période donnée
def compute_moving_average_for_rates_data(rates, nb_days_interval):
    sum = 0
    averages = []

    for i in range(len(rates)):
        rate = rates[i]
        sum += rate["value"]
        average = 0
        if i >= nb_days_interval:
            sum -= rates[i - nb_days_interval]["value"]
            average = sum / nb_days_interval
        else:
            average = sum / (i + 1)
        averages.append({"date": rate["date"], "value": average})

    return averages

# Calcul des points d'achat et de vente à partir de deux moyennes mobiles
def compute_buy_and_sell_points_from_ma(short_ma, long_ma, threshold_percent=0):
    buy_mode = True
    points = []

    for i in range(len(short_ma)):
        date_str = short_ma[i]["date"]
        short_ma_value = short_ma[i]["value"]
        long_ma_value = long_ma[i]["value"]
        multiplicateur = 1 + threshold_percent / 100

        if buy_mode: # On cherche un point d'achat
            if short_ma_value > long_ma_value * multiplicateur:
                points.append((date_str, buy_mode))
                buy_mode = False
        else: # On cherche un point de vente
            if short_ma_value < long_ma_value / multiplicateur:
                points.append((date_str, buy_mode))
                buy_mode = True

    return points

# Récupération du taux de change pour une date donnée
def get_rate_value_for_date_str(rates, date_str):
    for rate in rates:
        if rate["date"] == date_str:
            return rate["value"]
    return None

# Calcul des gains à partir des points d'achat et de vente
def compute_buy_and_sell_gains(initial_wallet, rates, buy_and_sell_points):
    current_wallet = initial_wallet
    last_wallet = 0
    shares = 0

    if buy_and_sell_points[-1][1]:
        buy_and_sell_points = buy_and_sell_points[:-1]

    for point in buy_and_sell_points:
        rate_value = get_rate_value_for_date_str(rates, point[0])
        if point[1]:
            print("Le", point[0] + ", j'achète pour", str(round(current_wallet, 2)) + "$.")
            shares = current_wallet / rate_value
            last_wallet = current_wallet
            current_wallet = 0
        else:
            current_wallet = shares * rate_value
            shares = 0
            print("Le", point[0] + ", je vend pour", str(round(current_wallet, 2)) + "$")
            if current_wallet > last_wallet:
                percent = (current_wallet - last_wallet) * 100 / last_wallet
                print("Soit un gain de", str(round(percent, 2)) + "%")
            else:
                percent = (last_wallet - current_wallet) * 100 / last_wallet
                print("Soit une perte de", str(round(percent, 2)) + "%")
            print()

    return current_wallet
    