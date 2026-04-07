from src.domain.repositories.link_repository import LinkRepository
from src.domain.entities.link_entinity import Link
from src.domain.expections.link_exeptions import LinkNotFound


class CreateLink:
    ...


class GetLink:
    def __init__(self, link_repo: LinkRepository):
        self.link_repo = link_repo

    async def execute(self, short_id: str) -> Link:
        link = await self.link_repo.get(short_id)
        if not link:
            raise LinkNotFound
        
        return link
        

class UpdateLink:
    ...

