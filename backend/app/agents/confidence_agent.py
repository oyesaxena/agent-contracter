async def confidence_agent(state):

    classification_confidence = (
        state["classification"].get(
            "confidence",
            0.5
        )
    )

    missing_count = len(
        state["validation"][
            "missing_fields"
        ]
    )

    score = (
        classification_confidence
        - (missing_count * 0.15)
    )

    score = max(score, 0)

    state["confidence_score"] = score

    state["review_required"] = (
        score < 0.8
    )
    state["current_node"] = "confidence"
    if "execution_logs" not in state:
        state["execution_logs"] = []
    state["execution_logs"].append({
    "node": "confidence",
    "output": {
        "confidence_score": score
    }
})
    return state