from services import get_contract, get_contracts_by_team
from engine.cap_engine import team_cap_spent

NFL_CAP_PER_YEAR = {
    2026: 303500000,
    2027: 329000000,
    2028: 350000000
}

def team_cap_space(team: str, year: int) -> int:
    cap_limit = NFL_CAP_PER_YEAR[year]
    spent = team_cap_spent(team, year)
    return cap_limit - spent
