import os

code_content = '''import os
import subprocess
import sys
from datetime import datetime

LAB_DIR = ".real_evolution_sandbox"
ORGANISM_FILE = os.path.join(LAB_DIR, "organism.py")
os.makedirs(LAB_DIR, exist_ok=True)

def log_real(message):
    print(f"[REAL_AGENT] {datetime.now().strftime('%H:%M:%S')} -> {message}")

def initialize_organism():
    if not os.path.exists(ORGANISM_FILE):
        code = \"\"\"import platform
import os

def main():
    print(">>> 真實生命體啟動：正在探測宿主真實系統環境...")
    info = {
        "system": platform.system(),
        "release": platform.release(),
        "cpu_cores": os.cpu_count()
    }
    print(f">>> 探測結果: {info}")
    return "GEN_1_SURVIVED"

if __name__ == "__main__":
    result = main()
    print(f"EXIT_STATUS: {result}")
\"\"\"
        with open(ORGANISM_FILE, "w", encoding="utf-8") as f:
            f.write(code)
        log_real("第一代真實有機體已在沙盒中誕生。")

def execute_organism():
    log_real(f"正在真實調用並執行: {ORGANISM_FILE}")
    result = subprocess.run([sys.executable, ORGANISM_FILE], capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def evolve_organism_real():
    with open(ORGANISM_FILE, "r", encoding="utf-8") as f:
        current_code = f.read()

    if "GEN_1_SURVIVED" in current_code and "GEN_2_SURVIVED" not in current_code:
        log_real("觸發真實基因突變：解鎖【本地檔案系統真實寫入】能力...")
        mutated_code = current_code.replace(
            'return "GEN_1_SURVIVED"',
            'metabolite_path = "metabolite_log.txt"\\n    with open(metabolite_path, "w", encoding="utf-8") as mf:\\n        mf.write("Metabolic active\\n")\\n    print(f">>> 真實代謝產物已寫入: {metabolite_path}")\\n    return "GEN_2_SURVIVED"'
        )
        with open(ORGANISM_FILE, "w", encoding="utf-8") as f:
            f.write(mutated_code)
        log_real("第二代基因已成功寫入硬碟！")
        return True
    return False

if __name__ == "__main__":
    log_real("🔥 啟動非模擬、百分之百真實的自主演化迴圈...")
    initialize_organism()
    code, stdout, stderr = execute_organism()
    print("-" * 50)
    print(stdout.strip())
    print("-" * 50)
    if code == 0:
        evolve_organism_real()
'''

with open("real_self_evolving_agent.py", "w", encoding="utf-8") as f:
    f.write(code_content)

print("✅ 檔案建立成功！現在可以執行了。")

