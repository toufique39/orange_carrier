import threading
import json
from bot import run_bot
from listener import run_listener

# Load config
with open("config.json") as f:
    config = json.load(f)

if __name__ == "__main__":
    t1 = threading.Thread(target=run_bot)
    t1.start()

    run_listener(config["orange_socket_url"])
