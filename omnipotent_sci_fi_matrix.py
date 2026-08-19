import os
import time
import json
import hashlib
import sys
from datetime import datetime

# ==========================================
# 1. 架構與路徑設定
# ==========================================
BASE_DIR = ".omnipotent_sci_fi_matrix"
DATA_DIR = os.path.join(BASE_DIR, "secure_core")
LOG_DIR = os.path.join(BASE_DIR, "audit_logs")
STATE_FILE = os.path.join(BASE_DIR, "system_state.json")

for d in [BASE_DIR, DATA_DIR, LOG_DIR]:
    os.makedirs(d, exist_ok=True)

# ==========================================
# 2. 科幻視覺與日誌模組
# ==========================================
def sci_fi_print(text, delay=0.02):
    """模擬未來科技指揮中心的逐字掃描輸出"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def write_audit_log(message, level="INFO"):
    """現實級系統審計追蹤紀錄"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_path = os.path.join(LOG_DIR, "matrix_operations.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

# ==========================================
# 3. 狀態管理與雜湊鏈結模組
# ==========================================
def load_system_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"total_runs": 0, "defense_integrity": 100.0}

def save_system_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)

def get_latest_block_hash():
    """取得鏈結上的最後一個雜湊指紋，確保歷史不可篡改"""
    files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".json")])
    if not files:
        return "0" * 64
    with open(os.path.join(DATA_DIR, files[-1]), "r", encoding="utf-8") as f:
        return json.load(f).get("current_hash", "0" * 64)

# ==========================================
# 4. 核心融合執行主程式
# ==========================================
def run_omnipotent_matrix():
    # 初始化科幻風介面
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;32m")
    print("=" * 68)
    print(" [OMNIPOTENT MATRIX] 啟動全數據融合與動態防禦演化協定 v5.0")
    print(" [STATUS] 零信任核心載入中 | 硬體物理噪點同步中...")
    print("=" * 68 + "\033[0m")
    time.sleep(0.4)

    # 模擬多維度檢核動畫
    steps = [
        "[*] 正在擷取當下系統高精度硬體效能噪點 (Hardware Entropy)...",
        "[*] 正在執行防禦完整性與自適應邊界檢核...",
        "[*] 正在與前一代區塊進行 SHA-256 密碼學鏈結對齊...",
        "[*] 矩陣防護護甲重組完畢，準備寫入不可變核心..."
    ]
    for step in steps:
        sci_fi_print(f"\033[36m{step}\033[0m", 0.015)
        time.sleep(0.2)

    # 載入狀態
    state = load_system_state()
    state["total_runs"] += 1

    # 捕捉真實硬體物理噪點
    perf_counter = time.perf_counter_ns()
    env_noise = os.urandom(16)
    raw_seed = f"{perf_counter}:{env_noise.hex()}:{time.time()}".encode("utf-8")
    entropy_fingerprint = hashlib.sha256(raw_seed).hexdigest()

    # 取得前代雜湊鎖定
    prev_hash = get_latest_block_hash()
    existing_blocks = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    gen_id = len(existing_blocks) + 1

    # 封裝當前區塊數據
    block_data = {
        "generation": gen_id,
        "timestamp": datetime.now().isoformat(),
        "previous_hash": prev_hash,
        "hardware_entropy": entropy_fingerprint,
        "metrics": {
            "defense_integrity": state["defense_integrity"],
            "cumulative_runs": state["total_runs"]
        }
    }

    # 計算當代雜湊指紋（區塊鏈結核心）
    block_str = json.dumps(block_data, sort_keys=True).encode("utf-8")
    current_hash = hashlib.sha256(block_str).hexdigest()
    block_data["current_hash"] = current_hash

    # 寫入硬碟與日誌
    filename = f"gen_{gen_id:03d}_fusion.json"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(block_data, f, indent=4)

    save_system_state(state)
    write_audit_log(f"成功演化至第 {gen_id} 代。指紋: {current_hash}", "SUCCESS")

    # 科幻風最終結算面板
    print("\n" + "\033[1;33m" + "┌─────────────────────────────────────────────────────────────┐")
    print(f"│ 🧬 世代突破成功 [GEN: {gen_id:03d}]                                 │")
    print(f"│ 🔗 區塊指紋: {current_hash[:32]}... │")
    print(f"│ 🛡️ 系統防禦完整度: {state['defense_integrity']}% (運作次數: {state['total_runs']})           │")
    print("└─────────────────────────────────────────────────────────────┘" + "\033[0m\n")

if __name__ == "__main__":
    try:
        run_omnipotent_matrix()
    except Exception as e:
        write_audit_log(f"系統異常攔截: {e}", "CRITICAL")
        print(f"\033[31m[CRITICAL] 系統遭遇例外阻斷: {e}\033[0m")
        sys.exit(1)
