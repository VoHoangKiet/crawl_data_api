from fastapi import FastAPI
from app.routes import crawl_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crawlclient.vercel.app"],  # Cho phép các domain trên thực hiện request
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức HTTP
    allow_headers=["*"],
)

# app.include_router(user.router, prefix="/api")
app.include_router(crawl_image.router, prefix="/crawl", tags=["Crawl"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)