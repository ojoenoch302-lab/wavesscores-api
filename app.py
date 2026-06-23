import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from flask import Flask, request, jsonify
from ticket_builder import generate_ticket

app = Flask(__name__)


@app.route("/")
def home():
    return "Wavesscores API is running"


@app.route("/generate-ticket", methods=["GET"])
def generate():

    user_id = request.args.get("user_id", "guest")
    mode = request.args.get("mode", "safe")

    ticket, odds = generate_ticket(user_id=user_id, mode=mode)

    result = []

    for pick in ticket:
        result.append({
            "match": pick["Match"],
            "pick": pick["Pick"],
            "odds": float(pick["Odds"]),
            "confidence": int(pick["Confidence"])
        })

    return jsonify({
        "user": user_id,
        "mode": mode,
        "total_odds": round(odds, 2),
        "ticket": result
    })


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
