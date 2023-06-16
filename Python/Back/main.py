# python -m uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI
from routers import user
from database.db import db

app = FastAPI()

app.include_router(user.router)


@app.get("/")
async def read_root():
    ref = db.reference('todos')
    todos = ref.get()
    if todos is None:
        return []
    return todos

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)


""" @app.get("/")
async def read_root():
    data = ref.get()
    return {"data": data}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000) """
