from fastapi import FastAPI

from .routers import subject_router
from .eddy import eddy_router

app = FastAPI(
    title="tutorial",
)


# @app.get(path="/contoh")
# def get_contoh():
#     return "aaa"

app.include_router(router=subject_router)
app.include_router(router=eddy_router)
