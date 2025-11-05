from fastapi import FastAPI, Response
from .endpoints import contributor, mock
from .database import Base, engine

app = FastAPI(
    title="Mozfest Backend",
    description="FastAPI + Postgres + Cloudinary",
    version="0.1.0",
)

# Create tables on startup (use Alembic in prod)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(contributor.router)
app.include_router(mock.router)

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
