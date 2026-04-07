from dataclasses import dataclass

@dataclass
class Link:
    short_id: str
    url: str
    count: int

    