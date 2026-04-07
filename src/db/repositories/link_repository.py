from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.link_entinity import Link
from src.db.models.link_model import LinkModel
from src.domain.repositories.link_repository import LinkRepository


class SQLAlchemyLinkRepository(LinkRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    def create(self, short_id: str, url: str, count: int):
        print(short_id, url, count)
        link = LinkModel(short_id=short_id, url=url, count=count)
        self.session.add(link)
        return Link(short_id, url, count)

    async def get(self, short_id: str) -> Link | None:
        link = await self.session.scalar(
            select(LinkModel).where(LinkModel.short_id == short_id)
        )
        if not link:
            return None

        return Link(short_id=link.short_id, url=link.url, count=link.count)

    async def update(self, short_id: str):
        ...