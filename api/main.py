from fastapi import FastAPI
from routes import targets

app = FastAPI(title="devops-lab")

app.include_router(targets.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}


