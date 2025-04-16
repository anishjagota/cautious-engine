#  Capital Time API

This API returns the current local time and UTC offset for a given capital city. It also includes a protected route requiring a valid token to access secret data.

---

##  Hosted Public Endpoint

** Base URL:**  
http://35.193.33.177:5000

>  All endpoints require an `Authorization` header to access. Unauthorized requests will return a 401 error.

---

##  Endpoints

### `/api/time`

Returns the local time and UTC offset for a capital city.

- **Method:** `GET`
- **Query Param:** `city` (case-sensitive)  
  - Valid cities: `London`, `Paris`, `New York`, `Tokyo`, `Delhi`, `Canberra`

---

### Example Request

```bash
curl -H "Authorization: Bearer supersecrettoken123" \
"http://35.193.33.177:5000/api/time?city=London"

Example Response:
{
  "city": "London",
  "local_time": "2025-04-16 14:01:09",
  "utc_offset": "+01:00"
}

 If City Not Found:
{
  "error": "SomeCity not found in database"
}

/api/secure-data
Protected route that returns secret content.

Method: GET

Headers Required:
Authorization: Bearer supersecrettoken123

 Example Request

curl -H "Authorization: Bearer supersecrettoken123" \
"http://35.193.33.177:5000/api/secure-data"

 Example Response

{
  "secret": "This is protected info!"
}

 Missing Token Response

{
  "error": "Unauthorized"
}

Use this header:
Authorization: Bearer supersecrettoken123

 How to Run Locally (for grading/debug)
1. Clone the repo

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python3 app.py


