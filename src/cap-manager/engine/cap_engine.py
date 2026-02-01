from domain.models.services import get_contracts_by_team

def team_cap_spent(team: str, year: int) -> int:
    contracts = get_contracts_by_team(team)
    return sum(c.cap_hit(year)for c in contracts)
    