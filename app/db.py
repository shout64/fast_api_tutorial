from collections.abc                import AsyncGenerator
from sqlalchemy                     import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio         import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm                 import DeclarativeBase, relationship
import uuid

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
