import time
import requests
from datetime import datetime

ORE_TRACKER_URL = "https://ore-mining-tracker.supply/api/latest-block"  # example endpoint
LOG_FILE = "mining_log.txt"

def get_latest_block():
    """Fetch latest block info from Ore tracker."""
    try:
        response = requests.get(ORE_TRACKER_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("block_height") or data.get("height")
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

def log_block(block_height):
    """Write block info to local log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} - Block: {block_height}\n")

def main():
    print("[⛏️] Starting Ore Mining Tracker bot...")
    last_block = None
    while True:
        block = get_latest_block()
        if block and block != last_block:
            print(f"[NEW BLOCK] {block}")
            log_block(block)
            last_block = block
            # ⬇️ TODO: add auto-mining request here later
        time.sleep(10)  # poll every 10 seconds

if __name__ == "__main__":
    main()
