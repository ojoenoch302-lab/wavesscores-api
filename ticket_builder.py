from engine.ticket_builder import generate_ticket

user_id = "user_1"
mode = "safe"   # safe / medium / risky

ticket, odds = generate_ticket(user_id=user_id, mode=mode)

print("\nWAVESSCORES BET BUILDER")
print("=" * 40)
print(f"User: {user_id}")
print(f"Mode: {mode.upper()}")

for pick in ticket:
    print(f"\n{pick['Match']}")
    print(f"Pick: {pick['Pick']}")
    print(f"Odds: {pick['Odds']}")
    print(f"Confidence: {pick['Confidence']}")
    print("-" * 20)

print("\nTOTAL ODDS:", round(odds, 2))
print("=" * 40)