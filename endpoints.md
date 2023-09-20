# Endpoints

## [POST] /send/
### Request
**Parameters:** 
- `ignore_headers` (optional): boolean, default `false`
    if `true`, ignore the headers in the request body

**Body:**
```
{
    "name": str,
    "email": str,
    "subject": str,
    "message": str
}*
```
_Note:_ `Body` may contain additional fields

### Response
**204 No Content**