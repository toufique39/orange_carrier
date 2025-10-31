import json
import websocket
from bot import notify_call

def on_message(ws, message):
    try:
        data = json.loads(message)
        if isinstance(data, list) and len(data) > 1:
            event_type = data[0]
            payload = data[1]

            if event_type == "call" and "calls" in payload:
                calls_data = payload["calls"].get("calls", [])
                for call in calls_data:
                    print("📲 New call:", call)
                    notify_call(call)
    except Exception as e:
        print("⚠️ Error parsing message:", e)

def on_error(ws, error):
    print("❌ WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔒 WebSocket closed")

def on_open(ws):
    print("🟢 Connected to OrangeCarrier Live Calls")

def run_listener(socket_url):
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        socket_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.run_forever()
