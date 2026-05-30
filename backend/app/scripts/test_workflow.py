import asyncio
import uuid

from app.workflows.graph import (
    workflow
)


async def main():

    state = {

        "workflow_id": str(
            uuid.uuid4()
        ),

        "tenant_id": "demo",

        "document_name": "sample.pdf",

        "document_text": """
        Vendor Agreement

        Between ABC Pvt Ltd and XYZ Pvt Ltd.

        Effective Date:
        01 Jan 2025

        Contract Value:
        $50,000
        """,

        "document_metadata": {},

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

    print(result)


asyncio.run(main())