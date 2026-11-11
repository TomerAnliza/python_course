"""לקוח MCP גולמי: מדבר עם server.py ב-JSON-RPC מעל stdio, בלי ספרייה."""
import json
import subprocess
import sys

# מריצים את השרת כתהליך-בן. ה-stdin שלו הוא הערוץ שלנו אליו, ה-stdout הערוץ ממנו אלינו.
proc = subprocess.Popen(
    [sys.executable, "server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True,
)


def send(msg: dict) -> None:
    """שולח הודעת JSON-RPC אחת: שורה אחת של JSON ואחריה ירידת שורה."""
    line = json.dumps(msg)
    print(f"\n>>> שולחים:\n{line}")
    proc.stdin.write(line + "\n")
    proc.stdin.flush()


def receive() -> dict:
    """קורא תשובה אחת: שורה אחת של JSON."""
    line = proc.stdout.readline()
    msg = json.loads(line)
    print(f"<<< מתקבל:\n{json.dumps(msg, indent=2, ensure_ascii=False)}")
    return msg


# שלב 1: לחיצת יד. הלקוח מציג את עצמו והשרת עונה מה הוא יודע לעשות.
send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
    "protocolVersion": "2025-06-18", "capabilities": {},
    "clientInfo": {"name": "classroom-demo", "version": "0.1"}}})
receive()

# שלב 2: הודעה (בלי id) שהלקוח מוכן. על הודעה לא מצפים לתשובה.
send({"jsonrpc": "2.0", "method": "notifications/initialized"})

# שלב 3: קריאה לכלי. זה בדיוק מה שמודל שפה עושה כשהוא "משתמש בכלי".
send({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
      "params": {"name": "add", "arguments": {"a": 7, "b": 5}}})
receive()

proc.stdin.close()
proc.wait(timeout=5)
