from fastapi import APIRouter
from app.services.crawl_service import google_crawl_image, crawl_image
from app.services.handle_image_service import handle_convert_base64
from pydantic import BaseModel
from fastapi import HTTPException
from app.models.ImageInfo import ImageInfo
from app.services.handle_image_service import HandleImageService

class QueryCrawlRequest(BaseModel):
    query: str
    
class QueryRequest(BaseModel):
    listImage: list[str]
    
class QueryRequestPushImage(BaseModel):
    listImage: list[dict]
    
router = APIRouter()

imageService = HandleImageService()

@router.post("/google-image")
async def google_image_endpoint(request: QueryCrawlRequest):
    query = request.query
    if not query:
        raise HTTPException(status_code=400, detail="query is required")
    result = await google_crawl_image(query)
    return result

@router.post("/crawl-image")
async def crawl_image_endpoint(request: QueryCrawlRequest):
    query = request.query
    if not query:
        raise HTTPException(status_code=400, detail="query is required")
    result = await crawl_image(query)
    return result

@router.post("/get-image-base64")
async def crawl_image_endpoint(request: QueryRequest):
    listImage = request.listImage
    if not listImage:
        raise HTTPException(status_code=400, detail="query is required")
    result = await handle_convert_base64(listImage)
    return result

@router.post("/push-image")
async def crawl_image_endpoint(request: QueryRequestPushImage):
    try:
        result = imageService.add_multiple_images(request.listImage)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/hello")
def read_root():
    return {"message": "Hello, World!"}