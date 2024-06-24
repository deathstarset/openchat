from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config.settings import settings

database_url = settings.DATABASE_URL
engine = create_async_engine(database_url, echo=False)

async_session = async_sessionmaker(bind=engine, autoflush=False, class_=AsyncSession)
