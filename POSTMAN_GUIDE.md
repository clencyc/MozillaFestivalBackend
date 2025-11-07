# 📮 Postman Collection for MozFest Backend API

This folder contains Postman collection and environment files for testing the MozFest Backend API.

## 📁 Files

- `postman_collection.json` - Complete API collection with all endpoints
- `postman_environment.json` - Environment variables for different environments

## 🚀 Quick Start

### Step 1: Import Collection

1. Open Postman
2. Click **Import** button (top left)
3. Select `postman_collection.json`
4. Click **Import**

### Step 2: Import Environment

1. Click **Import** again
2. Select `postman_environment.json`
3. Click **Import**

### Step 3: Select Environment

1. Click the environment dropdown (top right)
2. Select **MozFest Backend Environments**

### Step 4: Switch Between Environments

To test **production**:
- Use `{{base_url}}` in requests
- Or manually set to: `https://girlswhoml.onrender.com`

To test **local**:
- Change `base_url` variable to `{{local_url}}`
- Or manually set to: `http://localhost:8000`

## 📚 Collection Structure

```
MozFest Backend API
├── Health & Status (3 requests)
│   ├── Root - Welcome Message
│   ├── Health Check
│   └── OpenAPI Schema
│
├── Contributors (Full CRUD) (2 requests)
│   ├── Create Contributor
│   └── Get Contributor (Full Details)
│
├── Mock API - Contributors (2 requests)
│   ├── List All Contributors (Basic)
│   └── Get Single Contributor (Basic)
│
├── Mock API - Stories (2 requests)
│   ├── List All Stories
│   └── Create Story
│
└── Mock API - Tile Gradients (2 requests)
    ├── List All Tile Gradients
    └── Create Tile Gradient
```

**Total: 11 requests**

## 🎯 Testing Each Endpoint

### Health & Status

#### 1. Root - Welcome Message
- **Method:** GET
- **URL:** `{{base_url}}/`
- **Expected:** 200 OK with welcome message

#### 2. Health Check
- **Method:** GET
- **URL:** `{{base_url}}/health`
- **Expected:** 200 OK with status

#### 3. OpenAPI Schema
- **Method:** GET
- **URL:** `{{base_url}}/openapi.json`
- **Expected:** Complete OpenAPI spec

---

### Contributors (Full CRUD)

#### 1. Create Contributor
- **Method:** POST
- **URL:** `{{base_url}}/contributors/`
- **Body:** Form-data with:
  - `name`: Contributor name
  - `country`: Country name
  - `series_id`: (optional) Series ID
  - `mosaic`: Image file
  - `screenshot`: Image file

**Note:** You need to upload actual image files for this request.

#### 2. Get Contributor (Full Details)
- **Method:** GET
- **URL:** `{{base_url}}/contributors/1`
- **Returns:** Full contributor details including screenshots

---

### Mock API - Contributors

#### 1. List All Contributors (Basic)
- **Method:** GET
- **URL:** `{{base_url}}/api/mock/contributors`
- **Returns:** Array with basic contributor info

#### 2. Get Single Contributor (Basic)
- **Method:** GET
- **URL:** `{{base_url}}/api/mock/contributors/1`
- **Returns:** Single contributor with basic info only

---

### Mock API - Stories

#### 1. List All Stories
- **Method:** GET
- **URL:** `{{base_url}}/api/mock/stories`
- **Returns:** Array of all stories

#### 2. Create Story
- **Method:** POST
- **URL:** `{{base_url}}/api/mock/stories`
- **Body:** Form-data with:
  - `title`: Story title
  - `name`: Person's name
  - `occupation`: Person's occupation
  - `story`: Story text
  - `image`: Image file

**Note:** You need to upload an actual image file.

---

### Mock API - Tile Gradients

#### 1. List All Tile Gradients
- **Method:** GET
- **URL:** `{{base_url}}/api/mock/tile_gradients`
- **Returns:** Array of gradient configurations

#### 2. Create Tile Gradient
- **Method:** POST
- **URL:** `{{base_url}}/api/mock/tile_gradients`
- **Body:** JSON with:
```json
{
    "from_color": "#FF6B6B",
    "to_color": "#4ECDC4",
    "border": "#FFFFFF",
    "glow": "#FFD93D"
}
```

---

## 🔧 Environment Variables

The collection uses the following variables:

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `base_url` | `https://girlswhoml.onrender.com` | Production API URL |
| `local_url` | `http://localhost:8000` | Local development URL |
| `contributor_id` | `1` | Sample contributor ID for testing |

### How to Change Base URL

**Method 1: Environment Variable**
1. Click environment dropdown
2. Click edit icon (⚙️)
3. Change `base_url` value
4. Save

**Method 2: In Request**
- Manually replace `{{base_url}}` with your URL

---

## 🧪 Automatic Tests

The collection includes automatic tests that run after each request:

### Global Tests (Applied to all requests)
- ✅ Status code is successful (200, 201, or 204)
- ✅ Response time is under 3 seconds

### Custom Tests
You can add more tests in the **Tests** tab of each request.

---

## 📝 Example Usage

### Testing Production API

1. Set environment to **MozFest Backend Environments**
2. Ensure `base_url` is `https://girlswhoml.onrender.com`
3. Click **Send** on any request
4. Check response in the body panel

### Testing Local Development

1. Start your local server: `uvicorn src.main:app --reload`
2. In Postman environment, change `base_url` to `{{local_url}}`
3. Click **Send** on any request
4. Verify against your local database

---

## 🎨 Tips & Tricks

### Run Entire Collection
1. Click on collection name
2. Click **Run** button
3. Select requests to run
4. Click **Run MozFest Backend API**

### Save Responses as Examples
1. Send a request
2. Click **Save Response** dropdown
3. Click **Save as example**
4. This helps document expected responses

### Use Variables in Tests
```javascript
// Save response data for next request
pm.environment.set("contributor_id", pm.response.json().id);
```

### Chain Requests
1. Create a contributor
2. Save the ID to environment
3. Use that ID in "Get Contributor" request

---

## 🐛 Troubleshooting

### Issue: CORS Error
**Solution:** CORS is enabled, but ensure your server is running.

### Issue: 404 Not Found
**Solution:** 
- Check if endpoint exists in deployed version
- Verify contributor/story ID exists

### Issue: 502 Bad Gateway on Image Upload
**Solution:**
- Check Cloudinary credentials in `.env`
- Verify image file size (< 10MB recommended)
- Check image format (JPG, PNG supported)

### Issue: 422 Validation Error
**Solution:**
- Check all required fields are provided
- Verify data types match expectations

---

## 📖 Additional Resources

- **API Documentation:** `API_MOCK_ENDPOINTS.md`
- **Live Swagger Docs:** https://girlswhoml.onrender.com/docs
- **OpenAPI Spec:** https://girlswhoml.onrender.com/openapi.json

---

## 🔄 Updating Collection

When API changes:

1. Re-export from OpenAPI spec:
   ```bash
   curl https://girlswhoml.onrender.com/openapi.json > openapi.json
   ```

2. Or manually update:
   - Add new requests
   - Update URLs
   - Modify request bodies
   - Export collection
   - Replace `postman_collection.json`

---

## 📤 Sharing Collection

### Option 1: Share Files
Send these files to team members:
- `postman_collection.json`
- `postman_environment.json`

### Option 2: Postman Workspace
1. Publish to Postman workspace
2. Share workspace link with team

### Option 3: Generate Link
1. Right-click collection
2. Select **Share Collection**
3. Copy share link

---

*Last Updated: November 7, 2025*
