# Written by ChatGPT https://chatgpt.com/share/69ee57d6-c768-83ea-a92e-e2bf54c7a19a

from datetime import datetime, timezone
import asyncio
from pyscript import document

# =========================
# CONSTANTS
# =========================

WAR_START = datetime(2026, 2, 28, tzinfo=timezone.utc)

# Piecewise early-phase rates: (duration_in_days, dollars_per_day)
EARLY_PHASE = [
    (4.17, 891_000_000),    # after day 0 → day 4.17: 02/28-03/04, first 100 hours
    (1.83, 1_800_000_000),  # after day 4.17 → day 6: 03/04-03/06, early surge through day 6
    (6.0, 601_000_000),     # after day 6 → day 12: 03/06-03/12, reduced early-war phase
    (26.0, 1_000_000_000),  # after day 12 → day 38: 03/12-04/07, sustained hostilities
    (69.0, 750_000_000),    # after day 38 → day 107: 04/07-06/15, so-called 'ceasefire' period
    (13.0, 400_000_000),    # after day 107 → day 120: 06/15-06/28, reduced operations estimate post-MOU
    (20.0, 750_000_000),    # after day 120 → day 140: 06/28-07/18, renewed hostilities
]

# Steady-state average estimated dollars per day rate after latest TACO
STEADY_RATE = 500_000_000   # after day 140: 07/18-present, ongoing lower-intensity operations

# =========================
# DERIVED
# =========================

SECONDS_PER_DAY = 86400


# =========================
# CORE COST FUNCTION
# =========================

def compute_cost(elapsed_seconds):
    remaining_days = elapsed_seconds / SECONDS_PER_DAY
    total = 0.0

    for days, rate in EARLY_PHASE:
        if remaining_days <= 0:
            break

        span = min(remaining_days, days)
        total += span * rate
        remaining_days -= span

    # remaining time uses steady-state rate
    if remaining_days > 0:
        total += remaining_days * STEADY_RATE

    return total


# =========================
# FORMATTER
# =========================

def format_money(x):
    return f"${x:,.0f}"


# =========================
# LOOP
# =========================

async def update():
    cost_el = document.getElementById("cost")
    day_el = document.getElementById("day")

    while True:
        now = datetime.now(timezone.utc)
        elapsed = (now - WAR_START).total_seconds()
        day = elapsed / 86400

        total_cost = compute_cost(elapsed)

        cost_el.innerText = format_money(total_cost)
        day_el.innerText = str(int(day))

        await asyncio.sleep(0.1)


# run loop
asyncio.ensure_future(update())
