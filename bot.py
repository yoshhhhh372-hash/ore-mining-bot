import requests
import time
from datetime import datetime

RPC_URL = "https://api.mainnet-beta.solana.com"
LOG_FILE = "block_test_log.txt"

def get_latest_slot():
    """Fetch latest Solana slot (block equivalent)."""
    try:
        res = requests.post(RPC_URL, json={"jsonrpc":"2.0","id":1,"method":"getSlot"})
        slot = res.json()["result"]
        return slot
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

def log_block(slot):
    """Write block info to local log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} | Slot: {slot}\n")

def main():
    print("[🧪 TEST MODE] Starting ORE block tracker...")
    last_slot = None
    while True:
        slot = get_latest_slot()
        if slot and slot != last_slot:
            print(f"[NEW BLOCK] {slot}")
            log_block(slot)
            # simulate fake mining
            print("[Simulated mining] Pretending to send a mine transaction...")
            last_slot = slot
        time.sleep(3)  # check every 3s

if __name__ == "__main__":
    main()
