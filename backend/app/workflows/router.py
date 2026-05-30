from app.core.config import settings


def workflow_router(state):

    confidence_score = state.get(
        "confidence_score",
        0
    )

    if confidence_score >= settings.CONFIDENCE_THRESHOLD:
        return "complete"

    return "review"