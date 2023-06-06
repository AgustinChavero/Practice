from fastapi import Request, Response


async def get_all_users(req: Request, res: Response):
    try:
        res.status_code = 200
        return "Aca tenes todos los usuarios"
    except Exception as inner_error:
        res.status_code = 400
        return {"messsage": str(inner_error)}


async def get_user_by_query(req: Request, res: Response):
    try:
        res.status_code = 200
        return "Aca tenes los usuarios por query"
    except Exception as inner_error:
        res.status_code = 400
        return {"message": str(inner_error)}
