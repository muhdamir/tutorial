from fastapi import APIRouter

eddy_router = APIRouter(
    prefix="/eddy",
    tags=["Eddy punya api"]
)


@eddy_router.get("/apa")
def get_eddy():
    return "hahaha"