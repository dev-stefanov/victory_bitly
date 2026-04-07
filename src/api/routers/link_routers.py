from fastapi import APIRouter, Depends, HTTPException, status

from src.api.dependencies.link_depends import get_link_uc
from src.domain.expections.link_exeptions import LinkNotFound

router = APIRouter()

@router.post('/shorten')
async def shorten_url():
    return ...


@router.get('/{short_id}')
async def original_redirected(short_id: str, uc=Depends(get_link_uc)):
    try:
        return await uc.execute(short_id)
    except LinkNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Link not found')


@router.get('/stats/{short_id}')
async def count_redirected(short_id: str):
    return ...