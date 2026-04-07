from abc import ABC, abstractmethod
from src.domain.entities.link_entinity import Link


class LinkRepository(ABC):
    @abstractmethod
    async def create(short_id: str, url: str, count: int = 0) -> Link:
        ...

    @abstractmethod
    async def get(short_id: str) -> Link:
        ...

    @abstractmethod
    async def update(short_id: str) -> Link:
        ...

