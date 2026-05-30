from app.schemas.classification import (
    ClassificationOutput
)

from app.prompts.classification import (
    CLASSIFICATION_PROMPT
)

from app.services.llm.openai_provider import (
    llm
)


structured_llm = llm.with_structured_output(
    ClassificationOutput
)


async def classification_agent(state):

    result = await structured_llm.ainvoke(
        CLASSIFICATION_PROMPT.format(
            document=state["document_text"][:8000]
        )
    )

    state["classification"] = (
        result.model_dump()
    )

    state["current_node"] = (
        "classification"
    )

    state["execution_logs"].append({
    "node": "classification",
    "output": result.model_dump()
})

    return state