import pandas as pd
import random
import hashlib


def get_seed(user_id):
    return int(hashlib.md5(user_id.encode()).hexdigest(), 16) % 100000


def generate_ticket(user_id="guest", mode="safe"):
    df = pd.read_csv("data/daily_predictions.csv")

    df = df.sort_values(by="Confidence", ascending=False)

    random.seed(get_seed(user_id))

    # 🎯 MODE SETTINGS
    if mode == "safe":
        max_games = 2
        max_odds = 2.10
        min_conf = 85

    elif mode == "medium":
        max_games = 3
        max_odds = 3.20
        min_conf = 80

    else:  # risky
        max_games = 4
        max_odds = 5.00
        min_conf = 75

    selected = []
    total_odds = 1.0

    attempts = 0

    while len(selected) < max_games and attempts < 50:

        attempts += 1

        pool = df[df["Confidence"] >= min_conf]
        pool = pool.head(max(3, len(pool)))

        if pool.empty:
            break

        row = pool.sample(n=1).iloc[0]

        if row["Match"] in [x["Match"] for x in selected]:
            continue

        new_total = total_odds * row["Odds"]

        if new_total > max_odds:
            continue

        selected.append(row)
        total_odds = new_total

    return selected, total_odds