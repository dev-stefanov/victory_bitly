from src.domain.repositories.link_repository import LinkRepository
from src.domain.entities.link_entinity import Link
from src.domain.expections.link_exeptions import LinkNotFound
from src.domain.utils import generate_code


class CreateLink:
    def __init__(self, link_repo: LinkRepository):
        self.link_repo = link_repo

    def execute(self, url: str, count: int = 0) -> Link: 
        link = self.link_repo.create(generate_code(), url, count)
        return link


class GetLink:
    def __init__(self, link_repo: LinkRepository):
        self.link_repo = link_repo

    async def execute(self, short_id: str) -> Link:
        link = await self.link_repo.get(short_id)
        if not link:
            raise LinkNotFound
        
        return link
        

class UpdateLink:
    def __init__(self, link_repo: LinkRepository):
        self.link_repo = link_repo

    async def execute(self) -> Link:
        ...

