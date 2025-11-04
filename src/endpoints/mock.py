from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import uuid4
from .. import models, schemas, database, upload
from typing import List

router = APIRouter(prefix="/api/mock", tags=["mock"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Stories
@router.get("/stories", response_model=List[schemas.StoryOut])
def list_stories(db: Session = Depends(get_db)):
    return db.query(models.Story).order_by(models.Story.created_at.desc()).all()

@router.post("/stories", response_model=schemas.StoryOut)
def create_story(
    title: str,
    name: str,
    occupation: str,
    story: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        image_url, _ = upload.upload_image(image, folder="stories")
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    story_row = models.Story(
        id=str(uuid4()),
        title=title,
        name=name,
        occupation=occupation,
        story=story,
        image_url=image_url,
    )
    db.add(story_row)
    db.commit()
    db.refresh(story_row)
    return story_row

# Tile Gradients
@router.get("/tile_gradients", response_model=List[schemas.TileGradientOut])
def list_tile_gradients(db: Session = Depends(get_db)):
    rows = db.query(models.TileGradient).order_by(models.TileGradient.created_at.desc()).all()
    # Map DB fields to schema aliases
    return [
        type("Obj", (), {
            "from_": r.from_color,
            "to_": r.to_color,
            "border": r.border,
            "glow": r.glow,
        })()
        for r in rows
    ]

@router.post("/tile_gradients", response_model=schemas.TileGradientOut)
def create_tile_gradient(payload: schemas.TileGradientCreate, db: Session = Depends(get_db)):
    row = models.TileGradient(
        from_color=payload.from_,
        to_color=payload.to_,
        border=payload.border,
        glow=payload.glow,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return type("Obj", (), {
        "from_": row.from_color,
        "to_": row.to_color,
        "border": row.border,
        "glow": row.glow,
    })()