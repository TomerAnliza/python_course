"""Local classroom demo. No API key, external service, or private data required."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Classroom Lab")
DOCS = {
    "welcome": "Welcome to the AI Engineering course.",
    "schedule": "Next lesson: Python fundamentals and functions.",
}

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return their sum."""
    return a + b

@mcp.tool()
def read_doc(doc_id: str) -> str:
    """Read a classroom demo document by its ID: welcome or schedule."""
    if doc_id not in DOCS:
        raise ValueError(f"Unknown document: {doc_id}. Choose welcome or schedule.")
    return DOCS[doc_id]

@mcp.resource("classroom://guide")
def guide() -> str:
    """Return the classroom lab guide."""
    return "Use add for arithmetic. Read welcome or schedule with read_doc."

@mcp.prompt()
def study_plan(topic: str) -> str:
    """Create a reusable request for a study plan."""
    return (
        f"Create a beginner study plan for {topic}. "
        "Include a short explanation, one exercise, and a self-check question."
    )

if __name__ == "__main__":
    mcp.run(transport="stdio")
