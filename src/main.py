from fastapi import FastAPI, Response, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import uuid4
from typing import List
from .endpoints import contributor
from .database import Base, engine, SessionLocal
from . import models, schemas, upload

app = FastAPI(
    title="Mozfest Backend",
    description="FastAPI + Postgres + Cloudinary",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json",
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables on startup (use Alembic in prod)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Include contributor router
app.include_router(contributor.router)

# Root endpoints
@app.get("/")
def root():
    return {"message": "MozFest API – see /docs for Swagger"}

# Explicit health/HEAD handlers for platforms that probe with HEAD
@app.head("/", include_in_schema=False)
def head_root():
    return Response(status_code=200)

@app.get("/health", include_in_schema=False)
def healthz():
    return {"status": "ok"}


# ========== CONTRIBUTORS ==========
@app.get("/api/mock/contributors", response_model=List[schemas.ContributorBasicOut], tags=["mock"])
def list_contributors(db: Session = Depends(get_db)):
    """Get all contributors with basic info: name, country, series_id, and mosaic_url only"""
    return db.query(models.Contributor).order_by(models.Contributor.created_at.desc()).all()

@app.get("/api/mock/contributors/{contributor_id}", response_model=schemas.ContributorBasicOut, tags=["mock"])
def get_contributor(contributor_id: int, db: Session = Depends(get_db)):
    """Get a specific contributor with basic info: name, country, series_id, and mosaic_url only"""
    contributor = db.get(models.Contributor, contributor_id)
    if not contributor:
        raise HTTPException(status_code=404, detail="Contributor not found")
    return contributor


# ========== STORIES ==========
@app.get("/api/mock/stories", response_model=List[schemas.StoryOut], tags=["mock"])
def list_stories(db: Session = Depends(get_db)):
    """Get all stories"""
    return db.query(models.Story).order_by(models.Story.created_at.desc()).all()

@app.post("/api/mock/stories", response_model=schemas.StoryOut, tags=["mock"])
def create_story(
    title: str,
    name: str,
    occupation: str,
    story: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """Create a new story with image upload"""
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


# ========== TILE GRADIENTS ==========
@app.get("/api/mock/tile_gradients", response_model=List[schemas.TileGradientOut], tags=["mock"])
def list_tile_gradients(db: Session = Depends(get_db)):
    """Get all tile gradients"""
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

@app.post("/api/mock/tile_gradients", response_model=schemas.TileGradientOut, tags=["mock"])
def create_tile_gradient(payload: schemas.TileGradientCreate, db: Session = Depends(get_db)):
    """Create a new tile gradient"""
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
