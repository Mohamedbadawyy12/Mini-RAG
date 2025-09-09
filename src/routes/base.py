from fastapi import FastAPI , APIRouter ,Depends
import os

from helpers.config import get_settings ,Settings


base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/") 
async def welcome(app_settings:Settings=Depends(get_settings)): 
    # عشان لو حصل ان السيتينجز دي مجتش لسبب ما ف لازم بعتمد انه يجيب السيتينجز ويتاكد من وجودها ويشتغل عليها وجبت الكلاس بتاعها عشان اعرفه ان نوعه كلاس
   
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION

    return{
        "app_name": app_name,
        "app_version": app_version
    }