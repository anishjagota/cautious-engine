#  Capital Time API

This API returns the current local time and UTC offset for a given capital city.  
It requires a valid token to access both the time and secret data routes.

---

# IP Address of Your Working API

- **Public IP**: `http://35.193.33.177:5000`
- **Endpoint Path**: `/api/time?city=London`





###  To Get Time for a Capital City

Use this endpoint format:



```md
http://ip-address:5000/api/time?city=CityName
```

For example on GCP:
```md
http://35.193.33.177:5000/api/time?city=London
```


---

###  Authorization Required

Every request must include a valid token in the header:

**Authorization:**
```md
 Bearer supersecrettoken123
```


---

###  Example CURL Request

```bash
curl -H "Authorization: Bearer supersecrettoken123" \
"http://35.193.33.177:5000/api/time?city=London"
```

✅ Expected JSON Response
```bash
{
  "city": "London",
  "local_time": "2025-04-16 14:01:09",
  "utc_offset": "+01:00"
}
```

❌ Invalid City Example
```bash
{
  "error": "SomeCity not found in database"
}
```
❌ Missing Token Example
```bash
{
  "error": "Unauthorized"
}
```








