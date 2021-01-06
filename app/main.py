from fastapi import FastAPI

from users.urls import router as users_router
from admins.urls import router as admins_router

app = FastAPI()


app.include_router(users_router)
app.include_router(admins_router)
