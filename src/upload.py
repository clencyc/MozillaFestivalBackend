import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.exceptions

load_dotenv()

_CONFIGURED = False

def _ensure_configured():
    global _CONFIGURED
    if _CONFIGURED:
        return
    # If already configured (e.g., via CLOUDINARY_URL), cloud_name will be truthy
    if cloudinary.config().cloud_name:
        _CONFIGURED = True
        return
    # Prefer CLOUDINARY_URL if present
    if os.getenv("CLOUDINARY_URL"):
        cloudinary.config(secure=True)
        _CONFIGURED = True
        return
    # Else, try explicit vars; do NOT raise at import time
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    api_key = os.getenv("CLOUDINARY_API_KEY")
    api_secret = os.getenv("CLOUDINARY_API_SECRET")
    if cloud_name and api_key and api_secret:
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True,
        )
        _CONFIGURED = True


def upload_image(file, folder: str = "mozdest"):
    """Upload a FastAPI UploadFile → Cloudinary, return secure_url & public_id"""
    _ensure_configured()
    if not cloudinary.config().cloud_name:
        raise RuntimeError(
            "Cloudinary not configured. Set CLOUDINARY_URL or CLOUDINARY_CLOUD_NAME/API_KEY/API_SECRET."
        )
    try:
        result = cloudinary.uploader.upload(
            file.file,
            folder=folder,
            resource_type="image",
            overwrite=True,
            transformation=[{"width": 800, "crop": "limit"}],
        )
        return result.get("secure_url"), result.get("public_id")
    except cloudinary.exceptions.Error as e:
        # Surface a concise, actionable error up the stack
        raise RuntimeError(f"Cloudinary upload error: {e}")
