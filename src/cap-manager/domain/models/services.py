from collections import defaultdict
from typing import Dict, Set, List, Optional
from os import name
from players import Player, PlayerStatus
from contract import Contract


players_by_id: Dict[str, Player] = {}
players_ids_by_team: Dict[str, Set[str]] = defaultdict(set)
free_agent_ids: Set[str] = set()
contracts_by_id: Dict[str, Contract] = {}

def add_player(player: Player) -> None:
    if player.player_id in players_by_id:
        raise ValueError(f"Player {player.player_id} already exists")
    players_by_id[player.player_id] = player

    if player.team is None:
        free_agent_ids.add(player.player_id)
    else:
        players_ids_by_team[player.team].add(player.player_id)

def get_players_by_team(team: str) -> list[Player]:
    ids = players_ids_by_team.get(team, set())
    return [players_by_id[pid] for pid in ids]

def get_free_agents() -> list[Player]:
    return [players_by_id[pid] for pid in free_agent_ids]

def get_player(players: dict, player_id):
    return players.get(player_id)

def add_contract(contract: Contract) -> None:
    if contract.contract_id in contracts_by_id:
        raise ValueError(f"Contract {contract.contract_id} already exist")
    contracts_by_id[contract.contract_id] = contract

def get_contract(contract_id: str) -> Contract:
    return contracts_by_id[contract_id]

def get_contracts_by_team(team: str) ->List[Contract]:
    return [c for c in contracts_by_id.values() if c.team == team]

def get_contracts_by_player(player_id: str) -> List[Contract]:
    return [c for c in contracts_by_id.values if c.player_id == player_id]
    




