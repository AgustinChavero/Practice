from fastapi import APIRouter
from fastapi import Request, Response
from services.user import get_all_users, get_user_by_query

router = APIRouter()


@router.get("/users", tags=["users"])
async def endpoint(req: Request, res: Response):
    return await get_all_users(req, res)


@router.get("/users/{id}", tags=["users"])
async def endpoint():
    return await get_user_by_query()
