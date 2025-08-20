from fastapi import FastAPI
from api.routes import targets

app = FastAPI(title="devops-lab")

app.include_router(targets.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}


# @app.post("/targets")
# async def create_target(payload: dict):
#     # Stub: espera {"url": "...">
#     return {"message": "Target received", "payload": payload}


# @app.get("/results")
# async def get_results(
#     target_id: int = Query(..., description="Target ID"),
#     limit: int = Query(50, description="Max results"),
# ):
#     # Stub: retorna parâmetros recebidos
#     return {"target_id": target_id, "limit": limit, "results": []}


# # Outras rotas stub
# @app.delete("/targets/{id}")
# async def delete_target(id: int):
#     return {"message": f"Target {id} deleted (stub)"}


# @app.get("/status/{id}")
# async def get_status(id: int):
#     return {"id": id, "status": "stub"}


# @app.on_event("startup")
# async def startup_event():
#     # Esqueleto para variáveis e lista de targets
#     CHECK_INTERVAL_SECONDS = 60
#     TARGETS_ENABLED = [
#         {"id": 1, "url": "http://example.com", "enabled": True},
#         {"id": 2, "url": "http://example.org", "enabled": True},
#     ]
#     CHECK_TIMEOUT_SECONDS = 5
#     # Não iniciar loop/agendador

