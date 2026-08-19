import os
import sys
import subprocess
import json
import datetime

class ProductionUniversalCore:
    def __init__(self, workspace="."):
        self.workspace = workspace
        self.state_file = os.path.join(workspace, "system_evolution_state.json")
        self.log_file = os.path.join(workspace, "evolution_secure.log")
        self.load_state()

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    def load_state(self):
        self.state = {"runs": 0, "last_active": None}
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict): self.state.update(data)
            except: pass

    def save_state(self):
        self.state["runs"] = self.state.get("runs", 0) + 1
        self.state["last_active"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=4)

    def run_cycle(self):
        self.log("=== 啟動真實核心運作週期 ===")
        self.save_state()
        result = subprocess.run("uname -a", shell=True, capture_output=True, text=True)
        self.log(f"系統檢查: {result.stdout.strip()}")
        self.log(f"執行次數: {self.state['runs']}")
        self.log("=== 核心運作週期結束 ===")

if __name__ == "__main__":
    core = ProductionUniversalCore()
    core.run_cycle()
