from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from app.core.config import settings
from app.db.base import Base



engine = create_async_engine(
    url= settings.DB_URL,
    echo = True
)

new_session = async_sessionmaker(engine,
    expire_on_commit= settings.DB_EXPIRE_ON_COMMIT,
    autoflush= settings.DB_AUTOFLUSH,
)

async def create_table():
    print("Проверка метаданных:", list(Base.metadata.tables.keys()))
    
    async with engine.begin() as conn:
        print("Удаление таблиц...")
        await conn.run_sync(Base.metadata.drop_all)
        print("Создание таблиц...")
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()