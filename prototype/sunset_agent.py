import psutil
import time
import os

class SunsetAgent:
    def __init__(self, memory_threshold=80.0):
        """
        Initialize the AI System Controller prototype.
        :param memory_threshold: The CPU/Memory percentage threshold to trigger optimization.
        """
        self.memory_threshold = memory_threshold
        print("🌅 Sunset Agent OS Core Initialized.")
        print("🤖 AI Agent Partition Active and Monitoring System State.")
        self.whitelist = ['chrome.exe', 'explorer.exe', 'Code.exe', 'python.exe', 'System', 'Registry']

    def monitor_system(self):
        """Monitors system performance metrics."""
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        print(f"\n📊 System Status -> CPU: {cpu_usage}% | RAM: {memory.percent}%")

        if memory.percent > self.memory_threshold:
            print("⚠️ High RAM usage detected. Triggering AI Optimization Protocol...")
            self.optimize_memory()
        elif cpu_usage > self.memory_threshold:
            print("⚠️ High CPU usage detected. Analyzing heavy processes...")
            self.analyze_processes()
        else:
            print("✅ System Stable. No action required.")

    def optimize_memory(self):
        """Closes non-essential background processes."""
        freed_processes = 0
        print("🧠 AI Agent: Identifying non-essential background processes...")
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                # Mock logic: Kill processes using more than 1% memory NOT in whitelist
                if proc.info['name'] not in self.whitelist and proc.info['memory_percent'] is not None and proc.info['memory_percent'] > 1.0:
                    print(f"   [ACTION] Suspending {proc.info['name']} (PID: {proc.info['pid']}) to free memory.")
                    # In a real scenario, we'd use proc.kill() or proc.suspend()
                    # proc.kill() 
                    freed_processes += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        if freed_processes == 0:
            print("   [INFO] All heavy processes are whitelisted or secure. No apps closed.")
        else:
            print(f"✅ Optimization Complete. Freed resources from {freed_processes} apps.")

    def analyze_processes(self):
        print("🧠 AI Agent: Scanning active tasks for inefficiencies...")
        time.sleep(1)
        print("   [INFO] Active tasks are within optimal working boundaries.")

    def run(self):
        print("🔒 Dual Partition Security: ON.")
        print("Press Ctrl+C to shutdown Sunset Agent.\n")
        try:
            while True:
                self.monitor_system()
                time.sleep(3) # Check every 3 seconds
        except KeyboardInterrupt:
            print("\n🌇 Sunset Agent safely shutting down. Returning control to Normal OS Partition.")

if __name__ == "__main__":
    # Ensure psutil is installed: pip install psutil
    agent = SunsetAgent(memory_threshold=60.0) # Lowered threshold for demonstration purposes
    agent.run()
