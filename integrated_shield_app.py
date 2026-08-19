import sys
import os
import time
import hmac
import hashlib
from datetime import datetime

# ==================== 第一部分：防禦裝甲引擎 ====================
class EnterpriseMemoryShield:
    def __init__(self, master_secret_key="SECURE_SYSTEM_SALT_9981"):
        self._salt = master_secret_key.encode('utf-8')
        
        # 1. 核心記憶體金絲雀（動態校驗碼）
        self._canary_core = "CANARY_ALIVE_STATE_0xF00A"
        
        # 2. 多重蜜罐陷阱（Honeytokens）配置
        self.honeytokens = {
            "db_admin_pass": "DB_ROOT_SECRET_PASS_999",
            "aws_api_token": "AKIA_FAKE_PRODUCTION_KEY_XYZ",
            "internal_token": "BEARER_SUPER_ADMIN_JWT_TOKEN"
        }
        
        self.security_breached = False
        self.incident_log_path = "security_incident.log"

    def _log_incident(self, event_type, details):
        """將資安事件寫入日誌"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{event_type}] {details}"
        print(f"\033[91m{log_entry}\033[0m") # 紅色警示輸出
        
        with open(self.incident_log_path, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    def pulse_check(self):
        """系統常態心跳：檢查記憶體金絲雀是否遭到覆蓋或指標篡改"""
        if self._canary_core != "CANARY_ALIVE_STATE_0xF00A":
            self.security_breached = True
            self._log_incident("CRITICAL", "偵測到記憶體金絲雀損壞！記憶體可能遭到惡意注入或溢位攻擊。")
            return False
        return True

    def touch_honeytoken(self, token_name, accessor_identity):
        """當任何模組或外部輸入觸及蜜罐陷阱時的即時攔截點"""
        if token_name in self.honeytokens:
            self._log_incident("HONEYPOT_TRIPPED", f"主體 [{accessor_identity}] 觸碰了誘餌蜜罐 [{token_name}]！")
            self.security_breached = True
            return None
        return "ACCESS_DENIED"

    def trigger_kill_switch(self):
        """執行強制熔斷與安全終止"""
        self._log_incident("KILL_SWITCH", "系統正在執行緊急熔斷，清除敏感暫存並安全退出...")
        sys.exit(1)


# ==================== 第二部分：專案主程式邏輯 ====================
class MyRealProjectApp:
    def __init__(self):
        # 初始化防禦裝甲
        self.shield = EnterpriseMemoryShield()
        print("[APP] 🚀 專案主程式啟動，單一整合版安全防禦裝甲已掛載。")

    def run_business_logic(self):
        """專案原本的商業邏輯"""
        print("[APP] 正在執行正常業務邏輯...")
        
        # 1. 模擬日常心跳檢測
        if not self.shield.pulse_check():
            print("[ALERT] 偵測到記憶體遭到汙染！")
            self.shield.trigger_kill_switch()

        # 2. 模擬程式嘗試存取組態
        print("[APP] 嘗試載入系統組態...")
        
        # 3. 故意觸碰蜜罐陷阱以展示防禦效果
        unauthorized_access = self.shield.touch_honeytoken("aws_api_token", "module_x_suspicious")
        
        if unauthorized_access is None:
            print("[APP] 🛑 安全攔截生效：拒絕提供敏感資料，準備終止行程。")
            self.shield.trigger_kill_switch()


if __name__ == "__main__":
    app = MyRealProjectApp()
    app.run_business_logic()

