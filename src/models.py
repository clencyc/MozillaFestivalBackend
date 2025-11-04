from sqlalchemy import Column, Integer, String, DateTime, Text, func
from .database import Base

class Contributor(Base):
    __tablename__ = "contributors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    series_id = Column(String, index=True)
    mosaic_url = Column(String)
    screenshot_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Story(Base):
    __tablename__ = "stories"

    # String id as requested (we will use UUID strings)
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    story = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class TileGradient(Base):
    __tablename__ = "tile_gradients"

    id = Column(Integer, primary_key=True, index=True)
    from_color = Column(String, nullable=False)
    to_color = Column(String, nullable=False)
    border = Column(String, nullable=False)
    glow = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
