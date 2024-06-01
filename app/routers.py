from fastapi import APIRouter

router = APIRouter(
    prefix='/api',
    tags=['Основной']
)


@router.get('')
async def index() -> dict:
    return {'name': 'Slava'}
