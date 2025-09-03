class MissionStats:
    def __init__(self):
        self.missions = 0
        self.success = 0
        self.net_reward = 0

    def record(self, ok: bool, delta: int):
        self.missions += 1
        if ok:
            self.success += 1
        self.net_reward += delta

    def show(self):
        print("\n📊 MISSION STATS")
        print(f"Runs: {self.missions} | Success: {self.success} | Net: ${self.net_reward}")
