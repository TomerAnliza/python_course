from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.prompts import base
from pydantic import Field

# MCPServer מייצר שרת MCP מלא מתוך פונקציות פייתון מעוטרות
mcp = MCPServer("DocumentMCP", log_level="ERROR")

# "בסיס הנתונים" של הקורס: מילון בזיכרון של מסמכים מדומים
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


# --- Tools: פעולות שהמודל מחליט להפעיל ---

# כלי הדגמה מינימלי (כמו ב-quickstart של MCP): שני מספרים נכנסים, סכום יוצא.
# הסכמה של הפרמטרים נגזרת אוטומטית מרמזי הטיפוסים — זה מה שהמודל רואה.
@mcp.tool(name="add", description="Add two numbers and return the sum.")
def add(a: int, b: int) -> int:
    return a + b



@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string.",
)
def read_document(
    doc_id: str = Field(description="Id of the document to read"),
) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string.",
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(
        description="The text to replace. Must match exactly, including whitespace."
    ),
    new_str: str = Field(
        description="The new text to insert in place of the old text."
    ),
) -> None:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)


# --- Resources: מידע שהאפליקציה (לא המודל) מושכת לפי URI ---


# Resource סטטי: רשימת כל מזהי המסמכים. זה מה שמופיע ב-Inspector תחת Resources
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())


# Resource Template: URI עם פרמטר. זה "fetch_doc" שמופיע תחת Resource Templates
@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


# --- Prompts: תבניות שיחה מוכנות שהמשתמש בוחר להפעיל ---


@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format.",
)
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been edited,
provide a short summary of the changes you made.
"""
    return [base.UserMessage(prompt)]


if __name__ == "__main__":
    # STDIO: ה-Inspector (או כל לקוח MCP) מריץ את הקובץ כתהליך-בן ומדבר איתו דרך stdin/stdout
    mcp.run(transport="stdio")
