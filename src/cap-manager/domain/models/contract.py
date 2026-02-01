from dataclasses import dataclass, field
from typing import Dict, Optional
from .contract_year import ContractYear

@dataclass
class Contract:
    contract_id: str
    player_id : str
    team: str
    start_year: int
    end_year: int
    years: Dict[int, ContractYear] = field(default_factory=dict) #year -> ContractYear

    def add_year(self, contract_year: ContractYear) -> None:
        if contract_year.year < self.start_year or contract_year.year > self.end_year:
            raise ValueError(
                f"ContractYear {contract_year.year} outside contract range"
                f"{self.start_year}-{self.end_year}"
            )
        self.years[contract_year.year]= contract_year

    def get_year(self, year: int) -> Optional[ContractYear]:
        return self.years.get(year)

    def cap_hit(self, year: int)-> int:
        cy = self.get_year(year)
        return 0 if cy is None else cy.cap_hit()

