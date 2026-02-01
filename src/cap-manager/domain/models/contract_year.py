from dataclasses import dataclass

@dataclass(frozen=True)
class ContractYear:
    year: int = 0
    base_salary: int = 0
    signing_bonus_proration: int = 0
    roster_bonus: int = 0
    workout_bonus: int = 0
    other_bonus: int = 0

    def cap_hit(self) -> int:
        return(
            self.base_salary
            + self.signing_bonus_proration
            + self.roster_bonus
            + self.workout_bonus
            + self.other_bonus
        )

