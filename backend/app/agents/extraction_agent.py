from app.schemas.extraction import (
    ExtractionOutput
)

from app.prompts.extraction import (
    EXTRACTION_PROMPT
)

from app.services.llm.openai_provider import (
    llm
)


structured_llm = llm.with_structured_output(
    ExtractionOutput
)


async def extraction_agent(state):

    result = await structured_llm.ainvoke(
        EXTRACTION_PROMPT.format(
            document=state["document_text"][:12000]
        )
    )

    state["extraction"] = (
        result.model_dump()
    )

    state["current_node"] = (
        "extraction"
    )
    if "execution_logs" not in state:
        state["execution_logs"] = []
    state["execution_logs"].append({
    "node": "extraction",
    "output": result.model_dump()
    })

    return state