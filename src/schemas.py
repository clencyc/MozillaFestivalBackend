from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List
from datetime import datetime

# ---------- Contributor ----------
class ContributorCreate(BaseModel):
    name: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    series_id: Optional[str] = None

class ContributorOut(BaseModel):
    id: int
    name: str
    country: str
    series_id: Optional[str]
    mosaic_url: Optional[HttpUrl]
    screenshot_url: Optional[HttpUrl]
    created_at: datetime

    class Config:
        from_attributes = True

class ContributorBasicOut(BaseModel):
    name: str
    country: str
    series_id: Optional[str]
    mosaic_url: Optional[HttpUrl]

    class Config:
        from_attributes = True

# ---------- Stories ----------
class StoryCreate(BaseModel):
    title: str
    name: str
    occupation: str
    story: str
    # image uploaded via UploadFile in endpoint

class StoryOut(BaseModel):
    id: str
    title: str
    name: str
    occupation: str
    story: str
    image_url: HttpUrl
    created_at: datetime

    class Config:
        from_attributes = True

# ---------- Tile Gradients ----------
class TileGradientCreate(BaseModel):
    from_: str = Field(..., alias="from")
    to_: str = Field(..., alias="to")
    border: str
    glow: str

    class Config:
        populate_by_name = True

class TileGradientOut(BaseModel):
    from_: str = Field(..., alias="from")
    to_: str = Field(..., alias="to")
    border: str
    glow: str

    class Config:
        from_attributes = True
        populate_by_name = True
