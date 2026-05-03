# Written by ChatGPT https://chatgpt.com/share/69ee57d6-c768-83ea-a92e-e2bf54c7a19a

from datetime import datetime, timezone
import asyncio
from pyscript import document

# =========================
# CONSTANTS
# =========================

WAR_START = datetime(2026, 2, 28, tzinfo=timezone.utc)

# Piecewise early-phase rates:
# (duration_in_days, dollars_per_day)
EARLY_PHASE = [
    (4.17, 891_000_000),   # first 100 hours ≈ 4.17 days
    (1.83, 1_800_000_000), # up to day 6 total
    (6.0, 601_000_000),    # days 7–12
]

# Steady-state average estimated rate after early phase
STEADY_RATE = 800_000_000  # dollars per day

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
    el = document.getElementById("cost")

    while True:
        now = datetime.now(timezone.utc)
        elapsed = (now - WAR_START).total_seconds()

        total_cost = compute_cost(elapsed)

        el.innerText = format_money(total_cost)

        await asyncio.sleep(0.1)


# run loop
asyncio.ensure_future(update())
