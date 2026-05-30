import uuid
import tempfile

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.services.pdf_service import (
    load_pdf
)

from app.workflows.graph import (
    workflow
)

router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        temp.write(
            await file.read()
        )

        temp_path = temp.name

    pdf_data = load_pdf(
        temp_path
    )

    state = {

        "workflow_id": str(
            uuid.uuid4()
        ),

        "tenant_id": "demo",

        "document_name": file.filename,

        "document_text": pdf_data["text"],

        "document_metadata": pdf_data[
            "metadata"
        ],

        "current_node": "",

        "status": "processing",

        "classification": {},

        "extraction": {},

        "validation": {},

        "confidence_score": 0.0,

        "review_required": False,

        "indexed": False,

        "errors": []
    }

    result = await workflow.ainvoke(
        state
    )

    return result