import uvicorn
from fastapi import FastAPI, Request

from src.core.config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ip")
async def get_ip(request: Request):
    return {
        "ip": request.headers.get("X-Real-IP"),
        "real_ip": request.headers.get("X-Forwarded-For"),
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True
    )
