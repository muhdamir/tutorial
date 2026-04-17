from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from .config import config

async_engine: AsyncEngine = create_async_engine(url=config.async_db_url)

async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=async_engine
)

async def get_session():
    async with async_session_factory.begin() as session:
        yield session
