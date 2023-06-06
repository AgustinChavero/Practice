# python -m uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI
from routers import user


app = FastAPI()

app.include_router(user.router)

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
