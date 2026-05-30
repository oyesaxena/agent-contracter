from langgraph.graph import (
    StateGraph,
    END
)

from app.workflows.state import (
    WorkflowState
)

from app.workflows.router import (
    workflow_router
)

from app.agents.classification_agent import (
    classification_agent
)

from app.agents.extraction_agent import (
    extraction_agent
)

from app.agents.validation_agent import (
    validation_agent
)

from app.agents.confidence_agent import (
    confidence_agent
)


graph = StateGraph(
    WorkflowState
)

# Nodes

graph.add_node(
    "classification",
    classification_agent
)

graph.add_node(
    "extraction",
    extraction_agent
)

graph.add_node(
    "validation",
    validation_agent
)

graph.add_node(
    "confidence",
    confidence_agent
)

# Entry Point

graph.set_entry_point(
    "classification"
)

# Edges

graph.add_edge(
    "classification",
    "extraction"
)

graph.add_edge(
    "extraction",
    "validation"
)

graph.add_edge(
    "validation",
    "confidence"
)

# Conditional Routing

graph.add_conditional_edges(
    "confidence",
    workflow_router,
    {
        "complete": END,
        "review": END
    }
)

workflow = graph.compile()