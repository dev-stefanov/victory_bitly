from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.db_depends import get_async_db
from src.db.repositories.link_repository import SQLAlchemyLinkRepository
from src.services.usecases.link_usecases import (
    GetLink,
    CreateLink,
    UpdateLink,
)

def get_link_repo(session: AsyncSession = Depends(get_async_db)):
    return SQLAlchemyLinkRepository(session)


def get_link_uc(repo=Depends(get_link_repo)):
    return GetLink(repo)

def create_link_uc(repo=Depends(get_link_repo)):
    return CreateLink(repo)

def update_link_uc(repo=Depends(get_link_repo)):
    return UpdateLink(repo)