from typing import TypedDict, Dict, Any


class WorkflowState(TypedDict):

    workflow_id: str

    tenant_id: str

    document_name: str

    document_text: str

    document_metadata: Dict[str, Any]

    current_node: str

    status: str

    classification: Dict[str, Any]

    extraction: Dict[str, Any]

    validation: Dict[str, Any]

    confidence_score: float

    review_required: bool

    indexed: bool

    errors: list[str]
    execution_logs: list