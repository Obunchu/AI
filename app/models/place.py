from sqlalchemy import Column, Integer, Text, Float, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Text, unique=True)
    title = Column(Text, nullable=False)
    address = Column(Text)
    area_code = Column(Text)
    category = Column(Text)
    map_x = Column(Float)
    map_y = Column(Float)
    overview = Column(Text)
    created_at = Column(DateTime, server_default=func.now())