from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncio
from tables import Base
from dotenv import load_dotenv
import os
import nest_asyncio

nest_asyncio.apply()


# Load ENV variables
load_dotenv()

# Engine
engine = create_async_engine(os.getenv("DB_URL"), echo=True)
sess = async_sessionmaker(bind=engine, expire_on_commit=False)


# Create DB
async def createDB():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Connected to DB...")
    await engine.dispose()


# asyncio.run(createDB())
loop = asyncio.get_event_loop()
loop.run_until_complete(createDB())
