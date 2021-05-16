from fastapi import APIRouter

from .router.users import router as user_router

router = APIRouter()


router.include_router(user_router, tags=["Users"], prefix="/user")
