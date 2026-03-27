from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Auth API")


class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class MessageResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


fake_users_db: dict[str, dict[str, str]] = {}


@app.post("/signup", response_model=MessageResponse)
def signup(payload: SignupRequest):
    if payload.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[payload.email] = {
        "full_name": payload.full_name,
        "password": payload.password,
    }
    return MessageResponse(message="User created successfully")


@app.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    user = fake_users_db.get(payload.email)
    if not user or user["password"] != payload.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return TokenResponse(access_token="fake-jwt-token", token_type="bearer")
