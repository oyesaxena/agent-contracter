from fastapi import FastAPI

from app.api.routes.document import (
    router as document_router
)

app = FastAPI(
    title="Document Automation Agent"
)

app.include_router(
    document_router
)