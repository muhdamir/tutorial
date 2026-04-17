from importlib.resources import path
from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.coercions import name

from .db import get_session
from .entity import User
from .models import UserPost, UserResponse

subject_router = APIRouter(
    prefix="/subject",
    tags=["Subject API"],
)


@subject_router.post(
    path="/",
)
def create_user(user: UserPost) -> UserResponse:
    return UserResponse(name="haha", nombor=11, id=12)
    # return user


@subject_router.get(
    path="/",
    description="something something",
    summary="hu ha hu ha",
)
async def get_subjects():

    return "tutorial endpoints"


@subject_router.get(
    path="/another",
)
async def get_another_subjects():
    return "tutorial endpoints"


# @subject_router.get(
#     path="/sample",
# )
# async def get_sample(
#     session: Annotated[AsyncSession, Depends(get_session)],
# ) -> list[UserResponse]:
#     users = await session.scalars(select(User))
#     return users.all()


# @subject_router.post("/sample")
# async def create_sample(
#     session: Annotated[AsyncSession, Depends(get_session)],
# ): ...
