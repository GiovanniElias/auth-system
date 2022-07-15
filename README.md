# Authentication System

This is a basic version of a JWT based authentication system. It includes registration, login and session token validation.

## How it works

There are three resources: login, register and validate.

#### Login
Login supports a json object as a request body. After processing the request information, the client will be getting a response that contains an erorr message, if the request is badly formed or the user does not exist,
or a session token if the user does exist in the database.

> **Request object**
```json
{
  "email": "email@email.com",
  "password": "password"
 }
```
> **Login success response**
```json
{
    "body": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTc4OTQzMzgsImV4cCI6MTY1NzkzNzUzOCwidXNyIjoicGlub0BnbWFpbC5jb20iLCJwd2QiOiI4OTBhM2E5OTE3M2Q0ZmRkODg4MmIzMjkxYzM3Zjk0Mjo3M2VhY2FhOWM3MjE2ZmIwODk5MGQwODcxZTBlYjE3YjZmMWM0NzFlNjA1ZmVlNGI0NDg2ZWMwMjE3M2Q4OTBlIn0.        4otSzh-XhMaH_oOP6hwQqt4qUqg4cmjKLjNVI8jEtAs"
    },
    "status_code": 200
}
```

> **Login failure response**
```json
{
    "body": {
        "error": "Wrong password. Check again please."
    },
    "status_code": 403
}

```

#### Register

Register supports a json object as a request body. After processing the request information, the password is encrypted, and uuid is associated with the new user,
the client will be getting a response informing that a new user has been created.

> **Request object**
```json
{
  "email": "email@email.com",
  "password": "password",
  "confirm_password":"confirm_password"  
 }
```

> **Registration response**
> 
```json
{
    "body": {
        "created_at": 1657896013,
        "email": "email@gmail.com",
        "id": "7b93a78a99814849ad7c6a447f3ec247",
        "password": "c60555074f9743beaa4f3b67cd9ed2b1:2a3b40b1f276b950eed89cde1fd8c4af26f91c847245a62ae756c3cd4f86f39f",
        "status": 1
    },
    "status_code": 200
}
```

#### Validate

Validate elaborates the request cookies, finds the session token and tries to decode it. If decoding fails, the token is invalid, has invalid signature or has expired.
Otherwise the token will be authenticated. The service will output the folloing response:

> **Validation Response**
```json
{
    "body": {
        "message": "Token autheticated.",
        "user_id": "email@gmail.com"
    },
    "status_code": 200
}
```
