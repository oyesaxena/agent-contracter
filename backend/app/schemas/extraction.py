from pydantic import BaseModel
from typing import Optional


class ExtractionOutput(BaseModel):

    parties: list[str]

    effective_date: Optional[str]

    expiration_date: Optional[str]

    contract_value: Optional[str]

    obligations: list[str]