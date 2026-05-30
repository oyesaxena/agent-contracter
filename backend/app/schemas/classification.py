from pydantic import BaseModel


class ClassificationOutput(BaseModel):

    document_type: str

    confidence: float

    reasoning: str