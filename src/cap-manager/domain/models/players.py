from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PlayerStatus(Enum):
    ACTIVE = "active"
    INJURED_RESERVE = "injured reserve"
    PRACTICE_SQUAD = "practice squad"
    FREE_AGENT = "free agent"


@dataclass
class Player:
    player_id: str
    name: str
    position: str
    team: Optional[str]
    status: PlayerStatus
    experience: int

