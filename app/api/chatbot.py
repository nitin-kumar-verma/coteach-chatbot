from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from app.core.models import AskResponse
from app.core.process import process

from typing import Optional
import logging

router = APIRouter()



@router.post("/ask/", response_model=AskResponse)
async def ask(
    converstion_id: Optional[str] = Form(None),
    query: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
):
    #ensure query is not empty
    if not query:
        raise HTTPException(status_code=400, detail="No query provided.")
    
    image_content=None

    #try to get image bytes if image provided
    if image:
        try:
            image_content = await image.read()
        except Exception as e:
            logging.error(f"Error processing image: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    try:
        return process(
            query=query,
            image_content=image_content,
            conversation_id=converstion_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
