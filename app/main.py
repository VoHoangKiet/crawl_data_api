from fastapi import FastAPI
from app.routes import user, crawl_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Chỉ định origin được phép
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả phương thức (GET, POST, v.v.)
    allow_headers=["*"],  # Cho phép tất cả header
)

# app.include_router(user.router, prefix="/api")
app.include_router(crawl_image.router, prefix="/crawl", tags=["Crawl"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)