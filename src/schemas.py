from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

# ---------- Contributor ----------
class ContributorCreate(BaseModel):
    model_config = ConfigDict()  # Default; add populate_by_name=True if needed for aliases
    
    name: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    series_id: Optional[str] = None

class ContributorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # v2 ORM mode replacement
    
    id: int
    name: str
    country: str
    series_id: Optional[str]
    mosaic_url: Optional[HttpUrl]
    screenshot_url: Optional[HttpUrl]
    created_at: datetime

class ContributorBasicOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int  # Added: Matches route usage
    name: str
    country: str
    series_id: Optional[str]
    mosaic_url: Optional[HttpUrl]

# ---------- Stories ----------
class StoryCreate(BaseModel):
    model_config = ConfigDict()
    
    title: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    occupation: str = Field(..., min_length=1)
    story: str = Field(..., min_length=1)

class StoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    title: str
    name: str
    occupation: str
    story: str
    image_url: HttpUrl
    created_at: datetime

# ---------- Tile Gradients ----------
class TileGradientCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)  # v2 replacement for aliases
    
    from_: str = Field(..., alias="from_color")  # Adjust alias to match your DB field
    to_: str = Field(..., alias="to_color")
    border: str
    glow: str

class TileGradientOut(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
    
    from_: str = Field(alias="from_color")  # No ... if optional in DB
    to_: str = Field(alias="to_color")
    border: str
    glow: str