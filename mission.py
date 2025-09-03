import random, time
from config import TARGET_ALTITUDE, FUEL_UNITS, TICK_DELAY, ROCKETS
from status import MissionStats
from replay import save as save_replay, show_menu as show_replays

class Rocket:
    def __init__(self, name, thrust, efficiency, stability):
        self.name=name; self.thrust=thrust; self.efficiency=efficiency; self.stability=stability
        self.alt=0; self.fuel=FUEL_UNITS
    def tick(self):
        if self.fuel <= 0:
            return
        jitter = 1 if random.random() < (self.stability/20) else 0
        climb = max(1, self.thrust + jitter)
        self.alt += climb
        burn = max(1, 3 - (self.efficiency//3))
        self.fuel -= burn

class Economy:
    def __init__(self):
        self.credits = 1000
        self.bet_amount = 0
    def bet(self, amt):
        if amt <= 0 or amt > self.credits:
            print("❌ Invalid amount"); return False
        self.bet_amount = amt; self.credits -= amt; return True
    def settle(self, success):
        if self.bet_amount == 0: return 0
        if success:
            win = int(self.bet_amount * 2.2)
            self.credits += win
            return win - self.bet_amount
        return -self.bet_amount

DEV_MODE_AVAILABLE = True
from dev_utils import check_access  # lazy import behavior simple enough here


def pick_rockets():
    return random.sample([Rocket(**r) for r in ROCKETS], 3)


def run_single(stats: MissionStats):
    ships = pick_rockets()
    print("\n🚀 Choose your rocket:")
    for i, s in enumerate(ships, 1):
        print(f"{i}. {s.name} (T:{s.thrust} E:{s.efficiency} S:{s.stability})")
    try:
        idx = int(input("Bet on a mission (1-3, 0 skip): "))
    except: idx = 0
    eco = Economy()
    if 1 <= idx <= 3:
        try:
            amt = int(input("Credits to invest: $"))
            eco.bet(amt)
        except: pass
    input("Press Enter to launch...")
    winner = random.choice(ships)
    while winner.alt < TARGET_ALTITUDE and winner.fuel > 0:
        for s in ships:
            s.tick()
        time.sleep(TICK_DELAY)
    success = winner.alt >= TARGET_ALTITUDE
    delta = eco.settle(success)
    save_replay(f"{winner.name} reached {winner.alt} (success={success})")
    stats.record(success, delta)
    print("\n🏁 RESULT:", "Orbit achieved!" if success else "Mission failed.")


def main():
    stats = MissionStats()
    print("""
    🛰️=======================================🛰️
           SPACE MISSION SIMULATOR
    🛰️=======================================🛰️
    """)
    while True:
        print("\n1. 🚀 Launch Mission\n2. 📊 Statistics\n3. 🎬 Replays\n4. 🚪 Exit")
        if DEV_MODE_AVAILABLE:
            print("9. 🔧 Developer Mode")
        c = input(">> ")
        if c == '1': run_single(stats)
        elif c == '2': stats.show()
        elif c == '3': show_replays()
        elif c == '4': break
        elif c == '9' and DEV_MODE_AVAILABLE: check_access()
        else: print("❌ Invalid choice")

if __name__ == '__main__':
    main()
