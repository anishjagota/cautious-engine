# IP Address of Your Working API

- **Public IP**: `http://35.193.33.177:5000`
- **Endpoint Path**: `/api/time?city=London`
- **Full Working URL**:  http://35.193.33.177:5000/api/time?city=London



> **NOTE**: You **must include this header** in your request to get a valid response: Authorization: Bearer supersecrettoken123



---

## Example (Command to Test API)

```bash
curl -H "Authorization: Bearer supersecrettoken123" \
"http://35.193.33.177:5000/api/time?city=London"

Expected JSON Response:
{
  "city": "London",
  "local_time": "2025-04-16 14:01:09",
  "utc_offset": "+01:00"
}

Example If City Not Found:
{
  "error": "SomeCity not found in database"
}

Example If Missing Token:
{
  "error": "Unauthorized"
}










