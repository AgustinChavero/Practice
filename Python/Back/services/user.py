from fastapi import Request, Response
from models.user import UserToRegister, User
from database.db import db
from datetime import datetime
from fastapi.responses import JSONResponse


async def new_user(req: Request, res: Response):
    try:
        data: UserToRegister = await req.json()
        data_formatted = {
            **data,
            "createdAt": datetime.now().isoformat()
        }

        snapshot = db.collection("users").where(
            "email", "==", data.email).get()

        # fijate de hacer un for
        if snapshot:
            raise Exception("El correo electrónico ya está registrado")

        new = await db.reference("users").push(data_formatted)
        return JSONResponse(content={"message": f"Usuario creado correctamente. Nombre: {data_formatted['first_name']}"},
                            status_code=200)
    except Exception as inner_error:
        return JSONResponse(content={"message": str(inner_error)},
                            status_code=400)


async def get_all_users(req: Request, res: Response):
    try:
        users_ref = db.collection("users")
        users_docs = users_ref.get()

        usuarios = []
        for doc in users_docs:
            usuario = doc.to_dict()
        usuario["id"] = doc.id
        usuarios.append(usuario)

        return {"usuarios": usuarios}
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
