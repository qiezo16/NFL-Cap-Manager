import sys
from pathlib import Path
from tkinter import ACTIVE
from turtle import position

# Add src/cap-manager to path so imports work when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src" / "cap-manager"))

from domain.models.players import Player, PlayerStatus

p = Player(
    player_id="QB01",
    name="Jordan Love",
    position="QB",
    team="GB",
    status=PlayerStatus.ACTIVE,
    experience=6,
)



k = Player(
    player_id="QB02",
    name="Aaron Rodgers",
    position="QB",
    team="PIT",
    status=PlayerStatus.ACTIVE,
    experience=21,
)




players_by_id = {}

def add_player(players: dict, player: Player):
    if player.player_id in players:
        raise ValueError(f"Player {player.player_id} already exists")
    players[player.player_id] = player
def get_players_by_team(players: dict, team: str):
    return [p for p in players.values() if p.team == team]


add_player(
    players_by_id,
    p,  
)

add_player(
    players_by_id,
    k,
)

add_player(
    players_by_id,
    Player(
        player_id="QB03",
        name="Patrick Mahomes",
        position="QB",
        team="KC",
        status=PlayerStatus.ACTIVE,
        experience=9,
    ),  
)

add_player(
    players_by_id,
    Player(
        player_id="QB04",
        name="Josh Allen",
        position="QB",
        team="BUF",
        status=PlayerStatus.ACTIVE,
        experience=8,
    ),
)

add_player(
    players_by_id,
    Player(
        player_id="QB05",
        name="Matthew Stafford",
        position="QB",
        team="LAR",
        status=PlayerStatus.ACTIVE,
        experience=17,
    ),
)

add_player(
    players_by_id,
    Player(
        player_id="QB06",
        name="Justin Herbert",
        position="QB",
        team="LAC",
        status=PlayerStatus.ACTIVE,
        experience=6,
    ),
)

add_player(
    players_by_id,
    Player(
        player_id="QB07",
        name="Dak Prescott",
        position="QB",
        team="DAL",
        status=PlayerStatus.ACTIVE,
        experience=10,
    ),
)
add_player(
    players_by_id,
    Player(
        player_id="WR01",
        name="Justin Jefferson",
        position="WR",
        team="MIN",
        status=PlayerStatus.ACTIVE,
        experience=6,
    ),
)
add_player(
    players_by_id,
    Player(
        player_id="WR02",
        name="Davante Adams",
        position="WR",
        team="LAR",
        status=PlayerStatus.ACTIVE,
        experience=12,
    ),
)
add_player(
    players_by_id,
    Player(
        player_id="WR03",
        name="Christian Watson",
        position="WR",
        team="GB",
        status=PlayerStatus.ACTIVE,
        experience=4,
    ),
)
add_player(
    players_by_id,
    Player(
        player_id="WR04",
        name="Matthew Golden",
        position="WR",
        team="GB",
        status=PlayerStatus.ACTIVE,
        experience=1,   # rookie
    )
)
add_player(
    players_by_id,
    Player(
        player_id="TE01",
        name="Tucker Kraft",
        position="TE",
        team="GB",
        status=PlayerStatus.ACTIVE,
        experience=3,
    ),
)
add_player(
    players_by_id,
    Player(
        player_id="TE02",
        name="Luke Musgrave",
        position ="TE",
        team="GB",
        status=PlayerStatus.ACTIVE,
        experience=3,
    ),
)
min_players = get_players_by_team(players_by_id, "MIN")
print(min_players)
