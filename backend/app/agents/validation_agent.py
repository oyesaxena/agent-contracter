async def validation_agent(state):

    extraction = state["extraction"]

    missing_fields = []

    required_fields = [
        "parties",
        "effective_date"
    ]

    for field in required_fields:

        value = extraction.get(field)

        if not value:

            missing_fields.append(
                field
            )

    state["validation"] = {
        "valid": len(missing_fields) == 0,
        "missing_fields": missing_fields
    }

    state["current_node"] = (
        "validation"
    )

    state["execution_logs"].append({
    "node": "validation",
    "output": state["validation"]
    })

    return state