REPLAYS = []

def save(line: str):
    REPLAYS.append(line)

def show_menu():
    if not REPLAYS:
        print("No mission replays yet.")
        return
    print("\n🎬 REPLAYS (latest first):")
    for i, r in enumerate(reversed(REPLAYS), 1):
        print(i, r)
