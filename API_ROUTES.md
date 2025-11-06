# MozFest Backend API Routes

All routes are now consolidated in `src/main.py` for easier documentation and maintenance.

## 📍 All Available Endpoints

### 🏠 Root & Health
- `GET /` - Welcome message
- `GET /health` - Health check

---

### 👥 Contributors (Full CRUD)
**Tag:** `contributors`

- `POST /contributors/` - Create new contributor with mosaic and screenshot uploads
  - **Form Data:**
    - `name` (required)
    - `country` (required)
    - `series_id` (optional)
    - `mosaic` (file, required)
    - `screenshot` (file, required)
  - **Returns:** Full contributor object

- `GET /contributors/{contrib_id}` - Get contributor with full details
  - **Returns:** Full contributor object including screenshots

---

### 🔍 Mock Endpoints - Contributors (Basic Info)
**Tag:** `mock`

- `GET /api/mock/contributors` - List all contributors (basic info only)
  - **Returns:** Array of contributors with: `name`, `country`, `series_id`, `mosaic_url`

- `GET /api/mock/contributors/{contributor_id}` - Get specific contributor (basic info only)
  - **Returns:** Contributor with: `name`, `country`, `series_id`, `mosaic_url`

---

### 📖 Mock Endpoints - Stories
**Tag:** `mock`

- `GET /api/mock/stories` - List all stories
  - **Returns:** Array of story objects

- `POST /api/mock/stories` - Create new story
  - **Form Data:**
    - `title` (required)
    - `name` (required)
    - `occupation` (required)
    - `story` (required)
    - `image` (file, required)
  - **Returns:** Created story object

---

### 🎨 Mock Endpoints - Tile Gradients
**Tag:** `mock`

- `GET /api/mock/tile_gradients` - List all tile gradients
  - **Returns:** Array of gradient objects

- `POST /api/mock/tile_gradients` - Create new tile gradient
  - **JSON Body:**
    ```json
    {
      "from": "string",
      "to": "string",
      "border": "string",
      "glow": "string"
    }
    ```
  - **Returns:** Created gradient object

---

## 📚 Documentation URLs

- **Swagger UI:** `http://localhost:8000/docs`
- **OpenAPI JSON:** `http://localhost:8000/openapi.json`
- **Downloaded Docs:**
  - `openapi.json` - OpenAPI spec (JSON format)
  - `openapi.yaml` - OpenAPI spec (YAML format)
  - `swagger-docs.html` - Standalone Swagger UI

---

## 🏗️ Project Structure

```
src/
├── main.py              ✅ ALL ROUTES CONSOLIDATED HERE
├── models.py            - Database models
├── schemas.py           - Pydantic schemas
├── upload.py            - Cloudinary upload utilities
├── database/
│   └── __init__.py      - Database configuration
└── endpoints/
    └── (empty now - all routes moved to main.py)
```

---

## 🚀 Deployment Checklist

1. ✅ All routes consolidated in `main.py`
2. ✅ No external router imports needed
3. ✅ Documentation auto-generated from code
4. ✅ Ready to commit and deploy

### To Deploy:
```bash
git add .
git commit -m "Consolidate all API routes in main.py"
git push origin main
```

---

## 📝 Notes

- **Contributors endpoints**: Two versions available
  - `/contributors/*` - Full CRUD with all fields
  - `/api/mock/contributors/*` - Read-only with limited fields
  
- **Mock endpoints**: Prefixed with `/api/mock/` for testing/demo purposes

- **All endpoints**: Automatically documented at `/docs`
