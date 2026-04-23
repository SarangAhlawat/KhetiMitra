from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.models.user import User
from app.schemas.user_schema import (
    UserCreate,
    UserLogin
)


# router = APIRouter()
router = APIRouter(

    prefix="",

    tags=["Authentication"]

)


# Register User

@router.post("/register")

def register_user(

    user: UserCreate,
    db: Session = Depends(get_db)

):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = hash_password(
        user.password
    )

    db_user = User(

        username=user.username,
        password_hash=hashed_password

    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return {

        "message": "User registered successfully"
    }


# Login User

@router.post("/login")

def login_user(

    user: UserLogin,
    db: Session = Depends(get_db)

):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not verify_password(
        user.password,
        db_user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(

        data={
            "sub": db_user.username
        }

    )

    return {

        "access_token": access_token,
        "token_type": "bearer"

    }