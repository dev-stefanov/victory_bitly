from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from src.api.dependencies.link_depends import get_link_uc, create_link_uc, get_link_count_uc
from src.domain.expections.link_exeptions import LinkNotFound
from src.api.schemas.link_schema import LinkSchema

router = APIRouter()

@router.post('/shorten', status_code=status.HTTP_201_CREATED)
async def shorten_url(url: str, uc=Depends(create_link_uc)):
    link = await uc.execute(url)
    return {'short_id': link.short_id}
 
@router.get('/{short_id}', response_model=LinkSchema)
async def original_redirected(short_id: str, uc_get=Depends(get_link_uc)):
    try:
        link = await uc_get.execute(short_id)
        return RedirectResponse(url=link.url)
    except LinkNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Link not found')


@router.get('/stats/{short_id}')
async def count_redirected(short_id: str, uc=Depends(get_link_count_uc)):
    try:
        link = await uc.execute(short_id)
        return {'count': link.count}
    except LinkNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Link not found')