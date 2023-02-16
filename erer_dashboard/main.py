"""
Aplicação para Dashboard do projeto Observatório.
"""
import uvicorn
from fastapi import FastAPI
from erer_dashboard.api import lote as lote_router


def create_app() -> FastAPI:
    """
    Application Initializer
    """
    application: FastAPI = FastAPI()

    application.include_router(lote_router.router, tags=["Lote"], prefix="/lote")

    return application

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3333)
