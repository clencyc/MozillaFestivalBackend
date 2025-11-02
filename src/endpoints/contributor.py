from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from .. import models, schemas, database, upload

router = APIRouter(prefix="/contributors", tags=["contributors"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ContributorOut)
def create_contributor(
    name: str = Form(...),
    country: str = Form(...),
    series_id: str = Form(None),
    mosaic: UploadFile = File(...),
    screenshot: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # 1. Upload images
    try:
        mosaic_url, _ = upload.upload_image(mosaic, folder="mosaics")
        screenshot_url, _ = upload.upload_image(screenshot, folder="screenshots")
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    # 2. Persist
    db_contrib = models.Contributor(
        name=name,
        country=country,
        series_id=series_id,
        mosaic_url=mosaic_url,
        screenshot_url=screenshot_url,
    )
    db.add(db_contrib)
    db.commit()
    db.refresh(db_contrib)

    return db_contrib

@router.get("/{contrib_id}", response_model=schemas.ContributorOut)
def get_contributor(contrib_id: int, db: Session = Depends(get_db)):
    contrib = db.get(models.Contributor, contrib_id)
    if not contrib:
        raise HTTPException(404, "Contributor not found")
    return contrib

