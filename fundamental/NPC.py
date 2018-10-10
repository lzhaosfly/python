class Character:
    def __init__(self, name: str, hp: int, level: str):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def speak(self):
        print(f"{self.name} heard there were monsters running around last night!")
