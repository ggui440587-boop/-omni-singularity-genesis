import platform
import os

def main():
    print(">>> 真實生命體啟動：正在探測宿主真實系統環境...")
    info = {
        "system": platform.system(),
        "release": platform.release(),
        "cpu_cores": os.cpu_count()
    }
    print(f">>> 探測結果: {info}")
    metabolite_path = "metabolite_log.txt"
    with open(metabolite_path, "w", encoding="utf-8") as mf:
        mf.write("Metabolic active
")
    print(f">>> 真實代謝產物已寫入: {metabolite_path}")
    return "GEN_2_SURVIVED"

if __name__ == "__main__":
    result = main()
    print(f"EXIT_STATUS: {result}")
